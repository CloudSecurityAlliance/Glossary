# Script

is a simple programming language, which is evaluated from left to right
using a stack. The language is designed such that it guarantees all scripts will
execute in a limited amount of time (it is not Turing-Complete).
A script is essentially a list of instructions recorded with each transaction
that describe how the next person wanting to spend the Bitcoins being
transferred can gain access to them. The script for a typical Bitcoin transfer
to destination Bitcoin address D simply encumbers future spending of the
bitcoins with two things: the spender must provide:
1. a public key that, when hashed, yields destination address D embedded
in the script, and
2. a signature to show evidence of the private key corresponding to the
public key just provided.
Source: https://bitcore.io/api/lib/script and https://en.bitcoin.it/wiki/Script

