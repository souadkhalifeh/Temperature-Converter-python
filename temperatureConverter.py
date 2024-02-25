import tkinter as tk
from functools import partial

tempValue="Celcius"

def store_temp(temp):
    global tempValue
    tempValue=temp

def call_result(res1,res2,input):
    temp=input.get()
    if tempValue=="Celcius":
        f=float((float(temp)*9/5)+32)
        k=float((float(temp)+273.15))
        res1.config(text="%f Fahrenheit" %f)
        res2.config(text="%f Kelvin" %k)
    if tempValue=="Fahrenheit":
        c=float((float(temp)-32)*5/9)
        k=c+273
        res1.config(text="%f Celcius" %c)
        res2.config(text="%f Kelvin" %k)
    if tempValue=="Kelvin":        
        c=float((float(temp)-273.15))
        f=float((float(temp)-273.15)*1.0000 + 32.00)
        res1.config(text="%f Celcius" %c)
        res2.config(text="%f Fahrenheit" %f)
    return 

root=tk.Tk()
root.geometry("400x150")
root.title("Temperature Converter")
root.configure(background="Light Blue")
nb_input=tk.StringVar()
var=tk.StringVar()

input_label=tk.Label(root,text="Enter temperature:",background="Light Blue")
input_entry=tk.Entry(root,textvariable=nb_input)
input_label.grid(row=0)
input_entry.grid(row=0, column=1)


result_label1=tk.Label(root,text="Result1:",background="Light Blue")
result_label1.grid(row=2,columnspan=4)

result_label2=tk.Label(root,text="Result2:",background="Light Blue")
result_label2.grid(row=3,columnspan=4)

call_result= partial(call_result,result_label1,result_label2,nb_input)
result_button=tk.Button(root,text="Convert",command=call_result,background="Light Blue")
result_button.grid(row=1,columnspan=4)

dropdownList=["Celcius","Fahrenheit","Kelvin"]
dropdown=tk.OptionMenu(root,var,*dropdownList,command=store_temp)
dropdown.config(background="Light Blue")
dropdown["menu"].config(background="Light Blue")
var.set(dropdownList[0])
dropdown.grid(row=0,column=3)
root.mainloop()