import libfcrypt

# We need a key to encrypt and decrypt data
key = libfcrypt.base.gen_key()

# Define a string we want to encrypt
my_string = "I have many secrets!"

# We use the basic encrypts function, and supply it a key and a string
my_encypted_string = libfcrypt.base.encrypts(key,my_string)

# We then use the decrypt function with the same key to undo the encryption
my_decrypted_string = libfcrypt.base.decrypts(key,my_encypted_string)
