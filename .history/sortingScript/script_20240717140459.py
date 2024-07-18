import os
import glob
import shutil
from os import path
baseDir="C:/Users/Sachin/Downloads"
filename = glob.glob(f"{baseDir}*")

Documents = ['.pdf', '.docs', '.doc','.txt','.csv']
Photos = ['.jpeg','.png','.jpg','.svg','.PNG','.gif']
Programs = ['.exe','.msi','.bat']
Compressed = ['.zip',',7z','rar']
video = ['.mp4']
music = ['.mp3']

DocumentLocation = f"{baseDir}/Documents"
PhotoLocation = f"{baseDir}/Photos"
SetupLocation = f"{baseDir}/Programs"
ZipLocation = f"{baseDir}/Compressed"
VideoLocation = f"{baseDir}/Video"
MusicLocation = f"{baseDir}/Music"
FilesLocation =f"{baseDir}/Files"
for file in filename :
    if os.path.splittext(file)[1] in documents:
        if(path.exists(DocumentLocation)):
            shutil.move(file,DocumentLocation)
        else:
            os.mkdir(DocumentLocation)
            shutil.move(file,DocumentLocation)
   



