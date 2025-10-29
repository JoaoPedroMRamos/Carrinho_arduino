#Code by João Pedro Muniz Ramos, student of Mechanical Engineering at Ilha Solteira UNESP (FEIS)

#Python Docs (Python 3.13): https://docs.python.org/3.13/


from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import  ImageTk, Image
import keyboard
import serial


arduino=serial.Serial(port='COM2', baudrate=9600, timeout=1)

#background colours variables declared
#Variable must be a string containing the desired colour hexcode with # before the code
buttons_background='#d2d2d2'
selected_buttons_background='#fbd300'
background_themes=['#5cc4b4','#0a0a16'] #light_theme_background='#5cc4b4' ; #dark_theme_background='#0a0a16'
unesp_logo_bg_theme=['#316c63','#25254a']

#Delay time options for the config (seconds)
delay_options= [1.0, 1.25, 1.5, 1.75, 2.0]

config_index=[0,0]

#Building the Settings with OOP (Object Oriented Programing); 
class Settings:
    def __init__(self, theme_index=1, delay_index=2):
        self.themes= background_themes
        self.delays= delay_options
        self.theme= self.themes[theme_index]
        self.delay= self.delays[delay_index]

#Default settings (Dark Theme ; 1.5 seconds Delay)
settings=Settings(theme_index=1,delay_index=2)


#Function to get config itens index
def Settings_Index():
    for i in range (len(background_themes)):
        if settings.theme==background_themes[i]:
            config_index[0]=i

Settings_Index()
#Main U.I. geometry structure; 
main = Tk()
main.title("Carrinho")
main.geometry("1280x980")
main.configure(background=settings.theme)
main.resizable(width=False, height=False)


#Visual style theme
#Lista de themes https://tkdocs.com/tutorial/styles.html
style=Style(main)
style.theme_use("clam")

#Creating image variables with PIL

logo_unesp_lighttheme= Image.open('Logo_Unesp_preto.png')            #Opens the image from the main code folder
logo_unesp_lighttheme=logo_unesp_lighttheme.resize((227,73))         #Reshapes the image to the desired dimensions(first nuber width, second number height)
imgTk_logo_unesp_lighttheme=ImageTk.PhotoImage(logo_unesp_lighttheme)  #ImageTk.PhotoImage converts the image variable to a format compatible with Tkinter


#Main menu image
main_menu_image=Image.open('Mercedes_F1_W06.png')
main_menu_image=main_menu_image.resize((550,430))
imgTk_main_menu=ImageTk.PhotoImage(main_menu_image)

#Main menu Buttons
play_button_image=Image.open('play_button.png')
play_button_image=play_button_image.resize((300,300))
imgTk_play_button=ImageTk.PhotoImage(play_button_image)

config_button_image=Image.open('config_button.png')
config_button_image=config_button_image.resize((300,300))
imgTk_config_button=ImageTk.PhotoImage(config_button_image)

exit_button_image=Image.open('exit_button.png')
exit_button_image=exit_button_image.resize((300,300))
imgTk_exit_button=ImageTk.PhotoImage(exit_button_image)


#Play Tab Directions Buttons
up_button_image=Image.open('up.png')
up_button_image=up_button_image.resize((250,250))
imgTK_up_button=ImageTk.PhotoImage(up_button_image)

down_button_image=Image.open('down.png')
down_button_image=down_button_image.resize((250,250))
imgTK_down_button=ImageTk.PhotoImage(down_button_image)

right_button_image=Image.open('right.png')
right_button_image=right_button_image.resize((250,250))
imgTK_right_button=ImageTk.PhotoImage(right_button_image)

left_button_image=Image.open('left.png')
left_button_image=left_button_image.resize((250,250))
imgTK_left_button=ImageTk.PhotoImage(left_button_image)

#working with lists to make the declaring easier
opcoes_delays_img=['1s_button.png','125s_button.png','15s_button.png','175s_button.png','2s_button.png']
delay_button_image=[0,0,0,0,0]
imgTK_delay_button=[0,0,0,0,0]
for i in range(len(opcoes_delays_img)):
    delay_button_image[i]=Image.open(opcoes_delays_img[i])
    delay_button_image[i]=delay_button_image[i].resize((150,150))
    imgTK_delay_button[i]=ImageTk.PhotoImage(delay_button_image[i])

lighttheme_image=Image.open('lighttheme_button.png')
lighttheme_image=lighttheme_image.resize((150,150))
imgTK_lighttheme=ImageTk.PhotoImage(lighttheme_image)

darktheme_image=Image.open('darktheme_button.png')
darktheme_image=darktheme_image.resize((150,150))
imgTK_darktheme=ImageTk.PhotoImage(darktheme_image)

config_light_texto_image=Image.open('config_light_texto.png')
config_light_texto_image=config_light_texto_image.resize((1280,250))
imgTK_config_light=ImageTk.PhotoImage(config_light_texto_image)

config_dark_texto_image=Image.open('config_dark_texto.png')
config_dark_texto_image=config_dark_texto_image.resize((1280,250))
imgTK_config_dark=ImageTk.PhotoImage(config_dark_texto_image)
config_text=[imgTK_config_light,imgTK_config_dark]

x_button=Image.open('exit.png')
x_button=x_button.resize((50,50))
Tk_img_x=ImageTk.PhotoImage(x_button)

#Settings menu loop index
settings_loop_running=True
settings_loop_index=0

#Settings Menu Functions

# Funções de update: Apenas atualizam valores e cancelam after pendente (sem reiniciar loop)
def Update_Delay(settings_obj, delay_idx):
    global settings_after_id
    settings_obj.delay = settings_obj.delays[delay_idx]
    config_index[1] = delay_idx
    print(f"Delay atualizado imediatamente para: {settings_obj.delay}s (índice: {delay_idx})")
    
    # Cancela o agendamento pendente para evitar delay antigo
    if settings_after_id is not None:
        try:
            main.after_cancel(settings_after_id)
        except ValueError:
            pass  # Ignora se já executado
        settings_after_id = None

    
# Feedback visual: Mostra "concluído" por settings.delay segundos, então volta ao main_menu
def Update_Theme(settings_obj, theme_idx):
    #Atualiza o theme imediatamente no objeto settings e config_index[0], aplicando mudanças visuais.
    settings_obj.theme = settings_obj.themes[theme_idx]
    config_index[0] = theme_idx  # Atualiza o índice de rastreamento
    print(f"Theme atualizado imediatamente para: {settings_obj.theme} (índice: {theme_idx})")  # Log para depuração
    # Instantly apply the changes
    main.configure(background=settings_obj.theme)  # Atualiza background da janela principal
    if 'frame_configuracao' in globals() and frame_configuracao.winfo_exists():
        frame_configuracao.configure(bg=settings_obj.theme)
    if 'frame_opcoes' in globals() and frame_opcoes.winfo_exists():
        frame_opcoes.configure(bg=settings_obj.theme)
    if 'frame_unesp_logo' in globals() and frame_unesp_logo.winfo_exists():
        frame_unesp_logo.configure(bg=unesp_logo_bg_theme[theme_idx])
        # Atualiza logo se necessário (assumindo que é o mesmo para ambos, mas ajusta bg)
    if 'logo_label' in globals() and frame_unesp_logo.winfo_exists():
        logo_label.configure(bg=unesp_logo_bg_theme[theme_idx])
    # Atualiza texto de config dinamicamente se o label existir
    if 'configuracao_texto' in globals() and configuracao_texto.winfo_exists():
        configuracao_texto.configure(image=config_text[theme_idx])
        configuracao_texto.configure(bg=settings_obj.theme)
    
    # Feedback visual: Mostra "concluído" por settings.delay segundos, então volta ao main_menu

def settings_menu():
    
    def Done():
        # Limpa frames do settings
        for widget in frame_unesp_logo.winfo_children():
            widget.destroy()
        frame_unesp_logo.destroy()
        for widget in frame_opcoes.winfo_children():
            widget.destroy()
        frame_opcoes.destroy()
        for widget in frame_configuracao.winfo_children():
            widget.destroy()
        frame_configuracao.destroy()
        main_menu()

    def settings_control(i):
        updated = False
        if i=='1':
            Update_Delay(settings,0)
            updated = True
        if i=='1.25':
            Update_Delay(settings,1)
            updated = True
        if i=='1.5':
            Update_Delay(settings,2)
            updated = True
        if i=='1.75':
            Update_Delay(settings,3) 
            updated = True
        if i=='2':
            Update_Delay(settings,4)
            updated = True
        if i=='Light':
            Update_Theme(settings,0)
            updated = True
        if i=='Dark':
            Update_Theme(settings,1)
            updated = True
        if i=='Exit':
            Done()
            return
        if updated:
            global settings_loop_running, settings_after_id
            settings_loop_running = True  # Garante que rode
            settings_after_id = None  # Já cancelado no Update
            settings_scanning_loop()  # Reinicia aqui, no escopo correto
        
    global frame_unesp_logo
    frame_unesp_logo = Frame(main,width=1280, height=75,bg=unesp_logo_bg_theme[config_index[0]])
    frame_unesp_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    global logo_label
    logo_label= Label(frame_unesp_logo, image=imgTk_logo_unesp_lighttheme, bg=unesp_logo_bg_theme[config_index[0]])
    logo_label.place(x=527,y=0)

    #Frame TEXTO CONFIG
    global frame_configuracao
    frame_configuracao=Frame(main,width=1280, height=250,bg=settings.theme)
    frame_configuracao.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    global configuracao_texto
    configuracao_texto=Label(frame_configuracao,image=config_text[1],bg=settings.theme)
    configuracao_texto.place(x=0,y=0)

    #FRAME OPCOES DELAY 
    global frame_opcoes
    frame_opcoes=Frame(main,width=1280, height=580,bg=settings.theme)
    frame_opcoes.grid(row=1,column=0,pady=250,padx=0)

    s1_button=Button(frame_opcoes,image=imgTK_delay_button[0],anchor=CENTER,command=lambda:settings_control('1'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    s1_button.place(x=228,y=75)

    s125_button=Button(frame_opcoes,image=imgTK_delay_button[1],anchor=CENTER,command=lambda: settings_control('1.25'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    s125_button.place(x=403,y=75)

    s15_button=Button(frame_opcoes,image=imgTK_delay_button[2],anchor=CENTER,command=lambda: settings_control('1.5'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    s15_button.place(x=578,y=75)

    s175_button=Button(frame_opcoes,image=imgTK_delay_button[3],anchor=CENTER,command=lambda: settings_control('1.75'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    s175_button.place(x=753,y=75)

    s2_button=Button(frame_opcoes,image=imgTK_delay_button[4],anchor=CENTER,command=lambda: settings_control('2'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    s2_button.place(x=928,y=75)

    light_button=Button(frame_opcoes,image=imgTK_lighttheme,anchor=CENTER,command=lambda: settings_control('Light'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    light_button.place(x=403,y=250)

    dark_button=Button(frame_opcoes,image=imgTK_darktheme,anchor=CENTER,command=lambda: settings_control('Dark'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    dark_button.place(x=753,y=250)

    exit_button=Button(frame_opcoes,image=Tk_img_x,anchor=CENTER,command=lambda:settings_control('Exit'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    exit_button.place(x=928,y=250)

    settings_buttons=[s1_button,s125_button,s15_button,s175_button,s2_button,light_button,dark_button,exit_button]
    settings_list=['Exit','1','1.25','1.5','1.75','2','Light','Dark']
    def settings_scanning_loop():
        global settings_loop_index, settings_loop_running, settings_after_id
        if not settings_loop_running:
            return
        # Reseta cores
        for b in settings_buttons:
            b.config(bg=buttons_background)
        # Destaque atual
        settings_buttons[settings_loop_index].config(bg=selected_buttons_background)
        # Avança índice
        settings_loop_index = (settings_loop_index + 1) % len(settings_buttons)
        # Calcula timer com delay ATUAL (atualiza instantaneamente se mudado)
        timer = int(settings.delay * 1000)
        settings_after_id = main.after(timer, settings_scanning_loop)
    def select_settings(event=None):
        global settings_loop_index, settings_loop_running, settings_after_id
        selected = settings_list[settings_loop_index]
        
        # Cancela pendente e para loop temporariamente
        if settings_after_id is not None:
            try:
                main.after_cancel(settings_after_id)
            except ValueError:
                pass
            settings_after_id = None
            settings_control(selected)

    main.bind("<Return>", select_settings)

    settings_scanning_loop()

play_loop_index=0
play_loop_running=True
def play_menu():
    def play_control(i):
        comando=i
        arduino.write(comando.encode())
        if i=='exit':
            for widget in frame_unesp_logo.winfo_children():
                widget.destroy()
            frame_unesp_logo.destroy()
            for widget in frame_direcionais.winfo_children():
                widget.destroy()
            frame_direcionais.destroy()
            main_menu()

    global frame_unesp_logo
    frame_unesp_logo = Frame(main,width=1280, height=75,bg=unesp_logo_bg_theme[config_index[0]])
    frame_unesp_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    global logo_label
    logo_label= Label(frame_unesp_logo, image=imgTk_logo_unesp_lighttheme, bg=unesp_logo_bg_theme[config_index[0]])
    logo_label.place(x=527,y=0)


    global frame_direcionais
    frame_direcionais=Frame(main,width=1280,height=905,bg=settings.theme)
    frame_direcionais.grid(row=1,column=0, pady=0, padx=0, sticky=NSEW)

    up_button=Button(frame_direcionais,image=imgTK_up_button,anchor=CENTER,command=lambda:play_control('up'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    up_button.place(x=515,y=200)

    down_button=Button(frame_direcionais,image=imgTK_down_button,anchor=CENTER,command=lambda:play_control('down'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    down_button.place(x=515,y=475)

    left_button=Button(frame_direcionais,image=imgTK_left_button,anchor=CENTER,command=lambda:play_control('left'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    left_button.place(x=240,y=475)

    right_button=Button(frame_direcionais,image=imgTK_right_button,anchor=CENTER,command=lambda:play_control('right'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    right_button.place(x=790,y=475)

    exit_button=Button(frame_direcionais,image=Tk_img_x,anchor=CENTER,command=lambda:play_control('exit'),overrelief=RIDGE,relief=RAISED,bg=buttons_background)
    exit_button.place(x=1000,y=100)

    play_buttons=[up_button,right_button,down_button,left_button,exit_button]
    play_option=['exit','up','right','down','left']

    def play_scanning_loop():
        global play_loop_index, play_loop_running, main_after_id
        if not play_loop_running:
            return
        for b in play_buttons:
            b.config(bg=buttons_background)
        play_buttons[play_loop_index].config(bg=selected_buttons_background)
        play_loop_index = (play_loop_index + 1) % len(play_buttons)
        timer = int(settings.delay * 1000)  # Usa delay atual
        main_after_id = main.after(timer, play_scanning_loop)

    def Select_Option(event=None):
        global play_loop_running, play_loop_index, main_after_id
        play_control(play_option[play_loop_index])

    main.bind("<Return>", Select_Option)

    play_scanning_loop()
    

#Main Menu loop index
mainmenu_loop_running=True
main_menu_index=0
#Main Menu function
def main_menu():
    play_bg=buttons_background
    config_bg=buttons_background
    exit_bg=buttons_background
    main_menu_options=['exit','play','config']
    def main_menu_control(i):
        if i=='play':
            for widget in frame_unesp_logo.winfo_children():
                widget.destroy()
            for widget in frame_main_image.winfo_children():
                widget.destroy()
            for widget in frame_buttons.winfo_children():
                widget.destroy()
            play_menu()
        if i=='config':
            for widget in frame_unesp_logo.winfo_children():
                widget.destroy()

            for widget in frame_main_image.winfo_children():
                widget.destroy()
            for widget in frame_buttons.winfo_children():
                widget.destroy()
            settings_menu()
        if i=='exit':
            main.quit()
        
    #Creating frames on the main menu 
    #Width: Largura ; Height: Altura ; bg: Cor de fundo do frame ; Grid: posicionar o frame ; row=0: posicionado na primeira linha
    #column=0: posicionado na primeira coluna ; pady: margem vertical com relação ao frame ; padx: margem horizontal com relação ao frame ;
    global frame_unesp_logo
    frame_unesp_logo = Frame(main,width=1280, height=75,bg=unesp_logo_bg_theme[config_index[0]])
    frame_unesp_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    #main menu image frame
    global frame_main_image
    frame_main_image= Frame(main,width=550,height=430,bg=settings.theme)
    frame_main_image.grid(row=1, column=0, pady=50, padx=365, sticky=NSEW)

    #Main menu buttons frame
    global frame_buttons
    frame_buttons=Frame(main,width=1280,height=430,bg=settings.theme)
    frame_buttons.grid(row=2, column=0,pady=0, padx=0, sticky=NSEW)

    #lable to Unesp Logo
    logo_label= Label(frame_unesp_logo, image=imgTk_logo_unesp_lighttheme, background=unesp_logo_bg_theme[config_index[0]])
    logo_label.place(x=527,y=0)

    main_image_label=Label(frame_main_image,image=imgTk_main_menu,background=settings.theme)
    main_image_label.place(x=0, y=0)
        
    #Selected visual effect controller

    play_button=Button(frame_buttons,image=imgTk_play_button,anchor=CENTER,command=lambda:main_menu_control('play'),overrelief=RIDGE,relief=RAISED,bg=play_bg)
    play_button.place(x=170,y=0)

    config_button=Button(frame_buttons,image=imgTk_config_button,anchor=CENTER,command=lambda:main_menu_control('config'),overrelief=RIDGE,relief=RAISED,bg=config_bg)
    config_button.place(x=490,y=0)

    exit_button=Button(frame_buttons,image=imgTk_exit_button,anchor=CENTER,command=lambda:main_menu_control('exit'),overrelief=RIDGE,relief=RAISED,bg=exit_bg)
    exit_button.place(x=810,y=0)

    #Main menu Scanning Loop
    main_menu_buttons=[play_button,config_button,exit_button]

    def Main_Scanning_Loop():
        global main_menu_index, mainmenu_loop_running, main_after_id
        if not mainmenu_loop_running:
            return
        for b in main_menu_buttons:
            b.config(bg=buttons_background)
        main_menu_buttons[main_menu_index].config(bg=selected_buttons_background)
        main_menu_index = (main_menu_index + 1) % len(main_menu_buttons)
        timer = int(settings.delay * 1000)  # Usa delay atual
        main_after_id = main.after(timer, Main_Scanning_Loop)
    def Select_Option(event=None):
        global mainmenu_loop_running, main_menu_index, main_after_id
        if main_after_id is not None:
            try:
                main.after_cancel(main_after_id)
            except ValueError:
                pass
            main_after_id = None
        main_menu_control(main_menu_options[main_menu_index])

    main.bind("<Return>", Select_Option)

    Main_Scanning_Loop()


main_menu()
































main.mainloop()