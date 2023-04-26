import os
import sys
import subprocess

# answer sheet
responsDict = {}
with open('responses.txt', 'r') as f:
    responses = f.readlines()
    for response in responses:
        response = response.strip()
        if response != '':
            responsDict[response.split(':')[0]] = response.split(':')[1]
    print(responsDict)

os.system('cls')
while True:
    # print without new line
    sys.stdout.write(os.path.abspath(__file__))
    sys.stdout.write(">")
    a = input("")
    cmd = a.split(" ")
    if cmd[0] == "exit":
        break

    run = subprocess.run(["cd", ".."], capture_output=True, shell=True)

    print(run.stdout) # the output "Test"
    print(run.stderr) # the error part of the output

    
