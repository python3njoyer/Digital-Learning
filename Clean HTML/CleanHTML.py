import re
import os


def remove_styling(text):
    text = re.sub('.style=".*?"', '', text)
    text = re.sub('<span.*?>', '', text)
    text = re.sub('</span>', '', text)
    text = re.sub('&nbsp;', '', text)
    text_styling = ['<u></u>', '<b></b>']
    for i in text_styling:
        text = re.sub(i, '', text)
    text = re.sub('<p></p>\n', '', text)
    return text


# Makes sure directory path has a forward slash at the end
origDir = r'C:\Users\eliza\PycharmProjects\ODL\orig'.replace('\\', '/').rstrip('/') + '/'
buildDir = r'C:\Users\eliza\PycharmProjects\ODL\build'.replace('\\', '/').rstrip('/') + '/'

# For loop iterates through each file in origDir. File is the file name, not complete filepath
for file in os.listdir(origDir):
    # Print statement just because
    print('Processing file', origDir + file)

    # Open original file as a read file
    with open(origDir + file, 'r') as readfile:
        # Remove stylings
        data = remove_styling(readfile.read())

        # Open new file of same name in different directory as a write file
        with open(buildDir + file, 'w') as writefile:
            # Writes cleaned data
            writefile.write(data)
            