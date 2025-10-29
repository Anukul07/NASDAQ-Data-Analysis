import pandas as pd

def clean_turnover_data(df):
    """Cleans the filtered 'Accrued Expenses Turnover' DataFrame.
    
    This function performs several cleaning steps:
    1. Converts 'reportdate' from an object to a datetime.
    2. Drops the confusing 'region' column due to USA/Europe issue.
    3. Renames 'longname' and 'country' for clarity.
    4. Maps country codes to full country name.

    Args:
        df (pd.DataFrame): The filtered DataFrame containing 'Accrued Expenses Turnover' data.

    Returns:
        pd.DataFrame: A cleaned and ready-for-analysis DataFrame.
    """
    
    df_clean = df.copy()
    df_clean['reportdate'] = pd.to_datetime(df_clean['reportdate'])    
    df_clean = df_clean.drop(columns=['region'])
    df_clean = df_clean.rename(columns={
        'longname': 'company_name',
        'country': 'country_code'
    })
    country_mapping = {
        'USA': 'United States',
        'DEU': 'Germany',
        'JPN': 'Japan',
        'CYM': 'Cayman Islands',
        'BHS': 'Bahamas',
        'IRL': 'Ireland'
    }
    df_clean['country_name'] = df_clean['country_code'].map(country_mapping)
    df_clean['country_name'] = df_clean['country_name'].fillna('Other')
    return df_clean

