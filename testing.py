import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as tkBox
import tkinter.font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from testing import *


# %% Class App
class App:

    def __init__(self, root):

        root.title("Energy Usage 2010")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__Button_01 = tk.Button(root)
        self.__Button_01["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.__Button_01["font"] = ft
        self.__Button_01["fg"] = "#000000"
        self.__Button_01["justify"] = "center"
        self.__Button_01["text"] = "Open CSV file"
        self.__Button_01.place(x=70, y=50, width=90, height=25)
        self.__Button_01["command"] = self.Button_01_command
        self.__ComboBox_01 = ttk.Combobox(root)
        self.__ComboBox_01.set("Select community")
        self.__ComboBox_01.place(x=350, y=50, width=120, height=25)
        self.__ComboBox_01.bind("<<ComboboxSelected>>", self.testing)

        self.__Lable_01 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        self.__Lable_01["font"] = ft
        self.__Lable_01["fg"] = "#333333"
        self.__Lable_01["justify"] = "center"
        self.__Lable_01["text"] = "Please select a community:"
        self.__Lable_01.place(x=170, y=50, width=170, height=25)

# %%  Button command

    def Button_01_command(self):

        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.__ComboBox_01['values'] = list(self.__df['COMMUNITY AREA'
                                                          ' NAME'].unique())
        except filePath.DoesNotExist:
            tkBox.showinfo('This is an ugly Error!',
                           'Not that one, choose another')

# %% Combobox

    def testing(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'
                                               ''] == self.__ComboBox_01.get()]

        figure1 = plt.figure(dpi=50)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=50, y=130, width=250, height=155)
        kwhJanIdx = (self.__subdf.columns.get_loc('KWH JANUARY 2010'))
        self.__subdf.iloc[:, range(kwhJanIdx,
                                   kwhJanIdx+12)].mean().plot.bar(ax=ax1)
        ax1.set_title('KWH mean')

        figure1 = plt.figure(dpi=50)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=310, y=130, width=250, height=155)
        kwhJanIdx = (self.__subdf.columns.get_loc('THERM JANUARY 2010'))
        print(kwhJanIdx)
        self.__subdf.iloc[:, range(kwhJanIdx,
                                   kwhJanIdx+12)].mean().plot.bar(ax=ax1)
        ax1.set_title('THERM mean')

        figure1 = plt.figure(dpi=50)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=50, y=295, width=250, height=155)
        kwhJanIdx = (self.__subdf.columns.get_loc('KWH JANUARY 2010'))
        self.__subdf.iloc[:, range(kwhJanIdx,
                                   kwhJanIdx+12)].max().plot.bar(ax=ax1)
        ax1.set_title('KWH max')

        figure1 = plt.figure(dpi=50)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=310, y=295, width=250, height=155)
        kwhJanIdx = (self.__subdf.columns.get_loc('THERM JANUARY 2010'))
        self.__subdf.iloc[:, range(kwhJanIdx,
                                   kwhJanIdx+12)].max().plot.bar(ax=ax1)
        ax1.set_title('THERM max')
        
# %% Run


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
