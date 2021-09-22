command = "cmd.exe /C dir C:\\"
import os
import tkinter
#os.system('ipconfig')
cmd_text = os.popen('ipconfig').read()
finaltext = ''
for line in cmd_text.splitlines():
    templine = line.replace(" ", "")
    #print("qqqqqqqqq")
    #print(templine)
    #print("wwwwwwww")
    if(("Media") in line):
        newline = line[line.find(':') + 2:]
        print(newline)
        finaltext = finaltext + newline + os.linesep
        print("ooo")
        #ooo = re.sub(r'^.*?I', 'I', line)
        #tempint = index
        #temptempline = line[index(":"):]
from tkinter import *
window=Tk()
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('Hello Python')
lbl2=Label(window, text=finaltext, fg='black', font=("Helvetica", 16))
lbl2.place(x=60, y=50)
def refresh():
  tkinter.Message( "Hello Python", "Hello World")
btn=Button(window, text="Refresh", fg='black', command= refresh)
btn.place(x=80, y=100)
window.geometry("300x200+10+10")
window.mainloop()
    #print("x")
    #lineResult = libLAPFF.parseLine(line)
print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
#print(a)
print("cccccccccccccccccccccccccccc")
#print(type(a))
#print((a))