from tkinter import *
root = Tk()
root.title('Title of GUI')
Label(root,text="ID Number:").grid() # 0,0
Label(root,text="Name:").grid() # 1,0
Entry(root).grid(row=0,column=1)
Entry(root).grid(row=1,column=1) 
root.mainloop()