
import os
import subprocess
from tkinter import *
from tkinter import filedialog
delete = False
#scripts names and loctaions
scriptDict = {}
scriptDelete = ''
#open file read script info and format
file = open('script_loc.txt','r')
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip()
    scriptList =  line.split('/')
    script = scriptList[len(scriptList)-1]
    scriptList.pop()
    scriptDict[script] = '/'.join(scriptList)


window = Tk()
window.title("Script Manager")
window.geometry('800x600')
window.configure(bg='#4a4a4a')

top = Frame(window,bg='#4a4a4a')
middle = Frame(window,bg='#3d3d3d')
bottom  = Frame(window,bg='#4a4a4a')

def Refresh_Screen():
    global middle
    middle.destroy()
    middle = Frame(window,bg='#3d3d3d')
    middle.pack(ipadx=10,
    ipady=10,
    fill='both',
    expand=True)
    Write_Grid()



def Write_Grid():
    columnCount = 0
    rowCount = 0
    i = 0
    for i in scriptDict:
        print(i)
        label = Label(middle, text = i, bg ='#3d3d3d',fg = 'white',font=('Arial',11))
        label.grid(column = columnCount,row = rowCount,padx = 10,pady= 5)
        Buttons = Frame(middle,bg='#3d3d3d')
        button1 = Button(Buttons,text = 'Run Script',font=('Arial',11), bg = '#bababa',activebackground = '#3d3d3d',activeforeground='white',command=lambda c = i :Run_Script(c))
        button1.pack(side=LEFT)
        button2 = Button(Buttons,text = 'Delete Script',font=('Arial',11), bg = '#bababa',activebackground = '#3d3d3d',activeforeground='white',command=lambda c = i :Delete_Script(c))
        button2.pack(side=LEFT)
        Buttons.grid(column = columnCount,row = rowCount+1,padx=10)

        if columnCount >= 3:
            rowCount = rowCount + 2
            columnCount = 0
        else: 
            columnCount = columnCount + 1

def Get_Script():
    newScriptTup = filedialog.askopenfilenames()
    newScript = newScriptTup[0]

    #getting script name
    scriptList = newScript.split('/')
    script = scriptList[len(scriptList)-1]
    if script.split('.')[1] == 'py':

        #getting script directory
        scriptList.pop()
        scriptDir = '/'.join(scriptList)
        
        #add script to dict
        scriptDict[script] = scriptDir
        #format script data
        saveScript = ''
        for key in scriptDict:
            saveScript = saveScript + scriptDict[key]+'/'+key+'\n'
        
        #add script to list and Files
        file = open('script_loc.txt','w')
        file.write(saveScript)
        file.close()
        Write_Grid()
    #run script
    # os.chdir(scriptDir)
    # os.system(script)

def Delete_Script(script):
    scriptDelete = script
    scriptDict.pop(script)
    saveScript = ''
    for key in scriptDict:
        saveScript = saveScript + scriptDict[key]+'/'+key+'\n'
    
    #add script to list and Files
    file = open('script_loc.txt','w')
    file.write(saveScript)
    file.close()
    #middle = Frame(window,bg='#3d3d3d')
    Refresh_Screen()
def Run_Script(script):

    #run script
    os.chdir(scriptDict[script])
    os.system(script)

Button(top,activebackground='#4a4a4a',fg='white',bg='#3d3d3d',relief='groove',text='Add Script',command=Get_Script,font=('Arial',11)).pack(side=LEFT)

Write_Grid()
Label(bottom,bg='blue',text='bottom').pack()

top.pack(side=TOP,fill='x')
middle.pack(ipadx=10,
    ipady=10,
    fill='both',
    expand=True)
#bottom.pack(side=BOTTOM,fill='x')

window.mainloop()