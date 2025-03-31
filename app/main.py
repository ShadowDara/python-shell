# script written by Shadowdara

import sys

def main():
    while True:
        spam = input("$ ")
        if spam == 'exit 0':
            sys.exit(0)
        elif spam.startswith("echo "):
            print(spam[5:])
        else:
            print(f"{spam}: command not found")

if __name__ == "__main__":
    main()
