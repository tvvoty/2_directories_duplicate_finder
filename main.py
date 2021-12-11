import subprocess
import os
import glob
dir_to_check_1 = "/home/tvvoty/Secondary/AfterLinuxGotDeleted/AfterPCBrokeFromOldDisk/MultiMed/EmuPlace/"
dir_to_check_2 = "/home/tvvoty/Secondary/Backup/EmuPlace/"
#dir_to_check_1 = "/media/tvvoty/NewVolume11/Backup/LinuxBackup/Appimages/tor-browser_en-US/Browser/.config/"
#dir_to_check_2 = "/home/tvvoty/Secondary/Backup/LinuxBackup/Appimages/tor-browser_en-US/Browser/.config/"

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
    error_list = []
    for file_path in list_of_files:
        print(f"The file path is:\n{file_path}\n\n")
        p1 = subprocess.run(['md5sum', f"{file_path}"], capture_output=True,  text=True)
        print(f"The stdout is:\n{p1.stdout}\n\n")
        try:
            sum_of_file, path = p1.stdout.split("  ", maxsplit=1)
            list_of_checksums.append([sum_of_file, path[0:-1]])
        except Exception as e:
            error_list.append([file_path, e])
            print(e)

    return list_of_checksums, error_list

list_of_files_1, list_of_dirs_1 = get_list_of_files_and_folders(dir_to_check_1)
list_of_files_2, list_of_dirs_2 = get_list_of_files_and_folders(dir_to_check_2)
list_of_checksums_1, error_list1 = get_list_of_checksums(list_of_files_1)
list_of_checksums_2, error_list2 = get_list_of_checksums(list_of_files_2)


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


size_of_identicals_1 = 0
size_of_identicals_2 = 0
for entry in identical_file_list:
    try:
        size_of_one_file1 = os.path.getsize(entry[0])
        size_of_one_file2 = os.path.getsize(entry[1])
        size_of_identicals_1 += size_of_one_file1
        size_of_identicals_2 += size_of_one_file2
    except Exception as e:
        print(e)


print(size_of_identicals_1)
print(size_of_identicals_2)


with open(f"results.txt", mode='w', encoding='utf-8') as f:
    f.write(f"size_of_identicals_1 = {str(size_of_identicals_1)}\n\n")
    f.write(f"size_of_identicals_2 = {str(size_of_identicals_2)}\n\n")
    f.write(f"Dirs\n\n\n\n\n\n")
    for entry in identical_dir_list:
        print(f"Directory:{entry[0]}\n Is present in:\n {entry[1]}\n and in:\n{entry[2]}\n\n")
        f.write(f"{entry[0]}:\n\n{entry[1]}\n\n{entry[2]}\n\n\n\n")

    f.write(f"Files\n\n\n\n\n\n")
    for entry in identical_file_list:
        print(f"Files:{entry[0]}\n and\n {entry[1]}\n are identical\n\n\n")
        f.write(f"{entry[0]}\n\n{entry[1]}\n\n\n\n")

    f.write(f"Errors\n\n")
    f.write(f"The following files could not be processed, most probably they are simlinks:\n\n\n\n\n\n")
    for entry in error_list1:
        print(f"File:{entry[0]}\n\n Error:\n\n {entry[1]}\n\n\n")
        f.write(f"{entry[0]}\n\n{entry[1]}\n\n\n\n")
    for entry in error_list2:
        print(f"File:{entry[0]}\n\n Error:\n\n {entry[1]}\n\n\n")
        f.write(f"{entry[0]}\n\n{entry[1]}\n\n\n\n")



#d = os.walk(dir_to_check_2)
#for a,b,c in d:
    #print(f"Path : {a}")
    #print(f"Dir : {b}")
    #print(f"File : {c}")
