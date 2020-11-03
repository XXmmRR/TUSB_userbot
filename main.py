import os
import subprocess
import sys
import time

def picture():
    print('████████╗██╗░░░██╗░██████╗██████╗░')
    time.sleep(0.5)
    print('╚══██╔══╝██║░░░██║██╔════╝██╔══██╗')
    time.sleep(0.5)
    print('░░░██║░░░██║░░░██║╚█████╗░██████╦╝')
    time.sleep(0.5)
    print('░░░██║░░░██║░░░██║░╚═══██╗██╔══██╗')
    time.sleep(0.5)
    print('░░░██║░░░╚██████╔╝██████╔╝██████╦╝')
    time.sleep(0.5)
    print('░░░╚═╝░░░░╚═════╝░╚═════╝░╚═════╝░  by XXmmRR')
picture()

print("Нажми Enter чтобы запустить...")
input()

while (True):
    process = subprocess.Popen([sys.executable, "tusb.py"])
    process.wait()
