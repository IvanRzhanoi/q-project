'''
This program does not check the status of the light yet
'''

#hubrequest.php
from tkinter import *
import requests



#In this part of code we change the light based on the value of labels
class Request:
    def lightStatusChangeBedroom(event):
        if bedroomLight.cget("text")=="No Light!":
            bedroomLight.configure(text="Light!",fg="black",bg="green")


            resp = requests.post('http://www.mywebsite.com/user',params=userdata)

        else:
            bedroomLight.configure(text="No Light!",fg="white",bg="black")
    def lightStatusChangeLivingRoom(event):
        if livingRoomLight.cget("text")=="No Light!":
            livingRoomLight.configure(text="Light!",fg="black",bg="green")
        else:
            livingRoomLight.configure(text="No Light!",fg="white",bg="black")
    def lightStatusChangeKitchen(event):
        if kitchenLight.cget("text")=="No Light!":
            kitchenLight.configure(text="Light!",fg="black",bg="green")
        else:
            kitchenLight.configure(text="No Light!",fg="white",bg="black")




userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}


'''
class RitasRule(Rule):
   type = 'ON_FROM_MOVEMENT_RULE'
   name = "Test rule by Rita"
   description = 'Test rule by Rita'
   summary = 'When motion sensor reports movement, put device on. If movement stops, put device off.'

   sensors = Input(field_type=None,
                   capabilities=[Capability.MOTION],
                   display_order=1,
                   description='Motion sensor',
                   min_count=1)

   devices = Output(field_type=None,
                    capabilities=[Capability.ON_OFF],
                    display_order=2,
                    description='Controlled device',
                    min_count=1)

   def send_commands(self, on: bool):
       for device in self.devices:
           if on:
               self.send_command(DeviceOnCommand(device))
           else:
               self.send_command(DeviceOffCommand(device))

   def on_event(self, ev):
       self.send_commands(ev.state.motion)
'''





root=Tk()

commandLabel1=Label(root,text="Light in Bedroom")
commandLabel1.grid(row=0,column=0,padx=10,pady=5)

bedroomLight=Button(text="Turn on!")
bedroomLight.bind('<Button-1>',Request.lightStatusChangeBedroom)
bedroomLight.grid(row=4,column=0,padx=10,pady=5)

w1=Canvas(root, width=6, height=165,bg="purple")
w1.grid(row=0,column=1,rowspan=10,pady=10)

commandLabel2=Label(root,text="Light in Living Room")
commandLabel2.grid(row=0,column=2,padx=10,pady=5)

livingRoomLight=Button(text="Turn on!")
livingRoomLight.bind('<Button-1>',Request.lightStatusChangeLivingRoom)
livingRoomLight.grid(row=4,column=2,padx=10,pady=5)

w2=Canvas(root, width=6, height=165,bg="green")
w2.grid(row=0,column=3,rowspan=10,pady=10)

commandLabel3=Label(root,text="Light in Kitchen")
commandLabel3.grid(row=0,column=4,padx=10,pady=5)

kitchenLight=Button(text="Turn on!")
kitchenLight.bind('<Button-1>',Request.lightStatusChangeKitchen)
kitchenLight.grid(row=4,column=4,padx=10,pady=5)


w10=Canvas(root, width=450, height=6,bg="yellow")
w10.grid(row=10,column=0,columnspan=10,pady=10)


commandLabel1=Label(root,text="Light in Bedroom")
commandLabel1.grid(row=11,column=0,padx=10,pady=5)

bedroomLight=Label(root,text="No Light!",fg="white",bg="black")
bedroomLight.grid(row=12,column=0,padx=10,pady=5)

w1=Canvas(root, width=6, height=165,bg="purple")
w1.grid(row=11,column=1,rowspan=10,pady=10)

commandLabel2=Label(root,text="Light in Living Room")
commandLabel2.grid(row=11,column=2,padx=10,pady=5)

livingRoomLight=Label(root,text="No Light!",fg="white",bg="black")
livingRoomLight.grid(row=12,column=2,padx=10,pady=5)

w2=Canvas(root, width=6, height=165,bg="green")
w2.grid(row=11,column=3,rowspan=10,pady=10)

commandLabel3=Label(root,text="Light in Kitchen")
commandLabel3.grid(row=11,column=4,padx=10,pady=5)

kitchenLight=Label(root,text="No Light!",fg="white",bg="black")
kitchenLight.grid(row=12,column=4,padx=10,pady=5)


root.mainloop()