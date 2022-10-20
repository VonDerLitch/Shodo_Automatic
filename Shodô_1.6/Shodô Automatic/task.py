import wmi
from tkinter import messagebox
from sys import exit

def taskCheck():
    f = wmi.WMI()

    flag = 0

    # Iterating through all the running processes
    for process in f.Win32_Process():
        if "shodo.exe" == process.Name:
            messagebox.showinfo('Shodo Automatic', \
                                'Shodo já está em execução')
            flag = 1
            exit()

    if flag == 0:
        print("Application is not Running")



