# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:07:05 2022

@author: ankit computer
"""

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Lucky friend Wheel")
entercity_name = Entry(root)
entercity_name.place(relx=0.5,rely=0.2,anchor=CENTER)
entercountry_name = Entry(root)
entercountry_name.place(relx=0.5,rely=0.1,anchor=CENTER)
city_list=Label(root)
country_list=Label(root)
random_city_label = Label(root)
random_country_label = Label(root)


list1 = []
list2 = []
def addcitycountry():
    city_name = entercity_name.get()
    list1.append(city_name)
    city_list["text"] = "City list " +str(list1)
    country_name = entercountry_name.get()
    list2.append(country_name)
    country_list["text"] = "Country list " +str(list2)
    
def ran():
    length = len(list1)
    length2 = len(list2)
    randomcity = random.randomint(0,length - 1)
    random_city_label["text"] = str(list1[randomcity])
    randomcountry = random.randomint(0,length2 - 1)
    random_country_label["text"] = str(list2[randomcountry])
     
btn = Button(root,text="Add Country and city" ,command=addcitycountry)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
city_list.place(relx=0.5,rely=0.4,anchor=CENTER)
country_list.place(relx=0.5,rely=0.5,anchor=CENTER)
btn1 = Button(root,text="Generate random City and Country",command=ran)
btn1.place(relx=0.5,rely=0.6,anchor=CENTER)

random_city_label.place(relx=0.5,rely=0.7,anchor=CENTER)
random_country_label.place(relx=0.5,rely=0.8,anchor=CENTER)