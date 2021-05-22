import os
#target_folder = input("----> ")
#new = (f'abayomidare@abayomidare-Latitude-3570:~/Documents/{target_folder}')

files = os.listdir(f"abayomidare@abayomidare-Latitude-3570:~/Documents/practicals")
print(files)

for number in range(20):
    numbers = files[number]
    split = numbers.split(".")
    extension = split[-1]
    # print(split)
    print(extension)