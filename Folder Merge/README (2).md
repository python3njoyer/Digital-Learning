# Combine_file_folders

This simple program can take all the files from different folders in the same directory and merge them into one folder. It will not delete the original folders or their contents. The script accounts for duplicate file names by renaming the file with a new number at the end to allow for merging into the same folder. 

I wrote the script to combine various photo folders, but the code will work for other types of files; however, this may require minor adjustments to the code if the file extension is more than three letters (e.g. jpg). In this case, you will have to update the string slicing in the second function to reflect this; for example, a four-letter file extension like 'docx' would require you to change the 4s to 5s.

Steps:
1. Make sure all the folders you want to merge are in the same directory. 
2. Edit the three variable names at the top of the script.
    - Copy the current location of the folders into the currentDir variable.
    - Find the directory where you want to create the merged folder. Copy this location into the destDir variable. 
    - Create a name for the merged folder with the destName variable.
3. Run the script.
