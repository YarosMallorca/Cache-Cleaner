# MODULES
from tkinter import *
from tkinter.ttk import Button, Frame, Style
from configparser import ConfigParser
from PIL import ImageTk, Image
import time
import webbrowser
from win10toast import ToastNotifier
import os
import subprocess
import datetime

config = ConfigParser()

# THEME DETECTOR

config.read('config.ini')
pluginvalue = (config.get('settings', 'autorun'))
themevalue = (config.get('settings', 'theme'))

if themevalue == 'bright':
    global background
    background = 'white'
    global icons
    icons = 'white'

else:
    background = '#2d2d2d'

# MAIN WINDOW SETUP
window = Tk()
window.title("CacheCleaner")
window.geometry('500x300')
window.resizable(width=False, height=False)
window.iconbitmap("ui/logo/logo_small.ico")
window.overrideredirect(0)
window.configure(bg=background)



# FUNCTIONS

# MAIN WINDOW
def execute():
    recyclecommand()
    tempcommand()
    updatecommand()
  

def recyclecommand():
    recyclevalue = recyclevar.get()
    if (recyclevalue) == 1:
        os.startfile('recyclebin.bat')
    else:
        return

def tempcommand():
    tempvalue = tempvar.get()
    if (tempvalue) == 1:
        os.startfile('temp.bat')
    else:
        return

def updatecommand():
    updatevalue = updatevar.get()
    if (updatevalue) == 1:
        os.startfile('updates.lnk')
    else:
        return

#   SAVE SETTINGS
def savesettings():
    themesetting = darkvar.get()
    if (themesetting) == 1:
        config['settings'] = {
                'autorun': pluginvalue,
                'theme': 'dark'
        }
        with open('config.ini', 'w') as f:
            config.write(f)
        settingswindow.destroy()
        
    else:
        config['settings'] = {
                'autorun': pluginvalue,
                'theme': 'bright'
        }
        with open('config.ini', 'w') as f:
            config.write(f)
        settingswindow.destroy()
# CLOSE SETTINGS
def closesettings():
    settingswindow.destroy()

# SETTINGS
def opensettings():
    global settingswindow
    settingswindow = Toplevel()
    settingswindow.title('CacheCleaner Settings')
    settingswindow.geometry('350x250')
    settingswindow.resizable(width=False, height=False)
    settingswindow.iconbitmap("ui/logo/logo_small.ico")
    settingswindow.overrideredirect(0)
    settingswindow.configure(bg=background)

    Button(settingswindow, text="Cancel", command=closesettings).place(x=270, y=220)
    Button(settingswindow, text="OK", command=savesettings).place(x=190, y=220)
    
    global darkvar
    darkvar = IntVar()

    if background == 'white':
        
        settingslabel = Label(settingswindow, text="Cache Cleaner Settings", bg=background, font=("Arial Bold", 15))
        settingslabel.place(x=55, y=5)

        Label(settingswindow, text="Monthly reminder:", bg=background, font=("Calibri", 13)).place(x=5, y=45)
        Label(settingswindow, text="Use dark mode:", bg=background, font=("Calibri", 13)).place(x=5, y=100)
        Label(settingswindow, text="(restart required)", bg=background, font=("Calibri", 11)).place(x=5, y=120)

        
        darkcheck = Checkbutton(settingswindow, text="", variable=darkvar, bg='white', activebackground=background, selectcolor='white', font=("Calibri", 13))
        darkcheck.place(x=120, y=99)
        darkcheck.deselect()

    else:
        settingslabel = Label(settingswindow, text="Cache Cleaner Settings", bg=background, foreground='#FFFFFF', font=("Arial Bold", 15))
        settingslabel.place(x=55, y=5)

        Label(settingswindow, text="Monthly reminder:", bg=background, foreground='#FFFFFF', font=("Calibri", 13)).place(x=5, y=45)
        Label(settingswindow, text="Use dark mode:", bg=background, foreground='#FFFFFF', font=("Calibri", 13)).place(x=5, y=100)
        Label(settingswindow, text="(restart required)", bg=background, foreground='#FFFFFF', font=("Calibri", 11)).place(x=5, y=120)

        darkcheck = Checkbutton(settingswindow, text="", variable=darkvar, bg=background, activebackground=background, foreground='white', activeforeground='white', selectcolor='#2d2d2d', font=("Calibri", 13))
        darkcheck.place(x=120, y=99)
        darkcheck.select()

    config.read('config.ini')
    autorunvalue = (config.get('settings', 'autorun'))

    def installplugin():
        config['settings'] = {
            'autorun': 'true',
            'theme': themevalue
        }
        with open('config.ini', 'w') as f:
            config.write(f)

        os.startfile('reminder.bat')

        Button(settingswindow, text="Uninstall plugin", command=uninstallplugin).place(x=145, y=47)

    def uninstallplugin():
        config['settings'] = {
            'autorun': 'false',
            'theme': themevalue
        }
        with open('config.ini', 'w') as f:
            config.write(f)

        os.startfile('noreminder.bat')
        Button(settingswindow, text="  Install plugin   ", command=installplugin).place(x=145, y=47)

    if autorunvalue == 'false':
        Button(settingswindow, text="  Install plugin   ", command=installplugin).place(x=145, y=47)

    else:
        Button(settingswindow, text="Uninstall plugin", command=uninstallplugin).place(x=145, y=47)



# ICONS

if background == 'white':

    logo = ImageTk.PhotoImage(Image.open("ui/logo/title.png"))
    logolabel = Label(window, image=logo, bg=background).place(x=85, y=5)

    recycleimage = ImageTk.PhotoImage(Image.open("ui/main/recycle_bin.png"))
    logolabel = Label(window, image=recycleimage, bg=background).place(x=190, y=67)

    tempimage = ImageTk.PhotoImage(Image.open("ui/main/temp_folder.png"))
    logolabel = Label(window, image=tempimage, bg=background).place(x=260, y=115)

    updateimage = ImageTk.PhotoImage(Image.open("ui/main/updates.png"))
    logolabel = Label(window, image=updateimage, bg=background).place(x=255, y=170)

else:

    logo = ImageTk.PhotoImage(Image.open("ui/logo/title_dark.png"))
    logolabel = Label(window, image=logo, bg=background).place(x=85, y=5)

    recycleimage = ImageTk.PhotoImage(Image.open("ui/main/dark/recycle_bin.png"))
    logolabel = Label(window, image=recycleimage, bg=background).place(x=190, y=67)

    tempimage = ImageTk.PhotoImage(Image.open("ui/main/dark/temp_folder.png"))
    logolabel = Label(window, image=tempimage, bg=background).place(x=260, y=115)

    updateimage = ImageTk.PhotoImage(Image.open("ui/main/dark/updates.png"))
    logolabel = Label(window, image=updateimage, bg=background).place(x=255, y=170)

# CHECKBOXES


recyclevar = IntVar()
tempvar = IntVar()
updatevar = IntVar()

if background == 'white':
    recyclecheck = Checkbutton(window, text="Empty the Recycle Bin", variable=recyclevar, bg='white', activebackground=background, selectcolor='white', font=("Calibri", 13))
    recyclecheck.place(x=15, y=75)
    recyclecheck.select()



    tempcheck = Checkbutton(window, text="Clean the Temporary Directory", variable=tempvar, bg=background, activebackground=background, selectcolor='white', font=("Calibri", 13))
    tempcheck.place(x=15, y=125)
    tempcheck.select()



    updatecheck = Checkbutton(window, text="Delete old Windows Updates", variable=updatevar, bg=background, activebackground=background, selectcolor='white', font=("Calibri", 13))
    updatecheck.place(x=15, y=175)
    updatecheck.select()

else:

    recyclecheck = Checkbutton(window, text="Empty the Recycle Bin", variable=recyclevar, bg=background, activebackground=background, foreground='white', activeforeground='white', selectcolor='#2d2d2d', font=("Calibri", 13))
    recyclecheck.place(x=15, y=75)
    recyclecheck.select()


    tempcheck = Checkbutton(window, text="Clean the Temporary Directory", variable=tempvar, bg=background, activebackground=background, foreground='white', activeforeground='white', selectcolor='#2d2d2d', font=("Calibri", 13))
    tempcheck.place(x=15, y=125)
    tempcheck.select()


    updatecheck = Checkbutton(window, text="Delete old Windows Updates", variable=updatevar, bg=background, activebackground=background, foreground='white', activeforeground='white', selectcolor='#2d2d2d', font=("Calibri", 13))
    updatecheck.place(x=15, y=175)
    updatecheck.select()

 
# BUTTONS
Button(window, text="Execute", command=execute).place(x=95, y=230)

settingsicon = ImageTk.PhotoImage(Image.open("ui/main/settings.png"))
Button(window, image=settingsicon, command=opensettings).place(x=462, y=262)

window.mainloop()
