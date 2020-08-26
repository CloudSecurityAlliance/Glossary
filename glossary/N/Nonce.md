# Nonce

is an arbitrary number used only once in a cryptographic communication,
in the spirit of a nonce word. They are often random or pseudo-random
numbers. Many nonces also include a timestamp to ensure exact timeliness,
though this requires clock synchronization between organizations. The
addition of a client nonce ("cnonce") helps to improve the security in some
ways as implemented in digest access authentication. To ensure that a nonce
is used only once, it should be time-variant (including a suitably fine-grained
timestamp in its value), or generated with enough random bits to ensure
a probabilistically insignificant chance of repeating a previously generated
value. Some authors define pseudo-randomness (or unpredictability) as a
requirement for a nonce.
Source: https://en.wikipedia.org/wiki/Cryptographic_nonce

