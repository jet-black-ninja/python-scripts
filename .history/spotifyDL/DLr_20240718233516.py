import spotdl
import sys, os
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark_blue")

root = customtkinter.CTk()
root.geometry("500x350")

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
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx = 60, fill = "both" , expand = True)

label = customtkinter.CTkLabel(master= frame, text ="Enter Link To DownLoad", text_font=("Raleway",24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master= frame, )