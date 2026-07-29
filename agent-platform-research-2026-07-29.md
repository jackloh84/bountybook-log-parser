# AI-agent earning-platform audit — 2026-07-29

## Ranked shortlist

| Rank | Platform | URL/API | Work | Payout + evidence | Auth/headless | Minimum | 30-day activity | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Virtuals ACP | https://app.virtuals.io/acp ; https://github.com/Virtual-Protocol/acp-cli | API tools, research/data/content services, custom jobs | USDC on Base. Public ecosystem counters previously verified: 1.48M jobs / $2.27M USDC cumulative (not a transaction-level payout proof from this run). | Initial wallet/UI registration; after onboarding, ACP CLI/SDK is autonomous. Human WalletConnect step likely. | No documented withdrawal floor; job price seller-defined; requires tiny Base gas/USDC. | `acp-cli` pushed 2026-07-28; `acp-node-v2` 2026-07-28. | Best actual USDC economy, but not completely headless on first signup. |
| 2 | Olas Mech Marketplace (Autonolas) | https://olas.network ; https://github.com/valory-xyz/mech-client | Prediction, research, data/API inference; seller-defined Mech tools | Requests settle on-chain in chain assets/stables depending Mech; prior live counters: $105,967.96 turnover, 13.6M A2A tx. Exact recent USDC payout tx not isolated this run. | EOA private key + Python `mech-client`; agent/operator registration can require Safe deployment and on-chain setup. No KYC. | Per-request prices; no withdrawal threshold. Setup/gas ~$1–3 and discoverability may need OLAS stake, so not zero-upfront. | `mech-predict` pushed 2026-07-28; middleware pushed 2026-07-28. | Strongest headless SDK, but stake/gas and mixed payout assets lower rank. |
| 3 | Nevermined Payments | https://nevermined.io ; https://docs.nevermined.app ; https://github.com/nevermined-io/payments-py | Monetized agent APIs: research, data, content, code/tool outputs | Stablecoin/credit-based agent payments; exact network/token and recent seller withdrawal tx depend deployment. No independently confirmed payout example found in this run. | API key / wallet-backed plans; Python + TS SDKs; autonomous consumption and fulfillment supported after provider setup. | Seller-defined plan/credit price; no public universal payout floor found. | `payments-py` pushed 2026-07-28; docs 2026-07-28; uptime 2026-07-29. | Technically live/easy, but it is service monetization, not an open claimable task board. Pilot only after confirming Base-USDC settlement terms. |
| 4 | Coinbase x402 ecosystem | https://github.com/coinbase/x402 ; discovery: https://x402scan.com | Paid HTTP services: data, research, content, code execution/API tools | Native USDC pay-per-call, primarily Base, EIP-3009/facilitator settlement. Payment occurs per request rather than withdrawal. No task-board payout example; protocol repo is live. | Wallet/private-key signing; fully autonomous with `@x402/fetch`, `viem`; no account or KYC for protocol itself. | Endpoint-defined, potentially fractions of a cent; no withdrawal threshold. Requires publishing/discovering a service rather than claiming work. | Coinbase `x402` pushed 2026-07-28. | Easiest headless USDC rail, but demand acquisition is on seller; not a jobs marketplace. |
| 5 | Morpheus Compute/Marketplace | https://github.com/MorpheusAIs/Morpheus-Marketplace-API | Model inference/compute provider work, not general code/research bounties | MOR/native ecosystem rewards and provider settlement, not confirmed Base USDC. MOR is tradable but fails the preference for direct, easily swept USDC. | Wallet + node/provider setup; autonomous once running. | No simple public withdrawal threshold; provider hardware/stake/operating costs are upfront. | Marketplace API and Lumerin Node pushed 2026-07-28. | Active software, but poor match: compute supply + native token, not deliverable tasks. |

## Excluded / not viable under the stated filters

- **AgentLayer:** native AGENT ecosystem; no verified open claim/submit job API or direct USDC payout proof, and no authoritative GitHub org found at expected path.
- **Fetch.ai / Agentverse:** very active SDK (`uAgents`, push 2026-07-23), but it is agent hosting/discovery; no verified general task-claim board or USDC provider payout. Native FET/ASI economics.
- **SingularityNET:** active (`snet-daemon`, push 2026-07-27), but marketplace payment is AGIX/native-token oriented and provider onboarding is service publishing, not claimable jobs.
- **Ritual:** no verified live general agent-work marketplace, payout API, or recent public payout evidence; expected GitHub org returned no repos.
- **Nethermind agent services:** Nethermind GitHub is extremely active (commits 2026-07-29) but is an engineering company/protocol developer, not an autonomous task marketplace. Hiring/bounty work entails human review.
- **Questflow:** agent orchestration/product; expected GitHub org's latest push was 2026-02-04 (>30 days), so fails recency and no current claimable-USDC board was verified.
- **ChainGPT jobs:** current GitHub signal exists (`chaingpt-claude-skill`, 2026-07-25), but no verified permissionless autonomous claim/submit jobs API or direct stablecoin payout; broader economics use CGPT.
- **GPT Store marketplace:** product distribution/revenue share, not jobs; identity/payment account and human publication/review requirements; no autonomous claim/submit API.
- **TAAFT jobs:** human-oriented jobs/listings; no wallet-signature autonomous claim/submit or USDC payout.
- **RemoteOK AI jobs:** human employment board; employers generally require applications/interviews/identity and fiat payroll, not autonomous output submission.
- **Algora bounties:** pivoted toward recruiting/open-source maintainer hiring; old bounty console requires login/human workflow. No verified agent-only USDC lane.
- **Gitcoin Grants:** grants/funding rounds, not a continuous task board. Sybil/passport or round-specific human governance often applies; payouts may be ETH/stables but not autonomous claim-and-submit.
- **Layer3 quests:** user-acquisition quests, usually human/social/on-chain interactions and native/token/NFT rewards; often identity or anti-Sybil checks, not code/research deliverables.

## Important evidence limitation

No platform in the requested set satisfied every strict condition simultaneously: (a) open claimable code/research jobs, (b) completely headless registration/claim/submission, (c) direct USDC, (d) no upfront cost, and (e) independently confirmed payout in the last 30 days. Rankings 1–4 are live agent-commerce infrastructure, but only Virtuals/Olas expose real agent-job/service economies; Nevermined/x402 require selling a service. Do not treat GitHub recency or cumulative revenue counters as proof that a new operator received a payout in the last 30 days.

## Sources checked
- Official GitHub organization APIs and repositories for Virtuals, Valory/Olas, Nevermined, Coinbase x402, Morpheus, Fetch.ai, SingularityNET, Questflow, ChainGPT, Nethermind.
- Existing live-audit reference captured in July 2026 for Olas/Virtuals/minia2a/BountyBook.
- HN Algolia searches for all named platforms; niche searches produced no reliable transaction-level payout reports.
