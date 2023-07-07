import os

def compare_directories(dir1, dir2):
    files_dir1 = set(os.listdir(dir1))
    files_dir2 = set(os.listdir(dir2))

    files_only_in_dir1 = files_dir1 - files_dir2
    files_only_in_dir2 = files_dir2 - files_dir1

    print("Files only in", dir1, ":\n")
    for file in files_only_in_dir1:
        print(file)

    print("\nFiles only in", dir2, ":\n")
    for file in files_only_in_dir2:
        print(file)

# Provide the directories you want to compare
directory1 = "F:\Music"
directory2 = "D:\Music"

compare_directories(directory1, directory2)