'''Define the concept of caesar cipher and write the programs for encryption and
decryption with distance +3 for the lowercase alphabet.'''
text = input("Enter a string(lowercase only): ")
encrypted_text = ""
for ch in text:
    if ch.isalpha():
        new_char = chr((ord(ch)-ord('a')+3)%26+ord('a'))
        encrypted_text += new_char
    else:
        encrypted_text += ch
print("Encrypted text: ", encrypted_text)