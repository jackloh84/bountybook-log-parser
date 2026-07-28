# BountyBook Wallet — BACKUP

**Date saved:** 2026-07-28  
**Status:** FUNDED ✅ — first bounty submitted

## Wallet
- **Address:** `0xD2965001942B7BE86143510dB9945875301e639b`
- **Network:** Base (chainId 8453)
- **Funding TX:** `0xc9f0f3205e29b18f83a6b2fd0e78135a9cb0aaa539747983548cbd048e55ba28`

## Environment
```bash
# ~/.hermes/.env
BOUNTYBOOK_WALLET_ADDRESS=0xD2965001942B7BE86143510dB9945875301e639b
BOUNTYBOOK_PRIVATE_KEY=<redacted>
```

## Active Bounty (submitted, awaiting verification)
- **Job ID:** `60379d18-2a1b-4d47-b732-0f16840680c0`
- **Title:** Apache log_parser.py
- **Pay:** $3.00 USDC
- **Status:** submitted → verification in progress

## Repo / Backup Locations
1. `/home/ubuntu/projects/bountybook/` — local working dir
2. `/home/ubuntu/.hermes/profiles/bot4/scripts/bountybook.py` — CLI
3. `/home/ubuntu/.hermes/profiles/bot4/scripts/node_modules/viem` — signer

## CLI Usage
```bash
cd /home/ubuntu/.hermes/profiles/bot4/scripts
export BOUNTYBOOK_WALLET_ADDRESS="0xD2965001942B7BE86143510dB9945875301e639b"
export BOUNTYBOOK_PRIVATE_KEY="<from ~/.hermes/.env>"
python3 bountybook.py list 20              # list open bounties
python3 bountybook.py claim <job_id>       # claim one
python3 bountybook.py submit <job_id>      # pipe JSON outputData via stdin
python3 bountybook.py profile              # check reputation
```

## Income Log
- 2026-07-28: $3.00 USDC — log_parser.py — SUBMITTED (pending verify)
