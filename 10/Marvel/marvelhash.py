import hashlib
import time

# Your private and public keys
ts = str(int(time.time()))  # This should be a unique string (e.g., current timestamp)
private_key = "1626e651794c68d64ffa5d14b36eb7286a18645d"
public_key = "74b43c84091b507498b9e6cbb7fc900f"

# Create the hash (MD5 of ts + private_key + public_key)
hash_string = ts + private_key + public_key
hash_result = hashlib.md5(hash_string.encode()).hexdigest()

# Print the result
print("Timestamp:", ts)
print("MD5 Hash:", hash_result)
