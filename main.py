import BOT
import time
import PySimpleGUI as sg

form = sg.FlexForm('PRESENT(not)BOT by sheawn')  # begin with a blank form

layout = [[sg.Text('                                     Enter login details')],
          [sg.Text('username', size=(15, 1)), sg.InputText('XYZ@rnpodarschool.com')],
          [sg.Text('password', size=(15, 1)), sg.InputText('')],
          [sg.Text('                                     Enter details of 1st class')],
          [sg.Text('meeting code', size=(15, 1)), sg.InputText('rnpXYZ')],
          [sg.Text('time', size=(15, 1)), sg.InputText('time left for class(seconds)')],
          [sg.Text('duration', size=(15, 1)), sg.InputText('class duration(seconds)')],
          [sg.Text('                                     Enter details of 2nd class')],
          [sg.Text('                                     (if no class leave empty)')],
          [sg.Text('meeting code', size=(15, 1)), sg.InputText(' ')],
          [sg.Text('time', size=(15, 1)), sg.InputText(' ')],
          [sg.Text('duration', size=(15, 1)), sg.InputText(' ')],
          [sg.Text('                                   yall owe me money, just saying')],
          [sg.Submit(), sg.Cancel()]
          ]

button, values = form.Layout(layout).Read()


def check_SecondClass():
    if values[5] == ' ':
        BOT.leaveclass()
    else:
        BOT.joinclass(values[5], values[0], values[1])
        time.sleep(int(values[7]))  # class duration
        BOT.leaveclass()


for i in range(int(values[3]), 0, -1):
    time.sleep(1)
    print(i)

time.sleep(int(values[3]))  # time before 1st class

BOT.joinclass(values[2], values[0], values[1])
time.sleep(int(values[4]))  # class duration
BOT.leaveclass()

time.sleep(int(values[6]) - int(values[3]))  # time before next class
check_SecondClass()

