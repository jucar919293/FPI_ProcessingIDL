from FPIplot.utils import get_dateformat
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

year = 2015
month = 6
data_path_results = "Data2plot/2015/"
days = [i for i in range(1, 7)] + [n for n in range(9, 31)]


def preprocess_data(path):
    dic = []
    li = []
    dframe = pd.read_csv(path)
    angle1 = dframe.iloc[0, 4]
    angle2 = dframe.iloc[0, 5]
    count = 0
    for i in range(dframe.shape[0]):
        if angle1 == dframe.iloc[i, 4] and angle2 == dframe.iloc[i, 5]:
            li.append(i)
        else:
            angle1 = dframe.iloc[i, 4]
            angle2 = dframe.iloc[i, 5]
            dic.append(dframe.loc[li])
            li = []
            count = count + 1
            li.append(i)
    dic.append(dframe.loc[li])
    return dic


if __name__ == '__main__':
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    fig, ax = plt.subplots()
    ax.set_ylim((-150, 300))
    # ax.set_xlim((18, 21))
    for day in days:
        temporal_date = get_dateformat(year, month, day, "%Y%m%d")
        data_path_open_file = data_path_results + temporal_date + '.csv'
        dic = preprocess_data(data_path_open_file)
        print(data_path_open_file)
        for mode, color in zip(dic, colors):
            ax.scatter(mode.iloc[:, 0], mode.iloc[:, 1], s=5, c=color)

    ax.legend()
    ax.grid(True)
    plt.show()

