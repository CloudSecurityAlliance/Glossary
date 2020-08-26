# Bitcoin 0.9 Standard Transaction Types

As of bitcoin core 0.9, transactions from the network must match a set of
rules, Those transactions are called standard transactions. Only standard
transactions are mined or broadcast by peers running the default Bitcoin
Core software. The standard transaction types are as follows:
1. Pay to PubKey Hash (P2PKH) - standard way to send Bitcoins to a single
address
2. Pay to Address - standard way of assigning newly mined Bitcoins and
transaction fees to an address
3. Pay to Script Hash (P2SH) - moves the responsibility for supplying the
conditions to redeem a transaction from the creator of the transaction
to the payee(s)
4. Multi-Signature - used for multi-signature transactions by specifying the
multi-signature script in the P2SH (#3) redeemScript, they can also be
specified directly in the scriptPubKey
5. Null_Data - They allow the creator of the transaction to include some
arbitrary data in the blockchain in exchange for paying a transaction fee.
The output is unspendable
6. Non_Standard – None of the above
Source: http://www.quantabytes.com/articles/a-survey-of-bitcoin-transactiontypes and https://bitcoin.org/en/developer-guide#standard-transaction

