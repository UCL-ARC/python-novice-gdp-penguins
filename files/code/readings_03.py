import sys
import pandas as pd


def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = pd.read_csv(filename, index_col='country')
        for row_mean in data.mean(axis='columns'):
            print(row_mean)


if __name__ == '__main__':
    main()
