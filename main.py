from datetime import datetime
import pandas as pd
import numpy as np

# Temporal date to test
year = 2015
month = 6
day = 1

data_path_save = "Data2plot/2015/"

def select_data():

    # Create variables
    time_column = []
    winds_column = []
    temps_column = []
    intensity_column = []
    angle1_column = []
    angle2_column = []
    # Calculating path
    actual_day = datetime(year, month, day)
    temporal_date = actual_day.strftime("%Y%m%d")
    temporal_date_file = actual_day.strftime("%d%m%Y")
    temporal_file = "MRH" + temporal_date_file + "_LOS_Laser(Weighted average).txt"
    path_data = "./" + str(year) + "/" + temporal_date + "/" + temporal_file

    with open(path_data) as f:
        # Reading lines
        contents = f.readlines()
        for line in contents[2:]:
            time_column.append(float(line[4:11]))
            winds_column.append(float(line[16:22]))
            temps_column.append(float(line[37:44]))
            intensity_column.append(float(line[59:66]))
            angle1_column.append(float(line[79:84]))
            angle2_column.append(float(line[86:91]))

        # Creating dataframe
        df = pd.DataFrame(np.array([time_column,
                                   winds_column,
                                   temps_column,
                                   intensity_column,
                                   angle1_column,
                                   angle2_column]),
                          index=['times', 'winds', 'temps', 'intensity', 'angle1', 'angle2']).transpose()
        data_path_save_file = data_path_save + temporal_date + '.csv'
        df.to_csv(data_path_save_file,index=False)
        print(df)


if __name__ == '__main__':
    select_data()
