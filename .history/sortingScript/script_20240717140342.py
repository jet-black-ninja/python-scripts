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

DocumentLocation = f"{baseDir}/Documents"
PhotoLocation = f"{baseDir}/Photos"
SetupLocation = f"{baseDir}/Programs"
ZipLocation = f"{baseDir}/Compressed"
VideoLocation = f"{baseDir}/Video"
MusicLocation = f"{baseDir}/Music"
FilesLocation =f"{baseDir}/Files"
for file in filename :
    



