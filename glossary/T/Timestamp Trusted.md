# Timestamp Trusted

Initially, the original data is hashed. Hashing authenticates the exact data
content, because the hash function ensures that changing a single bit in
the data would generate a different hash value. The hash is then transmitted
to a TSA, which joins the hash with a plain text timestamp. The resulting string,
i.e. the hash combined with the timestamp, is hashed once more and digitally
signed using the TSA’s private key. The resulting ciphertext represents the
trusted timestamp, which, together with the plain text timestamp, is returned
to the requester. The validity of the trusted timestamp can be verified by
decoding the ciphertext using the public key of the TSA. To verify that some data
is identical to the data authenticated by the TSA, the process of creating the
trusted timestamp has to be replicated and the results have to be compared to
the decoded trusted timestamp. The need for a central TSA is a weakness of
established time-stamping approaches, since the integrity of the time-stamping
process is inevitably bound to the integrity of the TSA (Adams et al., 2001).
Source: https://www.gipp.com/wp-content/papercite-data/pdf/gipp15a.pdf

