import pandas as pd

def search_name(name:str, data:pd.DataFrame = "./data/dbpedia.csv") -> pd.DataFrame:
    """
    Search for a name in the dbpedia_data DataFrame

    Args:
        name (str): The name to search for

    Returns:
        pd.DataFrame: A DataFrame containing the search results
    """
    
    df = pd.read_csv(data)

    return df[df['name'].str.contains(name)]
