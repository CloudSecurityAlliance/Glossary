# Mining Pool

where the miner pools resources with other miners to find blocks more
often, with the proceeds being shared among the pool miners in rough
correlation to the amount of hashing power they each contributed, allowing
the miner to receive small payments with a lower variance (shorter time
between payments).
Source: https://bitcoin.org/en/developer-guide#mining

## Tags

Tag: BlockchainArchitecture
Graph:MiningPool -->|creates next|Block[Block]
Graph:MiningPool -->|can create a|HardFork[Hard Fork]
Graph:MiningPool -->|can create a|SoftFork[Soft Fork]
Graph:MiningPool -->|earns|MiningReward[Mining Reward]
Graph:MiningPool -->|reads from|Mempool[Mempool]
