#!/usr/bin/env python3

# Solution for Repeating XOR

def xor(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Encrypted data
encrypted_hex = "1f0e0e17001e1b050303091c1f11110900111f1c1f0e09000c0d1b1a1f191b191c000e0d001a1c0e1a1b08070c0e191f080301"
encrypted = bytes.fromhex(encrypted_hex)

# Try to find the key using known plaintext
# We know it contains "CTF{" which is 0x435446

def find_xor_key(ciphertext, known_plaintext):
    keys = []
    kp = known_plaintext.encode()
    
    for i in range(len(ciphertext) - len(kp) + 1):
        potential_key_chars = []
        for j in range(len(kp)):
            key_char = ciphertext[i + j] ^ kp[j]
            potential_key_chars.append(key_char)
        
        # Check if all key chars are consistent (repeating)
        key_len = 6  # We know key is "SECRET" (6 chars)
        is_valid = True
        for j in range(len(kp)):
            expected_key_pos = j % key_len
            if j < key_len and (i + j < key_len):
                continue
        
        potential_key = bytes(potential_key_chars[:key_len])
        decrypted = xor(ciphertext, potential_key)
        if b"CTF{" in decrypted:
            return potential_key, decrypted
    
    return None, None

key, decrypted = find_xor_key(encrypted, "CTF{")
print(f"Key: {key}")
print(f"Decrypted: {decrypted.decode('utf-8', errors='ignore')}")
