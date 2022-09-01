import tkinter as tk

#????


class main:

    def __init__(self):

        self.root = tk.Tk()  # ?????

        self.btn = tk.Button(self.root, text='????',
                             command=self.addlabel)  # ??btn
        self.cv = tk.Canvas(self.root, width=200, height=250, bg='white',
                            relief='solid', bd=0, highlightthickness=0)  # ??cv
        self.frm = tk.Frame(self.cv, relief='sunken')  # ??frm

        self.cv.create_window((0, 0), window=self.frm,
                              anchor='nw')  # ?cv?????frm
        self.cv.configure(scrollregion=(
            0, 0, self.frm.winfo_width(), self.frm.winfo_height()))  # ?cv???????frm???

        self.btn.pack()  # pack??
        self.cv.pack(fill='x')

        self.root.mainloop()

    def addlabel(self):  # ????

        __label = tk.Label(self.frm, text='??', width=27, relief='sunken')
        self.cv.bind('<MouseWheel>', lambda event: self.cv.yview_scroll(
            int(-1*(event.delta/50)), 'units'))
        __label.bind('<MouseWheel>', lambda event: self.cv.yview_scroll(
            int(-1*(event.delta/50)), 'units'))
        #???????????
        __label.pack(side='bottom', fill='x')

        self.root.update()  # ????
        self.cv.configure(scrollregion=(0, 0, self.frm.winfo_width(), max(self.frm.winfo_height(), self.cv.winfo_height()))) # ??????cv???????frm???

main()
