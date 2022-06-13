import glob
import hashlib

BLOCK_SIZE = 65536

filenames=glob.glob('files/test.*', recursive = True)
for filename in filenames:
    print("---------"+filename+"--------")
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()
    sha1_hash=hashlib.sha1()
    with open(filename, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            sha1_hash.update(fb)
            sha256_hash.update(fb)
            md5_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    print("MD 5")
    print (md5_hash.hexdigest())
    print("SHA 1")
    print (sha1_hash.hexdigest())



print("-----------------------------------------------")
filenames=glob.glob('Dokaz/*', recursive = True)
for filename in filenames:
    sha1_hash=hashlib.sha1()
    with open(filename, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            sha1_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    if sha1_hash.hexdigest()=="c15e32d27635f248c1c8b66bb012850e5b342119":
        print(f"\nFound: {filename}")
        print (sha1_hash.hexdigest())
        print("c15e32d27635f248c1c8b66bb012850e5b342119")
