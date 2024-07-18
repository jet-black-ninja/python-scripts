import spotdl
import sys, os
import PySimpleGUI as song

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
            name = input("Enter Playlist Name")
            os.system(f'spotdl --output "{name}/{{track-number}} - {{title}}.{{output-ext}}" {url}')
        if(url.find("album")> -1):
            print("album")
            os.system(f'spotdl --output "{{artist}}/{{album}}/{{track-number}} - {{title}}.{{output-ext}}" "{url}"')
            
if __name__== "__main__":
    spotify()
    
    