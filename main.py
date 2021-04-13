import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as tkBox
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class App:
    def __init__(self, root):
        # setting title
        root.title("Energy Usage 2010") # change this to proper name when you think of one.
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,(screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__Button_01= tk.Button(root)
        self.__Button_01["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.__Button_01["font"] = ft
        self.__Button_01["fg"] = "#000000"
        self.__Button_01["justify"] = "center"
        self.__Button_01["text"] = "Open CSV file" # this is the button name change it to a propper if needed
        self.__Button_01.place(x=70, y=50, width=90, height=25)
        self.__Button_01["command"] = self.Button_01_command
        self.__ComboBox_01 = ttk.Combobox(root)
        self.__ComboBox_01.set("Select community")
        self.__ComboBox_01.place(x=350, y=50, width=120, height=25)
        self.__ComboBox_01.bind("<<ComboboxSelected>>", self.__comboBoxCb)

        self.__Lable_01 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        self.__Lable_01["font"] = ft
        self.__Lable_01["fg"] = "#333333"
        self.__Lable_01["justify"] = "center"
        self.__Lable_01["text"] = "Please select a community:"
        self.__Lable_01.place(x=170, y=50, width=170, height=25)

        # these canvases are broken, fix them
        self.__GLineEdit_517 = tk.Canvas(root,bg='blue')
        self.__GLineEdit_517.place(x=50, y=130, width=250, height=155)
      
        self.__GLineEdit_985 = tk.Canvas(root,bg='red')
        self.__GLineEdit_985.place(x=310, y=130, width=250, height=155)

        self.__GLineEdit_392 = tk.Canvas(root,bg='yellow')
        self.__GLineEdit_392.place(x=50, y=295, width=250, height=155)

        self.__GLineEdit_700 = tk.Canvas(root,bg='green')
        self.__GLineEdit_700.place(x=310, y=295, width=250, height=155)

    def Button_01_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.__ComboBox_01['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            tkBox.showinfo('This is an ugly Error!', 'Not that one, choose another')
            #print('nope')

    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.__ComboBox_01.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.__GLineEdit_392.winfo_width, self.__GLineEdit_392.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)
      


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
