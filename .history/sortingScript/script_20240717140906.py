import os
import glob
import shutil
from os import path
baseDir="C:/Users/Sachin/Downloads"
filename = glob.glob(f"{baseDir}*")

paths={
"Documents" : ['.pdf', '.docs', '.doc','.txt','.csv'],
"Photos" : ['.jpeg','.png','.jpg','.svg','.PNG','.gif'],
"Programs" : ['.exe','.msi','.bat'],
"Compressed" : ['.zip',',7z','rar'],
"Videos" : ['.mp4'],
"Music" : ['.mp3']
}
for file in filename:
    for k,v in paths.items(:)
        

# for file in filename :
#     if os.path.splittext(file)[1] in documents:
#         if(path.exists(DocumentLocation)):
#             shutil.move(file,DocumentLocation)
#         else:
#             os.mkdir(DocumentLocation)
#             shutil.move(file,DocumentLocation)
   



