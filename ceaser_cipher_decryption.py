text = input('Enter the decryption text: ')
encrypted_text=""
for ch in text:
    if ch>='a' and ch<='z':
        new_char = chr((ord(ch) - ord('a') - 3) % 26 + ord('a'))
        encrypted_text += new_char
    else:
        encrypted_text += ch


print("Encrypted text: ", encrypted_text)