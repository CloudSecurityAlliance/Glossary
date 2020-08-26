```mermaid
graph LR
BlockchainAttack(BlockchainAttack)
34Attack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
51Attack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
BlockMiningTimejackAttack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
BlockMiningTimejackAttack -->|type of|AttackAgainstNode[Attack Against Node]
EclipseAttack -->|contributes to|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
LongRangeAttack -->|type of attack against|ProofofStakePOS[Proof of Stake POS]
LongRangeAttack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
LongRangeAttack -->|type of|AttackAgainstMiningPools[Attack Against Mining Pools]
NetworkRoutingAttacks -->|contributes to|EclipseAttack[EclipseAttack]
