import zipfile, os, py7zr

#This program requires the installation of py7zr. Install it with Pip! https://pypi.org/project/py7zr/

root_directory = os.path.dirname(os.path.abspath(__file__))
print("Do you want to name your unzipped folder something specific? \nThe default is called 'Unzipped Files' Y or N")
Rename = input()
if Rename=="Y":
    print("Please enter the name now:")
    folderName = input()
else:
    folderName = "Unzipped Files"

unzipped = os.path.join(root_directory, folderName)
if not os.path.exists(unzipped):
    os.mkdir(unzipped)

print("Searching for zipped files...\n\nDo you want to:\n1: Unzip all files in this directory? Or \n2: Just the ones that haven't been unzipped yet?\n\nPlease select the option 1 or 2.")

Option = input()
zip_file_path = root_directory
zipfilefinaldir = os.path.join(root_directory + os.sep + folderName)
file_list = os.listdir(root_directory)
abs_path = []
for a in file_list:
    x = zip_file_path+'\\'+a
    abs_path.append(x)
print(abs_path)
if Option == "1":    
    for f in abs_path:
        if f.endswith(".zip"):
            print(f + " found. Unzipping...")
            zip=zipfile.ZipFile(f)
            zip.extractall(zipfilefinaldir)
        elif f.endswith(".7z"):
            print(f+ "found. Unzipping...")
            with py7zr.SevenZipFile(f, mode='r') as z:
                z.extractall(zipfilefinaldir)
if Option == "2":
    for f in abs_path:
        if f.endswith(".zip") and not os.path.exists(f.rstrip(".zip")):
            print(f + " found. Unzipping...")
            zip=zipfile.ZipFile(f)
            zip.extractall(zipfilefinaldir)
        elif f.endswith(".7z") and not os.path.exists(f.rstrip(".7z")):
            print(f+ "found. Unzipping...")
            with py7zr.SevenZipFile(f, mode='r') as z:
                z.extractall(zipfilefinaldir)
    

print("Zip files successfully extracted to " + unzipped)
