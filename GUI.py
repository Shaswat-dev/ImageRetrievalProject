from tkinter import *
from tkinter import Tk,Toplevel, Listbox
#import tkFileDialog
from tkinter import filedialog
from PIL import Image, ImageTk
import control
import os
import sys



def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
######################################################
       
class Ask(Tk):
        def __init__(self):
                self.im = None
                self.open_window()
                
        def open_window(self):
                self.im = filedialog.askopenfilename(parent=root, title="Select image to compare")
 

 
class MyApp(Tk):
        def __init__ (self, parent):
                Tk.__init__(self, parent)
                self.parent = parent
                self.initialize()
                
        def initialize(self):
                    
                top_frame = Frame(master=None, bd=0)
                top_frame.pack(fill=X, padx=0, pady=0)
                bottom_frame = Frame(master=None, height=300, bd=0)
                bottom_frame.pack(fill=BOTH, padx=3, pady=3, expand=1)
                    
                topleft_frame = Frame(master=top_frame, height=22, width= 500, bd=0)
                topleft_frame.pack(side=LEFT,fill=Y, padx=2, pady=2)
                topright_frame = Frame(master=top_frame, height=22, width=500, bd=1, relief=SUNKEN)
                topright_frame.pack(fill=Y, padx=5, pady=27)
                    
                    
                    
                def callback():
                        print('Retrieving similar images...')
                        r_value()
                        can_height()
                        if v.get() == 2:
                                j = control.MyImage(a,2)
                                list1 = j.intersections[1:]
                        else:
                                j = control.MyImage(a,1)
                                list1 = j.distancewith[1:]
                        self.load_images(self.can, list1, self.r)
                    
                        print("Done!")
                
                    
                def callback2():
                        print("Trying to restart program")
                        restart_program()
                
                
                restart_button = Button(master=topright_frame,text='Select New Image!',command=callback2)
                restart_button.pack(side=RIGHT,anchor=SE,padx=5,pady=5)
                go_button = Button(master=topright_frame, text='Retrieve Similar Images!', command=callback)
                go_button.pack(side=RIGHT, anchor=SE, padx=5, pady=5)
        
        
                var = str(win1.im)
                var = var[41:]
                quote = "''"
                quote = str(quote)
                myphoto_title = Label(topleft_frame, text="User input image: " + quote + var + quote)
                myphoto_title.pack(anchor='nw')
            
                topleftbot_frame = Frame(master=topleft_frame, bd=5,relief=SUNKEN)
                topleftbot_frame.pack(side=BOTTOM, padx=4, pady=4)
                
                can1 = Canvas(master=topleftbot_frame, width=box[2]-2, height=box[3]-2)
                can1.pack(fill=BOTH)
            
                can1photo = ImageTk.PhotoImage(myphoto_thumb)
                self.can1photo = can1photo
                can1.create_image(0,0, image=can1photo, anchor=NW)
            
            
                method_ask_text = "Which retrieval option would you like to use?"
                Label(topright_frame, text=method_ask_text).pack(anchor=W)
            
                v = IntVar()
                method1 = "Distance retrieval"
                method2 = "Intersection retrieval"
                rdbut1 = Radiobutton(master=topright_frame, text=method1, variable=v, value=1)
                rdbut1.pack(anchor=W)
                rdbut2 = Radiobutton(master=topright_frame, text=method2, variable=v, value=2)
                rdbut2.pack(anchor=W)
                rdbut1.select()
            
                num_ask_text = "\n How many images would you like to display?"
                Label(topright_frame, text=num_ask_text).pack(anchor=W)
                self.r = 25
            
                def r_value():
                        #print w.get()
                        if w.get()==2:
                                self.r = 50
                        elif w.get()==3:
                                self.r = 100
                        else:
                                self.r = 25
                            
                w = IntVar()
                opt1 = "25"
                opt2 = "50"
                opt3 = "100"
                rdbut3 = Radiobutton(master=topright_frame, text=opt1, variable=w, value=1)
                rdbut3.pack(anchor=W) 
                rdbut4 = Radiobutton(master=topright_frame, text=opt2, variable=w, value=2)
                rdbut4.pack(anchor=W) 
                rdbut5 = Radiobutton(master=topright_frame, text=opt3, variable=w, value=3)
                rdbut5.pack(anchor=W) 
            
                rdbut3.select()
            
                Label(bottom_frame, text="Similar Images:").pack(side=TOP, anchor=W)
                
                scroll_height = 850
                
                def can_height():
                        if w.get()==1 or w.get()==0:
                                scroll_height = 850
                        if w.get()==2:
                                scroll_height = 1700
                        if w.get()==3:
                                scroll_height = 3400
                        self.can.config(scrollregion=(0,0,scroll_height,scroll_height))
                    
                can_width = (5*size[0])+(7*1)
                self.bottombot_frame = Frame(master=bottom_frame, height=78, width=500, bd=1, relief=SUNKEN)
                self.bottombot_frame.pack(side=BOTTOM, fill=BOTH, padx=2, pady=2, expand=1)
                self.can = Canvas(self.bottombot_frame,bg='#FFFFFF',width=can_width, scrollregion=(0,0,scroll_height,scroll_height))

                scrollbar = Scrollbar(self.bottombot_frame)
                scrollbar.pack(side=RIGHT, fill=Y)
                scrollbar.config(command=self.can.yview)
                
                
                self.can.config(yscrollcommand=scrollbar.set)
                self.can.pack(expand=True, fill=BOTH)

                self.load_images(self.can, list1, self.r)

        def load_images(self, canvas, list1, how_many):
                    countx = 0
                    county = 0
                    r = how_many
                    l = [0]*r
                    for i in range(r):
                     p = Image.open(list1[i][1])
                     p_thumb = p.copy()
                     p_thumb.thumbnail(size)
                     l[i] = ["photo{0}".format(i)]
                     l[i] = ImageTk.PhotoImage(p_thumb)
                     self.l = l
                     x = 1 + (countx * size[0]) + (countx * 1)
                     y = 1 + (county * size[1]) + (county * 1)
                     canvas.create_image(x, y, image=l[i], anchor=NW)
                     if countx == 4:
                      countx = 0
                      county += 1
                     else:
                      countx += 1
                    return
                    
                    
                            
####################################################################            
            
            
        
if __name__ == "__main__":

        root = Tk()
        root.withdraw()
        win1 = Ask()
        win1.im
           
        size = 170, 170
        size2 = 328, 328
           
        myphoto = Image.open(win1.im)
        a = str(win1.im)
        print(a[41:])
        i = control.MyImage(a,1)
        list1 = i.distancewith[1:]
        myphoto_thumb = myphoto.copy()
        myphoto_thumb.thumbnail(size2)
        box = myphoto_thumb.getbbox()
           
        root.deiconify()
        app = MyApp(None)
        app.title('Video Retrieval GUI')
        app.destroy()
        app.mainloop()
