import uuid
import hashlib

database = {}

def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode()+password.encode()).hexdigest()+":"+salt

def check_password(old_hash, password):
    thehash, salt = old_hash.split(":")
    return thehash == hashlib.sha256(salt.encode() + password.encode()).hexdigest()

if __name__ == "__main__":
    print("enter password:", end="")
    password = input()
    old_hash = hash_password(password)
    print("re-enter the password:", end="")
    password = input()
    print("password entered %s" % ("correctly" if check_password(old_hash, password) else "incorrectly"))
