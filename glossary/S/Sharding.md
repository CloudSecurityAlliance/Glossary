# Sharding

In a sharding, nodes hold a subset of the state (UTXOs), and a subset of the
blockchain. Instead of miners/validators redundantly doing the same work,
they are going share the load but still have an only economic assurance
even though they’re not going to validate every transaction. For example, a
sharding scheme on Ethereum might put all addresses starting with 0x00
into one shard, all addresses starting with 0x01 into another shard, etc. In a
simple version of the scheme, each user maintains a light client on all shards,
while validators fully download and track a few shards that they are assigned
to at some particular time.
Source: https://diyhpl.us/wiki/transcripts/scalingbitcoin/sharding-theblockchain/ and https://github.com/ethereum/wiki/wiki/Sharding-FAQ

## Tags

Tag: BlockchainArchitecture
