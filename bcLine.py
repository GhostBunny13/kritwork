import tkinter as tk
from tkinter import ttk
import webbrowser
from multiprocessing import Process
import requests as req
import tkinter.messagebox
import random

#tkGroup = ["AjaIX2PwWhNE2WiHrGRz2a8wpySvj85nH3jj0rDkZMo"]
class Main:
    def topCheck(self):
        if self.varTop.get() != 1:
            self.root.attributes("-topmost", False)
        else:
            self.root.attributes("-topmost", True)
    def addToken(self):
        webbrowser.open("https://notify-bot.line.me/my/")
        #try:
        #    if self.pageToken.state() == "normal":
        #        self.pageToken.focus()
        #        self.pageToken.grab_set()
        #except:
        #    self.pageToken = tk.Toplevel(self.root)
        #    self.pageToken.title('หน้าจัดการtoken')
        #    self.pageToken.focus()
        #    self.pageToken.grab_set()

    def randMsg(self):
        listText = ["แดง", "น้ำเงิน"]
        Msg = random.choice(listText)
        self.sendApi(Msg)

        
    def sendApi(self, msg):
        with open("token.txt", "r") as myTk:
            tkGroup = myTk.read().splitlines()
            #print(tkGroup)
        for token in tkGroup:
            if tkGroup[0] != "#":
                req.post("https://notify-api.line.me/api/notify",data={"message": msg}, headers={"Authorization": "Bearer "+token})
    def sendMsg(self, event=""):
        msg = self.text.get("1.0", "end-1c")
        self.text.delete('1.0', tk.END)
        self.sendApi(msg)
    def run(self):
        self.root = tk.Tk()
        self.root.call('encoding', 'system', 'utf-8')
        self.root.title("โปรแกรมนำกลุ่ม")
        #self.root.geometry("400x200")
        self.f1 = tk.Frame(self.root)
        self.f1.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        self.varTop = tk.IntVar()
        self.varTop.set(0)
        self.chTop = tk.Checkbutton(self.f1, text="วางทับ",variable=self.varTop, command=self.topCheck)
        self.chTop.pack()
        tk.Button(self.f1, text="จัดการกลุ่ม", command=self.addToken).pack()
        self.text = tk.Text(self.f1, height=5, width=60, background="#e1e1ea")
        self.text.pack()
        #self.text.bind("<Shift-Enter>", self.sendMsg)
        tk.Button(self.f1, text="สุ่ม", command=self.randMsg).pack(side="left")
        ttk.Button(self.f1, text="ส่ง", command=self.sendMsg).pack(side="right")
        self.root.mainloop()
Main().run()
