import pandas as pd

from dataCollections import Leagues as L

def get_data(league):
    """
    Gets the fantasy data for the league

    Parameters: 
        league - sports league to analyze data
    Returns:
        df - pandas dataframe 
    """
    if L.Leagues[league]['supported']:
        df = pd.read_csv(f'data/nfl/2022.csv')
        print(f'Data for {league.upper()} successfully imported.')
        return df
    else:
        print(f'WARNING: {league.upper()} is not supported yet.')