```mermaid
graph LR
BlockchainSecurity(BlockchainSecurity)
51Attack -->|type of|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
ChainLocks -->|defense against|51Attack[51% Attack]
ChainLocks -->|defense against|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
DelayedProofofWorkdPoW -->|defense against|51Attack[51% Attack]
DelayedProofofWorkdPoW -->|defense against|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
MergedMining -->|defense against|51Attack[51% Attack]
MergedMining -->|defense against|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
PenaltySystem -->|defense against|51Attack[51% Attack]
PenaltySystem -->|defense against|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
PirlGuard -->|defense against|51Attack[51% Attack]
PirlGuard -->|defense against|AttackAgainstConsensusMechanisms[Attack Against Consensus Mechanisms]
