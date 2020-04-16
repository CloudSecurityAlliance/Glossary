# Bitcoin Transaction Locktime

The Bitcoin transaction lock time is the time at which a particular transaction
can be added to the blockchain. This is the earliest time that miners can
include the transaction in their hashing of the Merkle root to attach it in the
latest block to the blockchain.There are two specific types of transaction
locktime. Firstly when the locktime figure is less than 500 million it is
interpreted as a block height and miners therefore have to wait until that block
height has been reached before attempting to include it in a block. If it is above
500 million it is converted to a unix timestamp – a unix timestamp being the
number of seconds since January 1st 1970.
Source: https://www.cryptocompare.com/coins/guides/what-is-bitcointransaction-locktime/

