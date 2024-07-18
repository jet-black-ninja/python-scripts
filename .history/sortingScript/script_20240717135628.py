import os
import glob
import shutil
from os import path
baseDir="C:/Users/Sachin/Downloads"
filename = glob.glob(f"{baseDir}*")

documents = ['.pdf', '.docs', '.doc','.txt','.csv']
photo = ['.jpeg','.png','.jpg','.svg','.PNG','.gif']
setupFiles = ['.exe','.msi','.bat']
zip = ['.zip',',7z','rar']
video = ['.mp4']
music = ['.mp3']

DocumentLocation = f{"{bases}"}
PhotoLocation = 
SetupLocation = 
ZipLocation = 
VideoLocation = 
MusicLocation = 
FilesLocation =
for file in filename :
    if os.path.splittext(file)[1] in documents:
        if(path.exists(DocumentLocation)):
            shutil.move(file,DocumentLocation)
        else:
            os.mkdir(DocumentLocation)
            shutil.move(file,DocumentLocation)
    if os.path.splittext(file)[1] in photo:
        if(path.exists(PhotoLocation)):
            shutil.move




