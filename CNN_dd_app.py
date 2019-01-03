from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import tkinter
from tkinter.scrolledtext import ScrolledText
import CNN_dd
import sys
sys.setrecursionlimit(10000)
'''

Author: Haftu @ Brique Inc.
Year: 2018

'''
import logging

window = tkinter.Tk()
window.title("CNN based defect detection")
window.geometry('750x570')
#window.resizable(0,0)

lbl = Label(window, text=' Dataset Path:')
lbl.grid(column=0,row=2, pady=10, sticky=W,padx = 15)
txt = Entry(window, width = 85)
txt.grid(column=1, row=2,columnspan=1,pady=0)

lbl2 = Label(window, text=' Meta file Path:')
lbl2.grid(column=0,row=3, pady=10, sticky=W,padx = 15)
txt2 = Entry(window, width = 85)
txt2.grid(column=1, row=3,columnspan=1,pady=0)

lbl3 = Label(window, text=' Model Path:')
lbl3.grid(column=0,row=4, pady=10, sticky=W,padx = 15)
txt3 = Entry(window, width = 85)
txt3.grid(column=1, row=4,columnspan=1,pady=0)


lbl4 = Label(window, text=' Destination Path:')
lbl4.grid(column=0,row=5, pady=10, sticky=W,padx = 15)
txt4 = Entry(window, width = 85)
txt4.grid(column=1, row=5,columnspan=1,pady=0)

def dataset_path_fn():
    global data_dir
    txt.delete(first=0, last=150)
    data_dir = filedialog.askdirectory()
    txt.insert(INSERT, data_dir)
def metafile_path_fn():
    global meta_dir
    txt2.delete(first=0, last=150)
    meta_dir = filedialog.askopenfilename(initialdir = "", title = "Select meta file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    txt2.insert(INSERT, meta_dir)
def model_path_fn():
    global model_dir
    txt3.delete(first=0, last=150)
    model_dir = filedialog.askopenfilename(initialdir = "", title = "Select model file",filetypes = (("H5 files","*.h5"),("all files","*.*")))
    txt3.insert(INSERT, model_dir)

def model_path_tr_fn():
    global model_dir_tr
    txt3.delete(first=0, last=150)
    model_dir_tr = filedialog.askdirectory()
    txt3.insert(INSERT, model_dir_tr)

def destination_path_fn():
    global destination_dir
    txt4.delete(first=0, last=150)
    destination_dir = filedialog.askdirectory()
    txt4.insert(INSERT, destination_dir)

data_btn = Button(window, text = 'Browse', command = '')
data_btn.grid(column = 2, row = 2,padx = 5,pady=0)

meta_btn = Button(window, text = 'Browse', command = '')
meta_btn.grid(column = 2, row = 3,padx = 5,pady=0)

model_btn = Button(window, text = 'Browse', command = '')
model_btn.grid(column = 2, row = 4,padx=5, pady=0)

dest_btn = Button(window, text = 'Browse', command = '')
dest_btn.grid(column = 2, row = 5,padx=5, pady=0)

# tr_frame.pack()
# tst_frame = Frame(window)

# tst_frame.pack()
# op_type =  operation.get()
lbl3 = Label(window, text='Status:')
lbl3.grid(column=0,row=14, sticky=W, padx = 10)
txt5 = ScrolledText(window, width=100, height=20)
txt5.grid(column=0, row=15, columnspan=3, rowspan = 10, sticky=W, padx = 10)

def on_field_change(index, value, op):
    # op_type.get()

    global txt_height
    global txt_width


    if (op_type.get() == 'train'):

        global txt_batch_sz
        global txt_epochs
        global txt_tst_per

        data_btn = Button(window, text='Browse', command=dataset_path_fn)
        data_btn.grid(column=2, row=2, padx=5, pady=0)

        meta_btn = Button(window, text='Browse', command=metafile_path_fn)
        meta_btn.grid(column=2, row=3, padx=5, pady=0)

        model_btn = Button(window, text='Browse', command=model_path_tr_fn)
        model_btn.grid(column=2, row=4, padx=5, pady=0)

        dest_btn = Button(window, text='Browse', command='')
        dest_btn.grid(column=2, row=5, padx=5, pady=0)


        lbll = Label(window, text='Image Size (Height, Width)')
        lbll.grid(column=1, row=6, pady=0, sticky=W, padx=5)
        txt_height = Entry(window, width=8)
        txt_height.insert(END, 360)
        txt_height.grid(column=1, row=7, pady=0, sticky=W, padx=10)
        txt_width = Entry(window, width=8)
        txt_width.insert(END, 400)
        txt_width.grid(column=1, row=7, pady=0, sticky=W, padx=85)



        tr_lbl = Label(window, text='Epochs')
        tr_lbl.grid(column=1, row=6, columnspan=1, sticky=W,pady=1, padx=215)
        txt_epochs = Entry(window, width=8)
        txt_epochs.insert(END, 200)
        txt_epochs.grid(column=1, row=7, pady=0, sticky=W, padx=210)

        tr_lbl2 = Label(window, text='Batch_Sz')
        tr_lbl2.grid(column=1, row=6, columnspan=1, sticky=E, pady=1, padx=90)
        txt_batch_sz = Entry(window, width=8)
        txt_batch_sz.insert(END, 32)
        txt_batch_sz.grid(column=1, row=7, pady=0, sticky=E, padx=85)

        tr_lbl3 = Label(window, text='Test %')
        tr_lbl3.grid(column=1, row=6, columnspan=1, sticky=E,pady=10, padx=15)
        txt_tst_per = Entry(window, width=8)
        txt_tst_per.insert(END, 30)
        txt_tst_per.grid(column=1, row=7, pady=0, sticky=E, padx=5)

    elif (op_type.get() == 'test'):

        data_btn = Button(window, text='Browse', command=dataset_path_fn)
        data_btn.grid(column=2, row=2, padx=5, pady=0)

        meta_btn = Button(window, text='Browse', command='')
        meta_btn.grid(column=2, row=3, padx=5, pady=0)

        model_btn = Button(window, text='Browse', command=model_path_fn)
        model_btn.grid(column=2, row=4, padx=5, pady=0)

        dest_btn = Button(window, text='Browse', command=destination_path_fn)
        dest_btn.grid(column=2, row=5, padx=5, pady=0)

        lbll = Label(window, text='Image Size (Height, Width)')
        lbll.grid(column=1, row=6, pady=0, sticky=W, padx=5)
        txt_height = Entry(window, width=8)
        txt_height.insert(END, 360)
        txt_height.grid(column=1, row=7, pady=0, sticky=W, padx=10)
        txt_width = Entry(window, width=8)
        txt_width.insert(END, 400)
        txt_width.grid(column=1, row=7, pady=0, sticky=W, padx=85)

        tr_lbl = Label(window, text='Epochs')
        tr_lbl.grid(column=1, row=6, columnspan=1, sticky=W, pady=1, padx=220)
        txt_epochs = Entry(window, width=8, state = 'disabled')
        txt_epochs.grid(column=1, row=7, pady=0, sticky=W, padx=210)

        tr_lbl2 = Label(window, text='Batch_Sz')
        tr_lbl2.grid(column=1, row=6, columnspan=1, sticky=E, pady=1, padx=90)
        txt_batch_sz = Entry(window, width=8, state = 'disabled')
        txt_batch_sz.grid(column=1, row=7, pady=0, sticky=E, padx=85)

        tr_lbl3 = Label(window, text='Test %')
        tr_lbl3.grid(column=1, row=6, columnspan=1, sticky=E, pady=10, padx=15)
        txt_tst_per = Entry(window, width=8, state = 'disabled')
        txt_tst_per.grid(column=1, row=7, pady=0, sticky=E, padx=5)


def trace_change(index, value, op):
    on_field_change(index, value, op)


v = StringVar()
v.trace('w', trace_change)
##############################################################################
##############################################################################
op_type = Combobox(window, textvar=v, state="readonly")
op_type_lbl = Label(window, text='Type of operation')
op_type['values'] = ('train', 'test')
# op_type.current(0)
op_type_lbl.grid(column=0, row=0, pady=5, padx=10)
op_type.grid(column=1, row=0, pady=5, sticky=W, padx=0)

for rows in range(30):
        window.rowconfigure(rows, weight=1)
for columns in range(10):
        window.columnconfigure(columns, weight=1)

def redirector(inputStr):
    txt5.delete(1.0, END)
    txt5.insert(INSERT, inputStr)

def decorator(func):
    def inner(inputStr):
        try:
            #txt5.delete(1.0,END)
            txt5.insert(INSERT, inputStr)
            return func(inputStr)
        except:
            return func(inputStr)
    return inner




def run():

    global txt_batch_sz
    global txt_epochs
    global txt_height
    global txt_width
    global txt_tst_per

    global data_dir
    global meta_dir
    global model_dir
    global destination_dir
    global model_dir_tr

    opt_type = op_type.get()
    img_rows = int(txt_height.get())
    img_cols = int(txt_width.get())

    sys.stdout.write = decorator(sys.stdout.write)
    #sys.stdout.write = redirector

    if(opt_type=='train'):

        dataset_path = str(data_dir)
        model_path = str(model_dir_tr)
        metafile_path = str(meta_dir)
        epochs = int(txt_epochs.get())
        batch_size = int(txt_batch_sz.get())
        tst_per = int(txt_tst_per.get())
        CNN_dd.train_dd_cnn(dataset_path,metafile_path,model_path,img_rows, img_cols,epochs,batch_size,tst_per)

    else:

        dataset_path = str(data_dir)
        model_path = str(model_dir)
        destination_path = str(destination_dir)
        CNN_dd.test_dd_cnn(dataset_path, model_path, destination_path,img_rows,img_cols)

run_btn = Button(window, text="Train/Test", command=run)

run_btn.grid(column=2, row=11, pady=0)

#txt5.insert(INSERT, 'Loading dataset and training....this will take a while....please wait a moment!\n')
#txt5.insert(INSERT, 'Feel free to do other stuff and come back after a while...\n')

window.iconbitmap('icon_iPP_1.ico')
window.mainloop()
