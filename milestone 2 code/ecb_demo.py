from des import des_encrypt_block

STATIC_KEY = b"8bytekey"
block = b"BANK0001"  # one 8-byte DES block, encrypted twice

ct_block1 = des_encrypt_block(block, STATIC_KEY)
ct_block2 = des_encrypt_block(block, STATIC_KEY)

print("Key (hex)            :", STATIC_KEY.hex())
print("Plaintext block 1    :", block, "->", block.hex())
print("Plaintext block 2    :", block, "->", block.hex())
print("-" * 55)
print("Ciphertext block 1   :", ct_block1.hex())
print("Ciphertext block 2   :", ct_block2.hex())
print("-" * 55)
print("Blocks identical?    :", ct_block1 == ct_block2)  # ECB leaks: same in -> same out
print()
if ct_block1 == ct_block2:
    print(">>> ECB WEAKNESS CONFIRMED: identical plaintext blocks")
    print(">>> produced identical ciphertext blocks. The pattern leaks.")
