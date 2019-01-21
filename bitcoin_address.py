## Convert private key to Base58Check address
import os

## generate private key
# 32 random bytes
private_key = os.urandom(32)

# do in loop to validate key is positive and below N
print(f"private key: {private_key.hex()}")

# convert private key to WIF

# Add 01 byte at the end

# Generate WIF from compressed private key

# Multiple generator point G with private key to get public key point
# This produces x and y

# Encode as hex with prefix 04 (non compresssed)
# Print uncompressed public key as address

# Compress public. Either use 02 of even Y or 03 for odd Y.

# Generate bitcoin address from compressed public key. Use 0x00 version prefix for normal p2pkh. Or 0x05 for p2sh.


## convert to public key
