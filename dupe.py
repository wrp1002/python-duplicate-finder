from pathlib import Path
import hashlib
from collections import defaultdict
import concurrent.futures
import time


checksums_map = defaultdict(list)
photos = Path("/media/wes/smb_ssd/Photos")
prev_path = ""
start = time.time()

for item in photos.rglob("*"):
    if not item.is_file():
        continue

    with open(item, 'rb') as f: # Open the file to read it's bytes
        digest = hashlib.file_digest(f, "sha256")

    hash = digest.hexdigest()
    current_path = item.parent

    if prev_path != current_path:
        print(current_path)
        prev_path = current_path

    checksums_map[hash].append(str(item))
    if len(checksums_map[hash]) > 1:
        print("Duplicate found!")
        print(checksums_map[hash])

print("All duplicates:")

with open('duplicates.txt', 'w') as output_file:
    for key in checksums_map:
        if len(checksums_map[key]) > 1:
            print(checksums_map[key])
            print()

            for path in checksums_map[key]:
                output_file.write(path + "\n")
            output_file.write("\n")

print(f"That took {time.time() - start} sec")
print()























