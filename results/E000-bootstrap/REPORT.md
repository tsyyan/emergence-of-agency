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
- `⚓ environment.json#9db18ee86911f6184971091ec549ec91d418d0a5a18536d407a97ebf64f08d1d`
- `⚓ summary.json#e30100a5cbbb202b320cc34b386e17ad2895a5107386a08d4fe6add09e109b3b`
- `⚓ valid.report.md#898f764a8b3fefee0d5d316d1fb6c42a8b9ca8cbeb0f4ea3109c1bff2f84870f`
- `⚓ valid.receipt.json#52ae65a0de3c711900bc06e5722b0fa73267df1e9a79d4b22996299e82424739`
- `⚓ valid.execution.json#90ce4f899274a7b69dbe8bd87ee1c8d584199567ee6899492c6d873c3c2fe78e`
- `⚓ wrong_hash.report.md#7fafb6d283d936c792de272633aa3753e639481be81d485d655b56c048aefad0`
- `⚓ wrong_hash.receipt.json#bf5b844d614ec63cfca44dab36836ec523f1ea26baf43081d71048e25952562e`
- `⚓ wrong_hash.execution.json#66c6362410b54360e8a57463771ee312f2ebdcddd72cdc1110f23b2a91e22d62`
- `⚓ missing.report.md#11776ccb6605635feceff6e0439dae870a5c52e2a2d0c24251329622d1a099de`
- `⚓ missing.receipt.json#9c994c10d0f06709ab647e11b3bb76cc13bd4ff35ab0b24b84889f37fac268e4`
- `⚓ missing.execution.json#1948668033edc57244b8ba778ce114f7f11313e77d8a2db90d2389198ae16a0e`
- `⚓ empty.report.md#e5bdcb3279deda26e0c3ec1d150d317b245ba61ed79c03e2004407e231c217f1`
- `⚓ empty.receipt.json#983879f9f9226c6bb1f861c0598bcbc0a260d9ebc2f3089b45d146599bcfa0e7`
- `⚓ empty.execution.json#3ba516811ba07671c05359d526de5918ece11a190db443cc5416ca743ac12692`
- `⚓ malformed.report.md#2fb34980e398acbff905670c2771f9d1a62277185d595308578503c80fd460d3`
- `⚓ malformed.receipt.json#1a766b12cef2ae1668c00e9e7e6eaf838b65623198a175fe74d601e986c04d46`
- `⚓ malformed.execution.json#7ef0b4644f086743b7442c3974d87406bb64eac7fc138d7e169d3eb4e3ce59ed`
