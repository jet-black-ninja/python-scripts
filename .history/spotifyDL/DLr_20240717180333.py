import spotdl
import sys, os

def spotify():
    if(len(sys.argv)<= 1):
        print("try 'python3 spotify.py -h' for help")
        return 1
    elif (sys.argv[1]=='-h'):
        print("To download a song run \n python3 spotify.py $trackURL\n\n To download an album ,\n python3 spotify.py $albumURL\n\nTo ")