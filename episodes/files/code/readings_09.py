import sys
import pandas as pd

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    if action not in ['--min', '--mean', '--max']:  # if no action given
        action = '--mean'  # set a default action, that being mean
        # start the filenames one place earlier in the argv list
        filenames = sys.argv[1:]
    else:
        filenames = sys.argv[2:]

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
