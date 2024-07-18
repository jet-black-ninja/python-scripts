import os
import glob
import shutil
from os import path
def dirSort(baseDir):
    filename = glob.glob(f"{baseDir}/*")

    paths={
    "Documents" : ['.pdf', '.docs', '.doc','.txt','.csv','.docx'],
    "Photos" : ['.jpeg','.png','.jpg','.svg','.PNG','.gif'],
    "Programs" : ['.exe','.msi','.bat'],
    "Compressed" : ['.zip',',7z','rar'],
    "Videos" : ['.mp4'],
    "Music" : ['.mp3']
    }
    for file in filename:
        print(file)
        ext = os.path.splitext(file)[1]
        if not len(ext):
            continue
        for k,v in paths.items():
            if  ext in v:
                if not (path.exists(f"{baseDir}/{k}")):
                    os.mkdir(f"{baseDir}/{k}")
                shutil.move(file,f"{baseDir}/{k}")
                break
            
        else:
            if not (path.exists(f"{baseDir}/Files")):
                os.mkdir(f"{baseDir}/Files")
            shutil.move(file,f"{baseDir}/Files")

if __name__ == "__main__": 
    dirSort(sys.argv)