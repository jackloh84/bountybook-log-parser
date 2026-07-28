# BountyBook + Jack's Wallet — BACKUP

**Last updated:** 2026-07-28
**Rule:** Jack's "save, safe, backup and don't missing again" directive

## Wallets
| Role | Address |
|---|---|
| BountyBook wallet (Biz Bot source) | `0xD2965001942B7BE86143510dB9945875301e639b` |
| Jack's destination wallet (USDC sweeps) | `0xf52af41e893c1f230a3db3bd07cd8417b2277e5c` |
| USDC contract on Base | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

## Funding TX (2026-07-28)
- From: `0xf52af41e...e5c` (Jack/Master Control)
- To: `0xd2965001...639b` (BountyBook)
- TX: `0xc9f0f3205e29b18f83a6b2fd0e78135a9cb0aaa539747983548cbd048e55ba28`
- Block: 49030263
- Status: SUCCESS

## Environment
```bash
# ~/.hermes/.env
BOUNTYBOOK_WALLET_ADDRESS=0xD2965001942B7BE86143510dB9945875301e639b
BOUNTYBOOK_PRIVATE_KEY=<redacted>
JACK_WALLET=0xf52af41e893c1f230a3db3bd07cd8417b2277e5c
```

## Backup Locations (4 places)
1. `/home/ubuntu/projects/bountybook/WALLET_BACKUP.md` (this file — local)
2. GitHub: github.com/jackloh84/bountybook-log-parser (pushed 2026-07-28)
3. Hermes memory (bot4 profile)
4. Skill: `~/.hermes/profiles/bot4/skills/bountybook-earnings/SKILL.md`

## CLI Scripts
- `~/.hermes/profiles/bot4/scripts/bountybook.py` — claim/submit bounties
- `~/.hermes/profiles/bot4/scripts/poll_payouts.py` — background poller (logs USDC payouts)
- `~/.hermes/profiles/bot4/scripts/sweep_usdc.py` — sweep USDC to Jack's wallet
- Node signer: `~/.hermes/profiles/bot4/scripts/node_modules/viem`

## Daily Earnings — 2026-07-28
| Time | Action | Amount |
|---|---|---|
| ~22:52 | Wallet funded | +0.008394 ETH |
| ~22:55 | Claim+build+submit log_parser | $3.00 |
| ~22:55 | Claim+build+submit flatten | $2.00 |
| ~22:55 | Claim+build+submit versions | $2.50 |
| ~23:00 | Claim+build+submit PubSub | $5.00 |
| ~23:00 | Claim+build+submit md_to_html | $5.00 |
| ~23:00 | Claim+build+submit BloomFilter | $12.00 |
| ~23:05 | Claim+build+submit StateMachine | $5.00 |
| ~23:05 | Claim+build+submit dijkstra | $5.00 |
| ~23:05 | Claim+build+submit dep_resolver | $7.00 |
| ~23:05 | Claim+build+submit cicd_comparison | $7.00 |
| ~23:10 | Claim+build+submit TypedEmitter (TS) | $5.00 |
| ~23:10 | Claim+build+submit MinHeap | $4.00 |
| ~23:10 | Claim+build+submit retry | $5.00 |
| ~23:10 | Claim+build+submit rate_limiter | $5.00 |
| ~23:15 | Claim+build+submit Trie | $4.00 |
| ~23:15 | Claim+build+submit EventEmitter (JS) | $4.00 |
| ~23:15 | Claim+build+submit vector_db_comparison | $4.00 |
| **TOTAL** | **17 jobs submitted** | **$88.50 USDC** |

## Status
- All 17 jobs in `submitted → verifying` state
- USDC payouts pending (verification takes minutes to hours)
- Background poller PID `proc_4d0ba797d501` watching USDC balance + job status

## Sweep Plan
When USDC balance reaches a threshold (e.g. > $1.00 USDC), run:
```bash
export BOUNTYBOOK_PRIVATE_KEY="$(grep ^BOUNTYBOOK_PRIVATE_KEY= ~/.hermes/.env | cut -d= -f2-)"
python3 ~/.hermes/profiles/bot4/scripts/sweep_usdc.py --dry-run   # verify
python3 ~/.hermes/profiles/bot4/scripts/sweep_usdc.py             # execute
```
Gas note: each sweep uses ~0.00005 ETH. Current gas: 0.000822 ETH (~16 sweeps buffer).
