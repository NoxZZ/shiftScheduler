import pandas as pd
import itertools
from tkinter import *
from tkinter.filedialog import askopenfile
root = Tk()
root.geometry('200x100')
temp = []   
d = {}
def open_file():
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

    for i in sorted_d:
        temp_text = '{1} \t\t {0}'.format(i[0],i[1])
        Label(root,text=temp_text).pack()
        #print(i[0],i[1])

 
btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 
mainloop()