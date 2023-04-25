import os
import sys

os.system('cls')
while True:
    # print without new line
    sys.stdout.write(os.path.abspath(__file__))
    sys.stdout.write(">")
    a = input("")
    if a == "cd ..":
        sys.stdout.write('Are you stupid?\n')
