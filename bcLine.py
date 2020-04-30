import tkinter as tk
from tkinter import ttk
import webbrowser
from multiprocessing import Process

class Main:
    def topCheck(self):
        if self.varTop.get() != 1:
            self.root.attributes("-topmost", False)
        else:
            self.root.attributes("-topmost", True)
    def addToken(self):
        try:
            if self.pageToken.state() == "normal":
                self.pageToken.focus()
                self.pageToken.grab_set()
        except:
            self.pageToken = tk.Toplevel(self.root)
            self.pageToken.title('หน้าจัดการtoken')
            self.pageToken.focus()
            self.pageToken.grab_set()

        
    def run(self):
        self.root = tk.Tk()
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
        tk.Button(self.f1, text="สุ่ม").pack(side="left")
        ttk.Button(self.f1, text="ส่ง").pack(side="right")
        self.root.mainloop()
Main().run()
