import subprocess
import os
import glob
dir_to_check_1 = "/media/tvvoty/NewVolume11/AfterLinuxGotDeleted/From desctop to make space in C b/Music files b/"
dir_to_check_2 = "/home/tvvoty/Secondary/Backup/0Music/"

def get_list_of_files_and_folders(dir_to_check):
    list_of_files = []
    list_of_dirs = []
    for root_path, dirs, files in os.walk(dir_to_check):
        for file in files:
            file_path = os.path.join(root_path, file)
            list_of_files.append(file_path)
        for dir in dirs:
            dir_path = os.path.join(root_path, dir)
            list_of_dirs.append([dir_path, dir])
    return list_of_files, list_of_dirs


def get_list_of_checksums(list_of_files):
    list_of_checksums = []
    for file_path in list_of_files:
        file = file_path
        p1 = subprocess.run(['md5sum', f"{file}"], capture_output=True,  text=True)
        print(p1.stdout)
        sum_of_file, path = p1.stdout.split("  ", maxsplit=1)
        list_of_checksums.append([sum_of_file, path[0:-1]])
    return list_of_checksums

list_of_files_1, list_of_dirs_1 = get_list_of_files_and_folders(dir_to_check_1)
list_of_files_2, list_of_dirs_2 = get_list_of_files_and_folders(dir_to_check_2)
list_of_checksums_1 = get_list_of_checksums(list_of_files_1)
list_of_checksums_2 = get_list_of_checksums(list_of_files_2)


identical_file_list = []
for sum1, path1 in list_of_checksums_1:
    for sum2, path2 in list_of_checksums_2:
        if sum1 == sum2:
            identical_file_list.append([path1, path2])

identical_dir_list = []
for dir_path1, dir_name1 in list_of_dirs_1:
    for dir_path2, dir_name2 in list_of_dirs_2:
        if dir_name1 == dir_name2:
            identical_dir_list.append([dir_name1, dir_path1, dir_path2])

with open(f"results.txt", mode='w', encoding='utf-8') as f:
    f.write(f"Dirs\n\n\n\n\n\n")
    for entry in identical_dir_list:
        print(f"Directory:{entry[0]}\n Is present in:\n {entry[1]}\n and in:\n{entry[2]}\n\n")
        f.write(f"{entry[0]}:\n\n{entry[1]}\n\n{entry[2]}\n\n\n\n")

    f.write(f"Files\n\n\n\n\n\n")
    for entry in identical_file_list:
        print(f"Files:{entry[0]}\n and\n {entry[1]}\n are identical\n\n\n")
        f.write(f"{entry[0]}\n\n{entry[1]}\n\n\n\n")

#d = os.walk(dir_to_check_2)
#for a,b,c in d:
    #print(f"Path : {a}")
    #print(f"Dir : {b}")
    #print(f"File : {c}")
