import Tkinter 
from Tkinter import*
from threading import Thread
import threading
import serial

serial_object = None
 def Connect():
    global serial_object.get()
    Baud = Baud_rate.get()
    Port = Serial_Port.get()

    try:
        
        serial_object = serial.Serial('COM' + str(port),Baud,timeout = 0)
    except ValueRrror:
        print("Error Baud and Port")
        return
 
 def Disconnect():
    global serial_object
    try:
        serial_object.close

    except AttributeError:
        print("Closed without Using it")

def transmit():
    global serial_pbject
    send_data = 'Hello World'
    serial_object.write(send_data)

def receive():
    while(1):
        while(serial_object.inWaiting() == 0)
            pass

        try:
            serial_data = serial_object.readline().strip('\n').strip('\r')

            v= stringVar()
            DATALABEL1 = Label(root,textvariable = v, width = 10)
            DATALABEL1.place(x=100,y=110)
            v.set(serial_data)

        except:
            pass
        
def Send():
    t1 = threading.Thread(target - transmit)
    t1.daemon = Trye
    t1.start()
def Read():
    t1 = threading.Thread(target.receive)
    t1.daemon = True
    t1.start()
	

    

    
root= Tk()
root.title('Demo')
root.resizable(False,False)
root.geometry('{}x{}'.format(500,300))

BaudRate = Label(root,text = 'Baud Rate: ', width = 10)
BaudRate.place(x=10,y=10)

SerialPort = Label(root,text = 'Serial Port ', width = 10)
SerialPort.place(x=10,y=30)

Baud_Rate = Entry(width = 7)
Baud_Rate.place(x = 100, y= 10)

Serial_Port= Entry(width = 7)
Serial_Port.place(x = 100, y = 30)

ButtonOne = Button(root, text = 'Connect',command = Connect).place(x = 250,y = 30)
ButtonTwo = Button(root, text = 'Disconnect',command = Disconnect).place(x = 250,y = 30)
ButtonThree = Button(root, text = 'Send',command = Send).place(x = 10,y = 50)
ButtonFour = Button(root, text = 'Read',command = Read).place(x = 10,y =80)

LabelOne = Label(root,text = "Hello World",width = 10)
Labeltwo - Label(root,text = "Arduio Response",width = 14)
LabelOne = place()
Labeltwo = place()

LabelThree = Label(root,text = "x",width = 10)
LabelThree.place(x = 100, y = 110)


root.mainloop()

