import subprocess
import os
import re
#file = "/media/tvvoty/NewVolume11/Backup/LinuxBackup/Appimages/tor-browser_en-US/Browser/.config/ibus/bus"
#p1 = subprocess.run(['md5sum', f"{file}"], capture_output=True,  text=True)
#print(p1.stdout)
#sum_of_file, path = p1.stdout.split("  ", maxsplit=1)
#print(f"{sum_of_file} and {path}")




pattern = re.compile(r"/[^\n]*\n*[^\n]*")
file = "results.txt"
list_of_files = []
with open(file, mode='r', encoding='utf-8') as f:
    contents = f.read()
    #print(contents)
    matches = pattern.findall(contents)
    #print(matches)
    for entry in matches:
        file_1, file_2 = entry.split("\n\n")
        list_of_files.append([file_1, file_2])

#print(list_of_files)
#for entry in list_of_files:
    #print(f"{entry[0]}\n\n{entry[1]}\n\n")

size_of_identicals_1 = 0
size_of_identicals_2 = 0



for entry in list_of_files:
    try:
        size_of_one_file1 = os.path.getsize(entry[0])
        size_of_one_file2 = os.path.getsize(entry[1])
        size_of_identicals_1 += size_of_one_file1
        size_of_identicals_2 += size_of_one_file2
    except Exception as e:
        print(e)

print(size_of_identicals_1)
print(size_of_identicals_2)
