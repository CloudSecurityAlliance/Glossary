# Schnorr Signatures

is a signature algorithm replacement for ECDSA, leveraging elliptic curve
cryptography that supports "native multisig" which enables the aggregation
of multiple signatures into a single one valid for the sum of the keys of their
respective inputs. This algorithm has 3 significant benefits:

* Constant-size signatures irrespective of the number of participants in the multisig setup.
* Diminished size of data to be validated and transmitted translates into capacity gains.
* Entire policy of multisig is obscured and indistinguishable from a conventional single pubkey.

Source: https://bitcoincore.org/en/2017/03/23/schnorr-signatureaggregation/

