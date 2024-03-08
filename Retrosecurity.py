import tkinter 
from tkinter import messagebox
import subprocess
import time
import os

def check():
     return not os.path.exists("Retrosecurity.flag")

def run():
     with open("Retrosecurity.flag", "w") as f:
          f.write("Tools are installed")

def preinstall():
     if check():
        nmap = 'pip install nmap'
        photon = 'pip install photon'
        subprocess.run(nmap, capture_output=True, text=True, shell=True)
        subprocess.run(photon, capture_output=True, text=True, shell=True)
        run()
     else:
          nmap_update = 'pip install --upgrade nmap'
          photon_update = 'pip install --upgrade photon'
          subprocess.run(nmap_update, capture_output=True, text=True, shell=True)
          subprocess.run(photon_update, capture_output=True, text=True, shell=True)
          run()
   
preinstall()

def noti():
     if textbox is not None:
        t = time.sleep(1)
        messagebox.showinfo("Message","Retro-security \n Process initiated!")
        
def final():
    noti()
    a=textbox.get()
    q = password.get()
    result = f"echo {q} | sudo -S nmap -Pn {a}"
    if checkboxvar1.get()==1:
        result+=" -O"
    if checkboxvar2.get()==1:
        z=port_number.get()
        x=f" -p {z}"
        result+=x
    if checkboxvar3.get()==1:
        result+=" -sS -sV"
    if checkboxvar4.get()==1:
        result+=" -A"
    command = subprocess.run(result, capture_output=True, text=True, shell=True)
    if command.returncode == 0:
        output.insert(tkinter.END, "\n"+command.stdout)
    else:
        output.insert(tkinter.END, "\n"+command.stderr)
    print(result)

root = tkinter.Tk()
root.title("Retro security")
root.geometry("600x400")
photo = tkinter.PhotoImage(file="logo2.png")
root.iconphoto(True,photo)
root.resizable(False, False)

checkboxvar1 = tkinter.IntVar()
checkboxvar2 = tkinter.IntVar()
checkboxvar3 = tkinter.IntVar()
checkboxvar4 = tkinter.IntVar()

left_frame = tkinter.Frame(root, bg="#388895", width=200, height=400)
left_frame.grid(row=0, column=1)

middle_frame = tkinter.Frame(root, bg="black", width=4, height=400)
middle_frame.grid(row=0, column=2)

right_frame = tkinter.Frame(root, bg="#f7efd8", width=400, height=400)
right_frame.grid(row=0, column=3)

label = tkinter.Label(left_frame, text="Enter ip or link", font="Impact 20 bold", bg="#388895", fg="#f7efd8")
label.place(x=7, y=1)

textbox = tkinter.Entry(left_frame, width=17,font="Impact 18 bold", bg="#388895", fg="#f7efd8",)
textbox.place(x=10, y=35)

tools = tkinter.Label(left_frame, text="Tools", font="Arial 20 bold", bg="#388895", fg="#f7efd8")
tools.place(x=10, y=70)

Start = tkinter.Button(left_frame, text="Start", font="Arial 18 bold", bg="white", fg="#388895",width=16, height=1,borderwidth=0,command=final)
Start.config(bg="#388895",fg="#303A52")
Start.place(x=-1, y=371)

option = tkinter.Label(left_frame, text="Options", font="Arial 20 bold", bg="#388895", fg="#f7efd8")
option.place(x=100, y=70)

os = tkinter.Checkbutton(left_frame, text="OS", font="Arial 14 bold", bg="#388895", fg="#f7efd8",variable=checkboxvar1)
os.place(x=110, y=110)

port = tkinter.Checkbutton(left_frame, text="Port", font="Arial 14 bold", bg="#388895", fg="#f7efd8",variable=checkboxvar2)
port.place(x=110, y=145)

service = tkinter.Checkbutton(left_frame,text="Service", font="Arial 14 bold", bg="#388895", fg="#f7efd8",variable=checkboxvar3)
service.place(x=110, y=180)

info = tkinter.Checkbutton(left_frame, text="Info", font="Arial 14 bold", bg="#388895", fg="#f7efd8",variable=checkboxvar4)
info.place(x=110, y=215)

os_label = tkinter.Label(left_frame, text="OS Dection", font="Arial 14 bold", bg="#388895",fg="#f7efd8")
os_label.place(x=10, y=110)

port_number = tkinter.Entry(left_frame, width=5, font="Arial 14 bold", bg="#388895", fg="#f7efd8",borderwidth=0,)
port_number.place(x=135, y=145)

port_label = tkinter.Label(left_frame, text="Port Scan", font="Arial 14 bold", bg="#388895", fg="#f7efd8")
port_label.place(x=10, y=145)

service_label = tkinter.Label(left_frame, text="Find Service", font="Arial 14 bold", bg="#388895", fg="#f7efd8")
service_label.place(x=10, y=180)

info_label = tkinter.Label(left_frame, text="Find Info", font="Arial 14 bold", bg="#388895", fg="#f7efd8")
info_label.place(x=10, y=215)

password_label=tkinter.Label(left_frame,text="System\n Password:",font="Arial 14 bold",bg="#388895",fg="#f7efd8")
password_label.place(x=9,y=325)

password=tkinter.Entry(left_frame,width=10 ,show="*" ,font="Arial 16 bold",bg="#388895",fg="#f7efd8",)
password.place(x=90,y=335)

output = tkinter.Text(right_frame,width=46,height=20,font="Arial 14 bold",bg="#f7efd8",fg="black",)
output.place(x=10,y=60)

output_label = tkinter.Label(right_frame,text="Output",font="Impact 20 bold",bg="#f7efd8",fg="black",)
output_label.place(x=18,y=45)

search1_label = tkinter.Label(right_frame,text="Retro-security",font="Impact 24 bold",bg="#f7efd8",fg="black")
search1_label.place(x=130,y=12)

osint_label = tkinter.Label(right_frame,text="OSINT",font="Impact 10 bold",bg="#f7efd8",fg="black")
osint_label.place(x=280,y=6)

root.mainloop()
