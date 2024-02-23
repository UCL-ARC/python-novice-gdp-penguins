import sys
import pandas as pd

def main():
    script = sys.argv[0]
    if len(sys.argv) == 1:  # no arguments, so print help message
        print("Usage: python readings_08.py action filenames\n"
              "Action:\n"
              "    Must be one of --min, --mean, or --max.\n"
              "Filenames:\n"
              "    If blank, input is taken from standard input (stdin).\n"
              "    Otherwise, each filename in the list of arguments is processed in turn.")
        return

    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], (
        'Action is not one of --min, --mean, or --max: ' + action)
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)

def process(filename, action):
    data = pd.read_csv(filename, index_col='country')

    if action == '--min':
        values = data.min(axis='columns')
    elif action == '--mean':
        values = data.mean(axis='columns')
    elif action == '--max':
        values = data.max(axis='columns')

    for val in values:
        print(val)

if __name__ == '__main__':
    main()
