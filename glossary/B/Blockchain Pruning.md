# Blockchain Pruning

It is not required for most fully validating nodes to store the entire blockchain,
currently around 127 GB. Reducing the amount of data to the size of the
current unspent output size, currently 1.7 GB, plus some additional for data
that is needed to handle re-orgs can reduce the stress on many nodes.
Source: https://en.bitcoin.it/wiki/Scalability and https://statoshi.info/dashboard/db/unspent-transaction-output-set

