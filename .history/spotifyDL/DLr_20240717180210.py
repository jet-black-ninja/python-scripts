import spotdl
import sys, os

def spotify():
    if(len(sys.argv)<= 1):
        print("try 'python3 spotify.py -h' for help")
        return 1
    elif (sys.argv[1]=='-h'):
        print("To download a song run \n ")