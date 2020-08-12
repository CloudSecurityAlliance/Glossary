```mermaid
graph TD
BlockchainAttack(BlockchainAttack)
34Attack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
51Attack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
BlockMiningTimejackAttack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
BlockMiningTimejackAttack -->|type of|AttackAgainstNode[Attack Against Node]
EclipseAttack -->|contributes to|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
NetworkRoutingAttacks -->|contributes to|EclipseAttack[EclipseAttack]
