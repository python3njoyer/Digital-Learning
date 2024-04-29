import os
import shutil

currentDir = r''  # insert current location of folders
destDir = r''  # insert directory to create the new folder in
destName ='Images'  # insert name for the new folder


currentDir = currentDir.replace('\\', '/') + '/'
destFolder = os.path.join((destDir.replace('\\', '/') + '/'), destName)
duplicates = {}

# Creates a new folder for images if one doesn't already exist. Then iterates through each image in each
# folder in the original directory and copies the image to the new folder. Images with duplicate file names
# are skipped and saved to a dictionary.
def merge(mergeFolder, origDir):
    if not os.path.exists(mergeFolder):
        os.makedirs(mergeFolder)
    for folder in os.listdir(origDir):
        print('Merging folder...', folder)
        for image in os.listdir(origDir + folder):
            if (os.path.exists(mergeFolder + '/' + image)):
                if image in duplicates:
                    duplicates[image].append(origDir + folder + '/' + image)
                else:
                    duplicates[image] = [origDir + folder + '/' + image]
            else:
                shutil.copy2(origDir + folder + '/' + image, mergeFolder)  # this method preserves img metadata
    print('Merge Successful')


# Iterates through images in duplicates dict and renames each file with an additional number (1 to n) at
# the end.
def file_rename(dict):
    for key in dict:
        i = 1
        for image in dict[key]:
            print('Renaming file:', image)
            os.rename(image, image[:len(image)-4] + '(' + str(i) + ')' + image[-4:])
            i += 1


merge(destFolder,currentDir)
file_rename(duplicates)
merge(destFolder,currentDir)