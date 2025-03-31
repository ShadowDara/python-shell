# script written by Shadowdara

# built in vars for Shell
shell_types = ["echo", "exit", "type"]
s_path = ["ls", "valid_command"]
s_relative_path = ["/usr/bin/ls", "/usr/local/bin/valid_command"]

import sys

def main():
    while True:
        spam = input("$ ")
        if spam == 'exit 0':
            sys.exit(0)
        elif spam[0:4] == 'type':
            if spam[5:] in shell_types:
                print(f"{spam[5:]} is a shell builtin")
            elif spam[5:] in s_path:
                index = s_path.index(spam[5:])
                print(f"{spam[5:]} is {s_relative_path[index]}")
            else:
                print(f"{spam[5:]}: not found")
        elif spam[0:4] == "echo":
            print(spam[5:])
        else:
            print(f"{spam}: command not found")

if __name__ == "__main__":
    main()
