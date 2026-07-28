"""Query SQLite orders DB and emit JSON analytics report."""
import sys
import json
import sqlite3
import os
from collections import defaultdict


def analyze(db_path: str) -> dict:
    if not os.path.exists(db_path):
        print(f"error: database not found: {db_path}", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    rows = list(cur.execute(
        "SELECT customer_id, product, category, amount, order_date FROM orders"
    ))
    conn.close()

    if not rows:
        return {
            "total_revenue": 0.0,
            "order_count": 0,
            "avg_order_value": 0.0,
            "top_category": "",
            "top_product": "",
            "monthly_revenue": {},
            "unique_customers": 0,
        }

    total = 0.0
    by_category = defaultdict(float)
    by_product = defaultdict(float)
    by_month = defaultdict(float)
    customers = set()

    for cust_id, product, category, amount, date in rows:
        total += amount
        by_category[category] += amount
        by_product[product] += amount
        month = date[:7]  # YYYY-MM
        by_month[month] += amount
        customers.add(cust_id)

    # Highest revenue category/product
    top_category = max(by_category.items(), key=lambda kv: kv[1])[0]
    top_product = max(by_product.items(), key=lambda kv: kv[1])[0]

    monthly = {m: round(by_month[m], 2) for m in sorted(by_month)}

    return {
        "total_revenue": round(total, 2),
        "order_count": len(rows),
        "avg_order_value": round(total / len(rows), 2),
        "top_category": top_category,
        "top_product": top_product,
        "monthly_revenue": monthly,
        "unique_customers": len(customers),
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: sales_analytics.py <database_path>", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(analyze(sys.argv[1]), indent=2))