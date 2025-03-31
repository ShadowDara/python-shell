# script written by Shadowdara

# built in vars for Shell
shell_types = ["echo", "exit", "type"]

import os
import sys
import shutil
import subprocess
import shlex

def findExecutable(command):
    paths = os.getenv("PATH", "").split(os.pathsep)
    for path in paths:
        executablePath = os.path.join(path, command)
        if os.path.isfile(executablePath):
            return executablePath
    return None

def main():
    while True:
        spam = input("$ ")
        if spam == 'exit 0':
            sys.exit(0)

        elif spam[0:4] == 'type':
            if spam[5:] in shell_types:
                print(f"{spam[5:]} is a shell builtin")
            elif path := shutil.which(spam[5:]):
                    print(f"{spam[5:]} is {path}")
            else:
                print(f"{spam[5:]}: not found")

        elif spam[0:4] == "echo":
            parsed_args = shlex.split(spam[5:].strip())
            output = " ".join(parsed_args)
            print(output)

        else:
            args = shlex.split(spam)
            executablePath = findExecutable(args[0])
            if executablePath:
                result = subprocess.run(args, capture_output=True, text=True)
                print(result.stdout, end="")
            else:
                print(f"{spam}: command not found")

if __name__ == "__main__":
    #print("Custom Shell Terminal in Python by Shadowdara\n")
    main()
