import sys

def main():
    script = sys.argv[0]
    arguments = sys.argv[1:]
    if len(arguments) >= 1:
        print('Thanks for specifying argument')
    else:
        print('usage: python check_argument.py filename.txt')
        sys.exit()

if __name__ == '__main__':
    main()
