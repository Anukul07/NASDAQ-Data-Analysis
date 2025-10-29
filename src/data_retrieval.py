import os, requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
API_KEY = os.getenv('NASDAQ_API_KEY')

def get_nasdaq_data(table_code='MER/F1', **kwargs):
    """
    Fetches data from Nasdaq data link API and returns a pandas DataFrame (DF).
    This function handles : 
    1. Fetching data from specified table code. 
    2. Passing extra paramets like 'ticker', 'qopts.per_page'.
    3. Parsing the JSON response. 
    4. Extracting data and column names.
    5. Creating and returning a clean DF.

    Parameters : 
    - table_code (str): The Nasdaq datatable code (e.g., 'MER/F1').
    - **kwargs: API parameters to pass in the request. Example: qopts_per_page=10000, ticker='AAPL'

    Returns : 
    - pd.DataFrame : A DF of the requested data, or None if error occurs.
    """

    if not API_KEY:
        print("API Key not found. Check .env file.")
        return None
    else:
        print("API Key loaded successfully.")

    api_url = f"https://data.nasdaq.com/api/v3/datatables/{table_code}.json"
    params = {'api_key': API_KEY}

    for key,value in kwargs.items():
        if "qopts_" in key:
            translated_key = key.replace("qopts_","qopts.")
            params[translated_key] = value
        else:
            params[key] = value
    print(f"fetching data from {api_url} with parameters : {params}")

    try:
        response = requests.get(url=api_url, params=params)
        response.raise_for_status()
        json_data = response.json()
        column_names = [col['name'] for col in json_data['datatable']['columns']]
        data = json_data['datatable']['data']
        df = pd.DataFrame(data=data, columns=column_names)
        return df
    except Exception as e:
        print(f"Error occurred : {e}")
        return None
    

        
