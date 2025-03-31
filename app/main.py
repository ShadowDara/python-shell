# script written by Shadowdara

shell_types = ["echo", "exit", "type"]

import sys

def main():
    while True:
        spam = input("$ ")
        if spam == 'exit 0':
            sys.exit(0)
        elif spam[0:4] == 'type':
            if spam[5:] in shell_types:
                print(f"{spam[5:]} is a shell builtin")
            else:
                print(f"{spam[5:]}: not found")
        elif spam[0:4] == "echo":
            print(spam[5:])
        else:
            print(f"{spam}: command not found")

if __name__ == "__main__":
    main()
