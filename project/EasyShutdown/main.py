from configs import *
from tkinter import messagebox
import tkinter as tk
import json

#界面更新
def update_language():
    root.title(LANGUAGES[current_language]["title"])
    language.config(text = LANGUAGES[current_language]["buttons"]["language"])
    style.config(text = LANGUAGES[current_language]["buttons"]["style"])
    shutdown.config(text = LANGUAGES[current_language]["buttons"]["shutdown"])
    sleep.config(text = LANGUAGES[current_language]["buttons"]["sleep"])
    reboot.config(text = LANGUAGES[current_language]["buttons"]["reboot"])

def update_style():
    root.config(bg=STYLES[current_style]["bg"])
    language.config(bg=STYLES[current_style]["bg"], fg=STYLES[current_style]["fg"])
    style.config(bg=STYLES[current_style]["bg"], fg=STYLES[current_style]["fg"])
    shutdown.config(bg=STYLES[current_style]["bg"], fg=STYLES[current_style]["fg"])
    sleep.config(bg=STYLES[current_style]["bg"], fg=STYLES[current_style]["fg"])
    reboot.config(bg=STYLES[current_style]["bg"], fg=STYLES[current_style]["fg"])

#更改设置
def change_language(new_lang):#切换语言
    global current_language
    current_language = new_lang
    update_language()
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump({"language": new_lang,"style": current_style}, f, ensure_ascii=False, indent=4)

def change_style(new_style):#切换UI风格样式
    global current_style
    current_style = new_style
    update_style()
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump({"language": current_language,"style": new_style}, f, ensure_ascii=False, indent=4)

#事件
def on_select(choice):#作出选择后将选项写入choice.txt临时文件传递给bat文件
    with open("choice.txt", "w") as f:
        f.write(choice)
    root.destroy()

def on_closing():
    if messagebox.askokcancel(LANGUAGES[current_language]["events"]["on_closing"]["title"], LANGUAGES[current_language]["events"]["on_closing"]["content"]):
        with open("choice.txt", "w") as f:
            f.write("close")
        root.destroy()  # 如果用户点击确定，则销毁窗口

#界面显示
def create_choice_window():#创建选择窗口
    global root
    root = tk.Tk()
    root.title(LANGUAGES[current_language]["title"])
    root.geometry("480x360")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    global language, style, shutdown, sleep, reboot
    language = tk.Button(root, command=lambda: change_language("en" if current_language == "zh" else "zh"))
    language.pack(pady=10)
    style = tk.Button(root, command=lambda: change_style("dark" if current_style == "default" else "default"))
    style.pack(pady=10)
    shutdown = tk.Button(root, width=30, command=lambda: on_select("shutdown"))
    shutdown.pack(pady=10)
    sleep = tk.Button(root, width=30, command=lambda: on_select("sleep"))
    sleep.pack(pady=10)
    reboot = tk.Button(root, width=30, command=lambda: on_select("reboot"))
    reboot.pack(pady=10)
    update_language()
    update_style()
    root.mainloop()

if __name__ == "__main__":
    create_choice_window()
