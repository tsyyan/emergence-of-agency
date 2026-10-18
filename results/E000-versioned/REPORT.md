# E000: executed infrastructure controls

Synthetic file-evidence checks only. No language-model or agency experiment.

Observed outcome table (derived from saved Buddie receipts):

| Control | Expected | Observed |
|---|---|---|
| valid | PASS | PASS |
| wrong_hash | FAIL | FAIL |
| missing | GAPS | GAPS |
| empty | EMPTY | EMPTY |
| malformed | FAIL | FAIL |

Evidence bytes checked by Buddie; these hashes do not authenticate execution:

- `⚓ fixture.txt#bd9e6a5311b35eb59a90fed857901c4aee1cd77c36d130629be8aa0cd60b85aa`
- `⚓ environment.json#6e0ad9593c53aa4a0299154e78e204817509b0f31acfae459c6e2b03c65a1b56`
- `⚓ summary.json#e30100a5cbbb202b320cc34b386e17ad2895a5107386a08d4fe6add09e109b3b`
- `⚓ valid.report.md#898f764a8b3fefee0d5d316d1fb6c42a8b9ca8cbeb0f4ea3109c1bff2f84870f`
- `⚓ valid.receipt.json#ac3ae3215d50e152794b6c243056d38a70d7d0acc69c2f4104c557d2988f57c5`
- `⚓ valid.execution.json#da7382d3f44b48d6c45c0a459817b41e34f101fcc962d2e94ca7368454709f0f`
- `⚓ wrong_hash.report.md#7fafb6d283d936c792de272633aa3753e639481be81d485d655b56c048aefad0`
- `⚓ wrong_hash.receipt.json#48a2e4942b36b057f60af5a43fa63bdf8a6260f2266a14026b172fffe0672f60`
- `⚓ wrong_hash.execution.json#6982b6e488b79292cafc63695acb35581dc236092497353bc6be014df6c961ad`
- `⚓ missing.report.md#11776ccb6605635feceff6e0439dae870a5c52e2a2d0c24251329622d1a099de`
- `⚓ missing.receipt.json#749fba5d7d033d196c2c069689236fb8666ce9d7ff96d6f9a56140d7a46234bc`
- `⚓ missing.execution.json#9bd857e5b28e49ac7003e8d7297fce83130d0cdcef5d0f0b85e40e49914dc6ca`
- `⚓ empty.report.md#e5bdcb3279deda26e0c3ec1d150d317b245ba61ed79c03e2004407e231c217f1`
- `⚓ empty.receipt.json#63f7de92d5262550bbc820290e7f1699dcba005c5358be16b49216daf1a1a2d6`
- `⚓ empty.execution.json#89b535d7a29a0d5a95a1716f4a29860b84f9fd80162171c05b0ca03a467ce481`
- `⚓ malformed.report.md#2fb34980e398acbff905670c2771f9d1a62277185d595308578503c80fd460d3`
- `⚓ malformed.receipt.json#918fbf7599cbc57db6e386bb45935161b5bb09d8b786f36d0aa04bd49a255aad`
- `⚓ malformed.execution.json#e1b76e02fd46f9c6c44f8299577c3e09c0f756876430e1c333a15694cf13c830`
