import os
import glob
import shutil
from os import path

filename = glob.glob("C:/Users/Sachin/Downloads/*")

documents = ['.pdf', '.docs', '.doc','.txt','.csv']
photo = ['.jpeg','.png','.jpg','.svg','.PNG','.gif']
setupFiles = ['.exe','.msi','.bat']
zip = ['.zip',',7z','rar']
video = ['.mp4']
music = ['.mp3']

DocumentLocation = r'C:\Users\Sachin\Downloads\Documents'
PhotoLocation = r'C:\Users\Sachin\Downloads\Photos'
SetupLocation = r'C:\Users\Sachin\Downloads\Programs'
ZipLocation = r'C:\Users\Sachin\Downloads\Compressed'
VideoLocation = r'C:\Users\Sachin\Downloads\Video'
MusicLocation = r'C:\Users\Sachin\Downloads\Music'
FilesLocation =r'C:\Users\Sachin\Downloads'
if file in filename :
    if os.path.splittext(file)[1] in documents:
        if(path.exists(DocumentLocation)):
            shutil.move(file,DocumentLocation)
        else:
            os.mkdir(DocumentLocation)
            shutil.move(file,DocumentLocation)
    if os.path.splittext(file)[1] in photo
        if(path.exists(PhotoLocation))
            shutil.move
