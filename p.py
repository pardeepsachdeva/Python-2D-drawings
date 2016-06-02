from tkinter import *
#********main menu***********
def doNothing():
    print("Do nothting")

root=Tk()

menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New...",command=doNothing)
subMenu.add_command(label="Save...",command=doNothing)
subMenu.add_command(label="Save as...",command=doNothing)
subMenu.add_command(label="Close...",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit...",command=root.quit)


editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

drawMenu=Menu(menu)
menu.add_cascade(label="Draw",menu=drawMenu)
drawMenu.add_command(label="Line",command=doNothing)
drawMenu.add_command(label="Circle",command=doNothing)
drawMenu.add_command(label="Rectangle",command=doNothing)



#**********tool bar

toolbar=Frame(root,bg="blue")
insertButt=Button(toolbar,text="insert image",command=doNothing)
insertButt.pack(side=LEFT,padx=2, pady=2)
printButt=Button(toolbar,text="print image",command=doNothing)
printButt.pack(side=LEFT,padx=2, pady=2)
toolbar.pack(side=TOP,fill=X)

canvas=Canvas(root,width=400,height=100,bg="blue",bd=3)
canvas.pack()
blackline=canvas.create_line(0,0,10,10)
redline=canvas.create_line(0,100,200,50,fill="red")
grenBox=canvas.create_rectangle(0,100,200,50, fill="green")

root.mainloop()
