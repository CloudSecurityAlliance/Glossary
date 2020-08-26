# Merkle Tree

Basic idea behind Merkle tree is to have some piece of data that is linking
to another. You can do this by linking things together with a cryptographic
hash. The content itself can be used to determine the hash. By using the
cryptographic hashing, we can address the content, and content gets
immutable because if you change anything in the data the cryptographic
hash changes and the link will be different. Bitcoin uses cryptographic
hashing, where every block points to the previous one, if you modify the
block, the hash will change and will make the block invalid.
Source: https://blockchainhub.net/glossary/

