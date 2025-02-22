from configs import *
from algorithm import *
from tkinter import messagebox
import tkinter as tk
import json
import wxauto
import copy
wx = wxauto.WeChat()
friends = wx.GetAllFriends()

#界面更新
def update_language():
    root.title(LANGUAGES[current_language]["title"])
    language.config(text = LANGUAGES[current_language]["buttons"]["language"])
    style.config(text = LANGUAGES[current_language]["buttons"]["style"])
    send.config(text = LANGUAGES[current_language]["buttons"]["send"])
    if inputing:
        window.title(LANGUAGES[current_language]["events"]["on_send"]["title"])
        search_tips.config(text = LANGUAGES[current_language]["events"]["on_send"]["search_tips"])
        money_tips.config(text = LANGUAGES[current_language]["events"]["on_send"]["money_tips"])
        sendConfirm.config(text = LANGUAGES[current_language]["events"]["on_send"]["send"])
        confirm.config(text = LANGUAGES[current_language]["events"]["on_send"]["confirm"])
        refresh.config(text = LANGUAGES[current_language]["events"]["on_send"]["refresh"])
        

def update_style():
    root.config(bg = STYLES[current_style]["bg"])
    language.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
    style.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
    send.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
    if inputing:
        window.config(bg = STYLES[current_style]["bg"])
        search_tips.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
        search.config(insertbackground = STYLES[current_style]["ibg"], bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
        select_box.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
        money_tips.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
        money.config(insertbackground = STYLES[current_style]["ibg"], bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
        sendConfirm.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
        confirm.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])
        refresh.config(bg = STYLES[current_style]["bg"], fg = STYLES[current_style]["fg"])

#更改设置
def change_language(new_lang):#切换语言
    global current_language
    current_language = new_lang
    update_language()
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump({"language": new_lang,"style": current_style}, f, ensure_ascii = False, indent = 4)

def change_style(new_style):#切换UI风格样式
    global current_style
    current_style = new_style
    update_style()
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump({"language": current_language,"style": new_style}, f, ensure_ascii = False, indent = 4)

#刷新会话列表options
def refreshSessionList(refresh = False):
    global search, options, friends
    if refresh:
        friends = wx.GetAllFriends()
    options = friends.copy()
    i = 0
    while i < len(options):
        options[i] = options[i]["nickname"]
        if search.get() and not search.get() in options[i]:
            options.pop(i)
        else:
            i += 1

#money输入检验
def validate_input(new_value):
    if new_value == "":
        return True
    elif "." in new_value:
        return False
    try:
        if float(new_value) > 0 and int(float(new_value)) == float(new_value):
            return True
        return False
    except ValueError:
        return False

#事件
def on_closing():
    if messagebox.askokcancel(LANGUAGES[current_language]["events"]["on_closing"]["title"], LANGUAGES[current_language]["events"]["on_closing"]["content"]):
        root.destroy()

def on_refresh(refresh = False):
    global options, select_box, selected_option
    refreshSessionList(refresh)
    menu = select_box["menu"]
    menu.delete(0, tk.END)#删除所有选项
    #为Menu添加新的选项
    for option in options:
        menu.add_command(label = option, command = lambda v = option: selected_option.set(v))
    #刷新默认选项
    if len(options):
        selected_option.set(options[0])
    else:
        selected_option.set("")

def on_select_change():
    print(selected_option.get())

def on_send_closing():
    global inputing, window
    inputing = False
    window.destroy()

def on_sendConfirm():
    if money.get() == "":
        return
    else:
        money_amount = int(float(money.get()))
    wx.ChatWith(selected_option.get())
    nums = calculate(money_amount)
    for i in range(len(nums)):#遍历nums
        for _ in range(nums[i]):
            wx.SendFiles(f"RMB{par[i]}.png")
    global inputing
    inputing = False

def on_send():
    global inputing
    if inputing:
        messagebox.askokcancel(LANGUAGES[current_language]["events"]["on_send"]["repeat"]["title"], LANGUAGES[current_language]["events"]["on_send"]["repeat"]["content"])
        return
    inputing = True
    global root, window, search_tips, search, confirm, refresh, select_box, money_tips, money, sendConfirm
    window = tk.Toplevel(root)
    window.title(LANGUAGES[current_language]["events"]["on_send"]["title"])
    window.geometry("360x270")
    window.protocol("WM_DELETE_WINDOW", on_send_closing)
    search_tips = tk.Label(window, text = LANGUAGES[current_language]["events"]["on_send"]["search_tips"])
    search_tips.pack()
    search = tk.Entry(window)
    search.pack()
    confirm = tk.Button(window, text = LANGUAGES[current_language]["events"]["on_send"]["confirm"], command = lambda: on_refresh())
    confirm.pack()
    refresh = tk.Button(window, text = LANGUAGES[current_language]["events"]["on_send"]["refresh"], command = lambda: on_refresh(True))
    refresh.pack()
    global options, selected_option
    refreshSessionList()
    selected_option = tk.StringVar(window)
    selected_option.set(options[0])#默认选项
    select_box = tk.OptionMenu(window, selected_option, *options)
    select_box.pack()
    money_tips = tk.Label(window, text = LANGUAGES[current_language]["events"]["on_send"]["money_tips"])
    money_tips.pack()
    validation = window.register(validate_input)#注册检验函数
    money = tk.Entry(window, validate = "key", validatecommand = (validation, "%P"))#应用检验函数
    money.pack()
    sendConfirm = tk.Button(window, text = LANGUAGES[current_language]["events"]["on_send"]["send"], command = lambda: on_sendConfirm())
    sendConfirm.pack()
    update_style()

#界面显示
def create_root_window():#创建主窗口
    global root
    root = tk.Tk()
    root.title(LANGUAGES[current_language]["title"])
    root.geometry("480x270")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    global language, style, send
    language = tk.Button(root, command = lambda: change_language("en" if current_language == "zh" else "zh"))
    language.pack(pady = 10)
    style = tk.Button(root, command = lambda: change_style("dark" if current_style == "default" else "default"))
    style.pack(pady = 10)
    send = tk.Button(root, width = 30, command = lambda: on_send())
    send.pack(pady = 10)
    update_language()
    update_style()
    root.mainloop()

if __name__ == "__main__":
    create_root_window()
