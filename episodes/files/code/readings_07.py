import sys
import pandas as pd

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['-n', '-m', '-x'], (
        'Action is not one of -n, -m, or -x: ' + action)
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)

def process(filename, action):
    data = pd.read_csv(filename, index_col='country')

    if action == '-n':
        values = data.min(axis='columns')
    elif action == '-m':
        values = data.mean(axis='columns')
    elif action == '-x':
        values = data.max(axis='columns')

    for val in values:
        print(val)

if __name__ == '__main__':
    main()
