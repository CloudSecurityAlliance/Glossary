# Decentralized Acyclic Graph (DAG)

A Decentralized Acyclic Graph (DAG) is a graph (a collections of nodes and edges) that does not have any cycles, or in simple terms no node is connected to other nodes in a way that forms loops. Please note that in a blockchain style data structure a DAG may have nodes that are connected to each other via edges, but these edges have a direction (e.g. the newer block has a hash of the older block, of course an older block cannot have a hash of a non existent "newer" block) so there may be a situation where A is connect to B and C, and B is connected to C but data can only travel from A to B and C, and from B to C, the data cannot loop around (e.g. from C to A).

DAG based systems are sometimes referred to as "tangle" chains as they often have interwoven structures like ivy or related plants.
## Tags

Category:BlockchainArchitecture
Graph:DecentralizedAcyclicGraph -->|is a type of data structure for a|Blockchain[Blockchain]
