# Beacon Chain

A beacon chain contains records covering activities in a sharded chain, the beacon chain does not contain transactions but acts as a coordinating mechanism instead.

## Tags

Tag: BlockchainArchitecture
Graph:BeaconChain -->|sends transactions to|MainChain[Main Chain]
Graph:BeaconChain -->|receives transactions from|ShardChain[Shard Chain]
