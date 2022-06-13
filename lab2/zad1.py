import magic
import glob

BLOCK_SIZE = 65536
# print("1. file:")
# print(magic.from_file("Lab2_download_1/file1"))
# print(magic.from_buffer(open("Lab2_download_1/file1", "rb").read(2048)))
# print("2. file:")
# print(magic.from_file("Lab2_download_1/file2.txt"))
# print(magic.from_buffer(open("Lab2_download_1/file2.txt", "rb").read(2048)))
# print("3. file:")
# print(magic.from_file("Lab2_download_1/file3"))
# print(magic.from_buffer(open("Lab2_download_1/file3", "rb").read(2048)))

filenames=glob.glob('Lab2_download_1/*', recursive = True)
for filename in filenames:
    print(filename)
    print(magic.from_file(filename))




