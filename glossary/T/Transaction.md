# Transaction

A request by a transactor to execute a function on the blockchain
network. The transaction types are deployed, invoked, and queried, which
are implemented through the chaincode functions set forth in the fabric’s
API contract.
Source: https://console.ng.bluemix.net/docs/services/blockchain/ibmblockchain_overview.html

## Tags

Category:BlockchainArchitecture
Graph:Transaction -->|is sent to|Mempool[Mempool]
Graph:Transaction -->|contains a|TransactionFee[Transaction Fee]
