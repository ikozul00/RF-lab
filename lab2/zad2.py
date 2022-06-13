
import glob
import hashlib

BLOCK_SIZE = 65536

filenames=glob.glob('Lab2_download_1/*', recursive = True)
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
    print("SHA 256")
    print (sha256_hash.hexdigest())
    print("MD 5")
    print (md5_hash.hexdigest())
    print("SHA 1")
    print (sha1_hash.hexdigest())




