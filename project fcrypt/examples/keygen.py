import libfcrypt

# Generate a new key with the basic gen_key function.
key = libfcrypt.base.gen_key()

# Generate a new key with a password.
other_key = libfcrypt.base.passwd_gen_key("Password1234")
