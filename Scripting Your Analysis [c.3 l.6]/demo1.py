import pandas as pd


def load_data():
    df = pd.read_csv('census_income_data.csv')
    return df


def print_columns(df):
    for column in df.columns:
        print(column)


if __name__ == '__main__':
    df = load_data()
    print_columns(df)
