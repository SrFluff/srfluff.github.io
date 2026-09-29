import libfcrypt

# Generate a new key
key = libfcrypt.base.key_gen()

# Read an unencrypted file
f = open("secrets.txt","r")

# Encrypt the data in the file with a supplied key
data = libfcrypt.file.encryptf(key,f)

# Close the file
f.close()

# Write the encrypted data to a new file
f = open("encrypted_secrets.txt","wb")
f.write(data)
f.close()

# Open the encrypted file
f = open("encrypted_secrets.txt","rb")

# Decrypt the contents of the file with a supplied key
decrypted_data = libfcrypt.file.decryptf(key,f)

# Close the file
f.close()
