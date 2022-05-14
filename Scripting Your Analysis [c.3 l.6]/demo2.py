import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


def load_data():
    df = pd.read_csv('census_income_data.csv')
    return df


def plot_hist(arr1, arr2, label1, label2):
    plt.hist(arr1, color='r', alpha=0.5, label=label1)
    plt.hist(arr2, color='b', alpha=0.5, label=label2)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    df = load_data()
    below = df.query('income == " <=50K"')
    above = df.query('income == " >50K"')
    plot_hist(below.age, above.age, '<=50K', '>50K')
