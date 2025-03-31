# script written by Shadowdara

# built in vars for Shell
shell_types = ["echo", "exit", "type"]

import sys
import shutil
import subprocess
import shlex

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
            if spam[5] and spam[-1] == "'":
                print(" ".join(spam[6:-1].split()))
            else:
                parts = shlex.split(spam[5:])
                print(" ".join(parts))
        elif spam[0:3] == 'cat':
            pass
        else:
            try:
                subprocess.run([spam.split(" ")[0], spam.split(" ", 1)[1]], check=True)
            except:
                print(f"{spam}: command not found")

if __name__ == "__main__":
    #print("Custom Shell Terminal in Python by Shadowdara\n")
    main()
