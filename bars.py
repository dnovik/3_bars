import json
import pandas as pd
import numpy as np


def load_data(file_name):
    string_container = []
    open_file = open(file_name, encoding='utf-8').read()
    json_data = json.loads(open_file)

    for line in json_data['features']:
        latitude = line['geometry']['coordinates'][0]
        longitude = line['geometry']['coordinates'][1]
        size = line['properties']['Attributes']['SeatsCount']
        names = line['properties']['Attributes']['Name']
        adress = line['properties']['Attributes']['Address']
        data_string = names, adress, latitude, longitude, size
        string_container.append(data_string)

    df = pd.DataFrame(data, columns=[
        'Name', 'Address', 'Latitude', 'Longtitude', 'Size'])

    return df


def get_biggest_bar(df):
    return df[df['Size'] == max(
        df['Size'])]['Name'].to_string(index=False, header=False)


def get_smallest_bar(df):
    return df[df['Size'] == min(
        df['Size'])]['Name'].to_string(index=False, header=False)


def closest_bar(df, My_Longtitude, My_Latitude):
    df['Distance'] = np.sqrt(((
        df['My_Latitude'] - df['Longtitude'])**2) + ((
            df['My_Longtitude'] - df['Latitude'])**2))
    return df.loc[df['Distance'] == min(
        df['Distance'])]['Name'].to_string(index=False, header=False)


if __name__ == '__main__':
    pass
