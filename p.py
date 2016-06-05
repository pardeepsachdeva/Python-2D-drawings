from tkinter import *
from tkinter.ttk import Notebook


#********main menu***********
def doNothing():
    print("Do nothting")

#basic blank window creation
root=Tk()
root.title("!ABC")
#adding menu into blank window
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

n=Notebook(root)
f1=Frame(n,width=200,height=200)
f2=Frame(n,width=200,height=200)
n.add(f1,text="first")
n.add(f2,text="second")
n.pack(fill=X)


left=Frame(root,bg="grey",bd=2,relief=GROOVE)


topLeft=Frame(left, bg="red", bd=5, relief=SUNKEN,height=800)

insertTopLeftButt1=Button(topLeft,text="insert image",command=doNothing)
insertTopLeftButt1.pack(side=TOP,padx=5, pady=5)

insertTopLeftButt2=Button(topLeft,text="insert image",command=doNothing)
insertTopLeftButt2.pack(side=TOP,padx=5, pady=5)

topLeft.pack(side=TOP,fill=X,padx=2,pady=2)

separator = Frame(left, height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X,padx=2,pady=2)


bottomLeft=Frame(left, bg="red",bd=5, relief=SUNKEN,height=400)

insertbottomLeftButt1=Button(bottomLeft,text="insert image",command=doNothing)
insertbottomLeftButt1.pack(side=TOP,padx=5, pady=5)

insertbottomLeftButt2=Button(bottomLeft,text="insert image",command=doNothing)
insertbottomLeftButt2.pack(side=TOP,padx=5, pady=5)

bottomLeft.pack(side=TOP,fill=X,padx=2,pady=2)

left.pack(side=LEFT,fill=Y)

canvas=Canvas(root,width=400,height=100,bg="blue",bd=3)
canvas.pack()
blackline=canvas.create_line(0,0,10,10)
redline=canvas.create_line(0,100,200,50,fill="red")
greenBox=canvas.create_rectangle(0,100,200,50, fill="green")

bottom=Frame(root,bg="grey", height=25)
bottom.pack(side=BOTTOM, fill=X)

root.mainloop()
