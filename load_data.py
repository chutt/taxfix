# -*- coding: utf-8 -*-

import database
import yaml
import requests
import pandas as pd


def load(db_name):
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    url = config['url']
    folder_list = config['folder']
    for folder in folder_list:
        r = requests.get(f'{url}/{folder}')
        data = r.json()
        df = pd.DataFrame(data)
        #We could add here a dwh_created column to track the records loading date
        if df.empty:
            print(f'The folder {folder} is empty. No data to be loaded.')
            #We could also add some logging here to save the prints into a log file
            continue
        else:
            conn = database.get_connection(db_name)
            try:
                df.to_sql(folder, conn)
                print(f'The folder {folder} has been loaded in {db_name} database')
            except ValueError:
                print(f'The folder {folder} has already been loaded in {db_name} database')
                continue


load(db_name='main')

