from tkinter import *
import tkinter.messagebox
import urllib.request
import random



def downloadImage():
    try:
        name = random.randrange(1,10000)
        imagejpg = str(name) + ".jpg"

        # ********************************if you are using windows change download path*********************************

        urllib.request.urlretrieve(entr.get(),'/home/bathiya/Downloads/'+ imagejpg)
        lbl2.config(text="Image Downloaded")
    except :
        lbl2.config(text="Image Download fail")
        tkinter.messagebox.showerror("Error","File type should be .JPG")





root = Tk()
root.title("ImageI")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

root.geometry("300x350")
root.geometry("+{}+{}".format(positionRight,positionDown))
root.resizable(0, 0)

lbl1 = Label(root, text="Enter Image URL")
lbl1.pack(pady=10)

lbl2 = Label(root,text=" Status...", relief=SUNKEN, anchor=W)
lbl2.pack(side=BOTTOM, fill=X)

entr = Entry(root)
entr.pack(ipadx=35)


but = Button(root,text="Download", command=downloadImage)
but.pack(side=BOTTOM, pady=10)

root.mainloop()