#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
class Window(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        #Build Object/建立物件
        #label物件
        self.lb_1 = tk.Label(self, height=1, width=30, text="出發地")
        self.lb_2 = tk.Label(self, height=1, width=30, text="目的地")
        self.lb_3 = tk.Label(self, height=1, width=30, text="時間(年/月)")
        self.lb_4 = tk.Label(self, height=1, width=30, text="天數")
        #entry物件(空白輸入)
        self.en_0 = tk.Entry(self, width = 30)
        self.en_1 = tk.Entry(self, width = 30)
        self.en_2 = tk.Entry(self, width = 30)
        self.en_3 = tk.Entry(self, width = 30)
        self.en_4 = tk.Entry(self, width = 30)
        self.en_5 = tk.Entry(self, width = 30)
        self.en_6 = tk.Entry(self, width = 30)
        self.en_7 = tk.Entry(self, width = 30)
        self.en_8 = tk.Entry(self, width = 30)
        self.en_9 = tk.Entry(self, width = 30)
        
        #button物件
        self.btn = tk.Button(self, height=1, width=20, text="搜尋",command =self.input_data)
        self.spbtn = tk.Checkbutton(self, text="特殊條件",command =self.create_special)
        #物件指定位置(基本介面：出發/到達/日期/天數/搜尋)
        self.lb_1.grid(row=1, column=1)
        self.en_1.grid(row=2, column=1)
        self.lb_2.grid(row=1, column=2)
        self.en_2.grid(row=2, column=2)
        self.lb_3.grid(row=1, column=3)
        self.en_3.grid(row=2, column=3)
        self.lb_4.grid(row=1, column=4)
        self.en_4.grid(row=2, column=4)
        self.btn.grid(row=2, column=5)
        self.spbtn.grid(row=2, column=6)

    # 資料輸入定義式(未完成)        
    def input_data(self):
        bfrom = self.en_1.get()
        depart = self.en_2.get()
        time = self.en_3.get()
        day = self.en_4.get()
        input_test = bfrom + depart
        print(input_test)
    # 製作特殊需求函數
    def create_special(self):
        self.lb_0 = tk.Label(self, height=1, width=30, text="去回or單程")
        self.lb_5 = tk.Label(self, height=1, width=30, text="人數(成人/孩童/嬰兒")
        self.lb_6 = tk.Label(self, height=1, width=30, text="直飛與否")
        self.lb_7 = tk.Label(self, height=1, width=30, text="去程時段(輸入：早or午or晚)")
        self.lb_8 = tk.Label(self, height=1, width=30, text="去程時段(輸入：早or午or晚)")
        self.lb_9 = tk.Label(self, height=1, width=30, text="票價(輸入：0-10000")
        
        self.lb_0.grid(row=3, column=1)
        self.lb_5.grid(row=3, column=2)
        self.lb_6.grid(row=3, column=3)
        self.lb_7.grid(row=5, column=1)
        self.lb_8.grid(row=5, column=2)
        self.lb_9.grid(row=5, column=3)

        self.en_0.grid(row=4, column=1)
        self.en_5.grid(row=4, column=2)
        self.en_6.grid(row=4, column=3)
        self.en_7.grid(row=6, column=1)
        self.en_8.grid(row=6, column=2)
        self.en_9.grid(row=6, column=3)

  
        
        
myprogram = Window()

myprogram.master.geometry("1400x1200")  # 寬x高
myprogram.master.title("my window")  # 程式標題
myprogram.mainloop()

