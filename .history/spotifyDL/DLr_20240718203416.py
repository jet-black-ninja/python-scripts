import spotdl
import sys, os

def spotify():
    if(len(sys.argv)<= 1):
        print("try 'python3 spotify.py -h' for help")
        return 1
    elif (sys.argv[1]=='-h'):
        print("To download a song run \n python3 spotify.py $trackURL\n\n To download an album ,\n python3 spotify.py $albumURL\n\nTo download a playlist run,\n   python3 spotify.py $playlistUrl")
        return 1
    url = sys.argv[1]
    if(url.find('track')> -1):
        os.system(f'spotdl save download {url}')
    else: 
        #playlist 
        if(url.find('playlist') > -1):
            print("playlist")
            # os.system(f"spotdl -p {url} --write-to playlist.txt")
            # os.system(f"spotdl --list playlist.txt")
        #artist
        if(url.find("artist")> -1):
            print("artist")
            # os.system(f"spotdl -all {url} --write-to artist.txt")
            # os.system(f"spotdl --list artist.txt")
        if(url.find("album")> -1):
            print("album")
            os.mkdir(f"")
            os.system(f"spotdl --output \"{artist}/{album/}/{track-number} - {title}.{output-ext}" ")
            
if __name__== "__main__":
    spotify()