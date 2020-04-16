# Timestamp Blockchain

Cryptocurrencies can serve as decentralized trusted time-stamping services
if hash values of digital data are embedded into the transactions recorded
in the block chain of the crypto currency. When a user submits a file or
plain text through the browser, a client-side Javascript hashes the data.
Alternatively, the data can be hashed offline, e.g., using an open source
tool. In either case, only the hash, not the data is transmitted to the server.
Then a bitcoin transaction, using the smallest amount possible, is created
that includes the document hash. By processing the transaction, the hash
and the timestamp of the transaction are permanently embedded in the
distributed Bitcoin block chain. The timestamp of confirmed transactions and
the data they encode can be verified by inspecting the Bitcoin block chain,
e.g. using websites like blockchain.info.
Source: https://www.gipp.com/wp-content/papercite-data/pdf/gipp15a.pdf
and https://app.originstamp.org/home

