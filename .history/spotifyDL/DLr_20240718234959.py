import spotdl
import sys, os
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x450")

def spotify():
    url = entry1
    
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
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=200, padx = 60, fill = "both" , expand = True)

label = customtkinter.CTkLabel(master=frame, text ="Enter Link To DownLoad")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master= frame, placeholder_text="Spotify Link")
entry1.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Download",command = spotify)
button.pack(pady= 12, padx =10 )
root.mainloop()