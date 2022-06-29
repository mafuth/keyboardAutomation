import keyboard
import json
from datetime import datetime
import time

def createHelp():
    modfiers = {'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'}
    print("\nMain key names: \n")
    for value in modfiers:
        print(value)
    print("\n\n")

def createKeys():
    log = open("storage/keyLogger.log", "w")
    keys = []
    while True:
        inputValue = input('enter a key combo or a key: ')
        if inputValue != "exit":
            keys.append(inputValue)
        else:
            log.write(json.dumps(keys))
            break

def simulate(sleepTime):
    now = datetime.now()

    print("Simulating Keyboard from log file")
    log = open("storage/keyLogger.log", "r")
    keys = json.loads(log.read())

    logFile = open("log/process.log", "a")
    print("starting simulation on "+ now.strftime("%m/%d/%Y %H:%M:%S"))
    for key in keys:
        time.sleep(sleepTime)
        now = datetime.now()
        timeNow = now.strftime("%m/%d/%Y %H:%M:%S")
        keyboard.press_and_release(key)
        logText = "on "+ timeNow +" keylogger pressed ( " + key + " )\n"
        #print(logText)
        logFile.write(logText)

    now = datetime.now()
    print("simulation ended on "+ now.strftime("%m/%d/%Y %H:%M:%S"))
    print("See log/process.log for detailed log \n\n")

print('')
while True:
    print("1.create a new simulation \n2.help \n3.Run simulation\n\n")
    choice = input("Enter your Choice: ")
    if choice == "1":
        createKeys()
    if choice == "2":
        createHelp()
    if choice == "3":
        simulate(1)