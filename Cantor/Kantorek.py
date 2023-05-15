
import tkinter as tk
from tkinter import ttk
import json
import urllib.request
from tkinter import messagebox
from tkinter.messagebox import showinfo

try:
    url="http://api.nbp.pl/api/exchangerates/tables/C/"
    response=urllib.request.urlopen(url,timeout=5)
    data=json.loads(response.read())
    key='currency'
    values_of_key=[waluta[key] for waluta in data[0]['rates'] ]
    key2='bid'
    kurs=[i[key2] for i in data[0]['rates']]

    values_of_key+=["PLN"]
    kurs+=["1"]
    
    backup=open("Backup_data.json","w")
    json.dump(data,backup)
    backup.close()
            
except urllib.error.URLError:
    with open("Backup_data.json","r") as backupfile:
        lista=json.loads(backupfile.read())
        values_of_key=[waluta['currency'] for waluta in lista[0]['rates']]
        kurs= [i['bid'] for i in lista[0]['rates']]
    backupfile.close()


def currency_picked():
    return combobox.get()

def currency_final():
    return combobox2.get()
    
def calculator():
    if writebox3.get()=="":
        messagebox.showerror(title="ERROR",message="Enter the amount")
        
    else:
        for value in values_of_key:
            for value2 in values_of_key:
                if value==currency_picked():
                    if value2==currency_final():
                        x= (int(writebox3.get())/float(kurs[values_of_key.index(value2)])*float(kurs[values_of_key.index(value)]))
        ttk.Label(window,text="Result: ").place(x=320,y=0)   
        ttk.Label(window, text=str(x), background="Green").place(x=320,y=20)
    
            
window= tk.Tk()
window.geometry("500x500")
window.title("Kalkulator walut")
current_var=tk.StringVar()
next_var=tk.StringVar()
final_var=tk.StringVar()

combobox=ttk.Combobox(window,textvariable= current_var)
combobox["state"]="readonly"
combobox["values"]=values_of_key
combobox.place(x=0,y=20)

label1=ttk.Label(text="Select a source currency")
label1.pack(padx=5,pady=5,)
label1.place(x=0,y=0)

combobox.bind('<<ComboboxSelected>>', currency_picked)
combobox2=ttk.Combobox(window,textvariable=next_var)
combobox2["state"]="readonly"
combobox2["values"]=values_of_key
combobox2.place(x=150,y=20)
combobox.bind('<<ComboboxSelected>>', currency_final())

label2=ttk.Label(text="Select a final currency")
label2.place(x=150,y=0)
writebox3=tk.Entry(window,font=(30))
writebox3.place(x=0,y=70)
label3=ttk.Label(text="Write amount of money you want to convert ")
label3.place(x=0,y=50)
Calculate=tk.Button(window,text="calculate",command=calculator)
Calculate.place(x=0,y=100)

window.mainloop()
