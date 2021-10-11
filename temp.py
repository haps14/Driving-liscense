
from tkinter import *

root = Tk()
root.title("Driving License")
root.geomentary("300x400")
root.mainloop()

root.configure(bg = "white")
canvas = canvas(root, width= 300, height= 400)
canvas.create_image(0, 0, anchor=NW)

canvas = canvas(root, width= 300, height= 400)
canvas.create_rectangle(0,0,300,55, fill="#1456380")
canvas.create_rectangle(0,345,300,400, fill = "#1456380")

label_heading = canvas.create_text(150,90, font=('Times' , '24','bold ital'))
label_name_tag = canvas.create_text(40,165, font=('Times' , '24','bold'))
label_pin_tag = canvas.create_text(40,205, font=('Times' , '24','bold'))
label_id_tag = canvas.create_text(40,250, font=('Times' , '24','bold'))
label_adress_tag = canvas.create_text(40,300, font=('Times' , '24','bold'))
label_vehicles_tag = canvas.create_text(40,325, font=('Times' , '24','bold'))
label_db_tag = canvas.create_text(40,350, font=('Times' , '24','bold'))

label_name = label(root)
label_pin = label(root)
label_id = label(root)
label_adress = label(root)
label_vehicles = label(root)
label_db = label(root)

def myCardDetails():
    name = "Winne the pooh"
    print(type(name))
    pin = "93839"
    print(type(pin))
    adress = "Disney Land"
    print(type(adress))
    vehicles ="Two Four"
    print(type(vehicles))
    db = "14 December 2008"
    print(type(db))
    
    
    label_name["text"] = name
    label_pin["text"] = pin
    label_adress["text"] = adress
    label_vehicles["text"] = vehicles
    label_db["text"] = db
       
    button1 = Button(root, text = "show my License" ,command=myCardDetails)
      
    
    









