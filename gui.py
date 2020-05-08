from tkinter import *
from tkinter.filedialog import askopenfile
import tkinter.scrolledtext as tkst
import pandas as pd
import itertools
import tkinter 
window = Tk()
window.title('tasker')
window.geometry('1920x1080')
#scheduler btn for file selection
btn = Button(window, text="Shift Scheduler",height=2,width=20,borderwidth = 5,command = lambda:open_file())
btn.grid(column=1, row=0)
#entry box for search bar
e1 = tkinter.Entry(window)
e1.grid(row = 0 , column = 5)
#search btn   
btn = Button(window, text="Search",height=2,width=20,borderwidth = 5,command = lambda:disp())
btn.grid(column=6, row=0)
sorted_d = []

def open_file():
    d = {}
    temp = []
    global sorted_d
    file_open = askopenfile(mode='rb',filetypes = [('xlxs files ','*.xlsx')])
    f = pd.read_excel(file_open, sheet_name = 'Sheet1')
    arr = f.iloc[:, 4:5]
    for index,row in arr.iterrows():
        temp = list(row[0].split('\n'))
        temp.remove(temp[0])
        for i in temp:
            a = i.split(',')
            for e in a:
                if(e not in d):
                #cnt+=1
                    d.update({e : 1})
                else:
                    d[e]+=1
    sorted_d = sorted((value, key) for (key,value) in d.items())

    area = tkst.ScrolledText(
        master = window,
        wrap = tkinter.WORD,
        width = 50,
        height = 50
    )    
    area.grid(row=10,column = 60,sticky = E)
    for i in range(len(sorted_d)):
        temp_text = '{1} \t\t\t\t\t {0}\n'.format(sorted_d[i][0],sorted_d[i][1])
        area.insert(tkinter.INSERT,temp_text)
        #Label(window, text = temp_text ).grid(row=i+1,ipadx=10,ipady=10,column=15)        
    #     print(sorted_d[i][0],sorted_d[i][1])
def disp():
    area = tkst.ScrolledText(
        master = window,
        wrap = tkinter.WORD,
        width = 50,
        height = 50
    )    
    area.grid(padx=20, pady=20,row=5,sticky=tkinter.W)
    print(sorted_d)
    for i in range(len(sorted_d)):
        if(sorted_d[i][1] == e1.get()):
            temp_text = '{1} \t\t {0}\n'.format(sorted_d[i][0],sorted_d[i][1])
            area.insert(tkinter.INSERT,temp_text)
            #Label(window, text = temp_text ).grid(row=i+1,ipadx=10,ipady=10,column=15)        
            print(sorted_d[i][0],sorted_d[i][1])

window.mainloop()