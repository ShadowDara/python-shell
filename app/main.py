import sys

def main():
    while True:
        spam = input("$ ")
        if spam == 'exit 0':
            sys.exit
        else:
            print(f"{spam}: command not found")

if __name__ == "__main__":
    main()
