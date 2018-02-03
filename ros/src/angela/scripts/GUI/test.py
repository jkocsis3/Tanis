#!/usr/bin/env python
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()


class useroutput():
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "JoyStick.py":'


    def __init__(self, debug=True):
        self._DEBUG = debug
        self.makeGUI()
        
        # self.root.mainloop()

        

    def makeGUI(self):
        self.initializetkinter()
        self.showImage()
        self.updateImage()
        print("makeGUI")
        print("starting main loop")
        # root.update()
        root.mainloop()
        # self.root.mainloop()

    def SayHi(self):
        # self.initializetkinter()
        print("sayHi")
        w = tk.Label(root, text="Fuck Off", fg='red', bg='black').grid(row=0, column=1)
        # w.pack()
        x = tk.Label(root, text="asshole", fg='red', bg='black').grid(row=1, column=1)
        # x.pack()
        # self.root.mainloop()

    def initializetkinter(self):
        # self.root = tk.Tk()
        self.counter = 1

    def counter_label(self, label):
        def count():
            self.counter += 1
            label.config(text=str(self.counter))
            label.after(1000, count)
        count()


    def setDymanicLabel(self):
        self.root.title = "This is a test"
        label = tk.Label(self.root, fg="green")
        label.pack()
        self.counter = 1
        self.counter_label(label)
        button = tk.Button(self.root, text='stop', width=25, command=self.root.destroy)
        button.pack()
        self.root.mainloop()

    def setGenericLabel(self, title):
        return tk.Label(self.root, fg='green', bg='white', text=title)        


    def setLayout(self):
        print("starting method")
        counter = 0
        while counter < 5:
            tk.Label(self.root, fg='green', bg='blue', text=str(counter)).grid(row=counter, column=counter)  # self.setGenericLabel(title="blarg")
            counter += 1
            print(str(counter))
        # newLabel = tk.Label(self.root, fg='green', bg='white', text=str(counter))
        # newLabel.grid(row=3, column=2)
        self.root.mainloop()

    def showImage(self):
        print("showing Image")
        path = './images/Image 00' + '1' + '.png'
        print(path)
        image = ImageTk.PhotoImage(Image.open(path))
        self.labtext = "starting"
        blarg = tk.Label(root, width=100, height=20, text="Here we go!")
        blarg.grid(row=0, column=0)
        self.label = tk.Label(root, width=100, height=20, image=image)  
        # self.label.pack()
        self.label.grid(row=1, column=0)
        # self.updateImage()
        # self.label.pack()
        # root.mainloop()


    def updateText(self):        
        print("Updating...")
        self.label.configure(text=self.labtext)
        self.labtext = str(self.counter)
        root.after(1000, self.updateText)
        self.counter += 1

    def updateImage(self):
        path = './images/Image 00' + str(self.counter) + '.png'
        image = ImageTk.PhotoImage(Image.open(path))        
        # need to add the second call setting the image, to prevent garbage collection from deleting the image..
        self.label.configure(image=image)
        self.label.image = image
        self.counter += 1
        root.after(1000, self.updateImage)

if __name__ == '__main__':
    useroutput()
