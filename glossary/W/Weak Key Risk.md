# Weak Key Risk

is the risk that the Key generation method used is faulty allowing the
attacker to duplicate the key gaining access to the objective (wallet, etc.).
For example a poor random number generator (RNG) can create the same
‘random’ number on more than one occasion. When the transaction is
hashed, this number is multiplied by the same generator point (ie: same
random number) as the public key. Since one unknown has been removed
from the equation, the private key can be revealed by effectively reversing
the hash through additional mathematical operations.

Source: https://www.enisa.europa.eu/publications/blockchain-security and
http://www.coindesk.com/open-source-tool-identifies-weak-bitcoin-walletsignatures/

