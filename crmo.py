import crcmod
import os

# Create CRC32 hash function
crc32_func = crcmod.predefined.mkCrcFun('crc-32')

maya = ['IFNet_HDv3.py', 'refine.py', 'RIFE_HDv3.py']
# Calculate CRC32 value of a file
for filename in maya:
    file_path = './arch/' + filename
    with open(file_path, 'rb') as file:
        file_contents = file.read()
        crc32_value = crc32_func(file_contents)
    size_in_bytes = os.path.getsize(file_path)
    print('"filename:"', filename)
    print('"dir": "\\arch"')
    print('"size:"', size_in_bytes)
    # Print the CRC32 value in decimal format
    print('"crc32:"', crc32_value)
