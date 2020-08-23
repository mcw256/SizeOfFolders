"""
Windows only!
Run this script in directory to obtain sizes of its child folders
Saves .txt file on desktop with list: <folderdirectory> <foldersize>
"""
import os

def GetHumanReadable(size,precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1 #increment the index of the suffix
        size = size/1024.0 #apply the division
    return "%.*f%s"%(precision,size,suffixes[suffixIndex])



#Create list of child folders directory and their size(initiate with 0)
SubfoldersAndTheirSize = list(map(lambda x: [os.path.join(os.getcwd(),x)] + [0],next(os.walk('.'))[1]))

#Create list of directory of files and their size
Files = []
for root,dirs,files in os.walk(os.getcwd()):
    for f in files:
        Files.append([os.path.join(root,f),os.path.getsize(os.path.join(root,f))])

#Sum up sizes
for s in SubfoldersAndTheirSize:
    for f in Files:
        if s[0] in f[0]:
            s[1] += f[1]


#Sort by size
SubfoldersAndTheirSize.sort(key=lambda x: x[1], reverse=True)


#Save txt file to desktop
TextFileName = os.path.join('C:',os.environ["HOMEPATH"], 'Desktop', str(os.path.basename(os.getcwd())) + '--SubFolderSizes.txt')
TextFile = open(TextFileName, 'a')

for s in SubfoldersAndTheirSize:
    TextFile.write(str(s[0]) + ' ' + str(GetHumanReadable(s[1])))
    TextFile.write('\r\n')
TextFile.close()

print('Done')


