import os
from tkinter import *
from tkinter.filedialog import askopenfilename

import customtkinter
import pytesseract
from PIL import Image
from gtts import gTTS
from playsound import playsound

root = customtkinter.CTk()
root.geometry("370x370")
root.resizable(True, True)
root.title('Soundify')
root.iconbitmap(os.path.join('assets', "icon.ico"))
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
dark_theme = True  # Helpful In Themes Switcher
img_light = PhotoImage(file=os.path.join('assets', 'light.png'))
img_dark = PhotoImage(file=os.path.join('assets', "dark.png"))
text_img = customtkinter.CTkImage(light_image=Image.open(os.path.join('assets', "text-light.ico")),
                                  dark_image=Image.open(os.path.join('assets', "text-dark.ico")))

sound_img = customtkinter.CTkImage(light_image=Image.open(os.path.join('assets', "speaking-light.ico")),
                                   dark_image=Image.open(os.path.join('assets', "speaking-dark.ico")))
link = " "


# Function To Set Dark Theme
def dark():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    theme.configure(image=img_dark, bg="#242424")
    sound.configure(hover_color="#242424")
    text.configure(hover_color="#242424")


# Function To Set light Theme
def light():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")
    theme.configure(image=img_light, bg='#ebebeb', activebackground='#ebebeb')
    sound.configure(hover_color="#ebebeb")
    text.configure(hover_color="#ebebeb")


# Theme Switcher Function
def theme_switch():
    global dark_theme

    if dark_theme:
        light()
        dark_theme = False
    else:
        dark()
        dark_theme = True


def from_file():
    global link
    link = askopenfilename()  # Initiate Link With Selected File Path


def image_to_sound(path_to_image):
    """
    Function for converting an  image to sound
    """
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        loaded_image = Image.open(path_to_image)
        decoded_text = pytesseract.image_to_string(loaded_image)
        cleaned_text = " \n".join(decoded_text.split("\n"))
        select_label.configure(text=f"\n\n{cleaned_text}", justify=LEFT)
        sound1 = gTTS(cleaned_text, lang="en")
        os.remove("sound.mp3")
        sound1.save("sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while executing the code\n", bug)
        return


def play_audio():
    playsound("sound.mp3")


select_label = customtkinter.CTkLabel(root, font=('calibri', 20, 'bold'), text="\n\n\n\nSelect an image ",
                                      fg_color="transparent", justify=CENTER, anchor=CENTER)
select_label.pack()

s_file = customtkinter.CTkButton(root, text='Browse', command=from_file, border_spacing=4, width=90)
s_file.place(x=135, y=230)
text = customtkinter.CTkButton(root, image=text_img, text=" ", command=lambda: image_to_sound(link),
                               hover_color="#242424",
                               fg_color="transparent", width=40)
text.place(x=135, y=265)
sound = customtkinter.CTkButton(root, image=sound_img, text=" ", command=play_audio, fg_color="transparent", width=40,
                                hover_color="#242424")
sound.place(x=190, y=265)
theme = Button(root, text='theme', command=theme_switch, bd=0, image=img_dark, bg="#242424")
theme.place(x=330, y=330)

root.mainloop()
