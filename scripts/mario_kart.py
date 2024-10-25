import hashlib
"""why would luigi give this file to mario?,
   does it have something to do with password of the zip file?
    or is it just a random file?
"""
def sha1_hash(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()

if __name__ == "__main__":
    text = input("Enter the text to hash: ")
    print(f"SHA1 hash of '{text}' is: {sha1_hash(text)}")
    