import pandas as pd

GITHUB_BASE_URL = "https://github.com/KenjiOhtsuka/UoM_SIADS593_submission/raw/refs/heads/main/src/data/"

def load_acs_profile(label: str) -> pd.DataFrame:
    """Load ACS Detail Profile data from a JSON file and preprocess it.
    
    INPUTS:
        label: str, the label of the ACS Detail Profile data to load (e.g., 'DP02', 'DP03', etc.)
    OUTPUTS:
        pd.DataFrame: The preprocessed ACS Detail Profile data.
    """
    url = f"{GITHUB_BASE_URL}{label}.json"
    df = pd.read_json(url)
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)
    df['CountyFIPS'] = df['state'] + df['county']
    PE_cols = [col for col in df.columns if col.endswith('PE')]
    for col in PE_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def load_places() -> pd.DataFrame:
    """Load Places data from a CSV file and preprocess it."""
    url = f"{GITHUB_BASE_URL}PLACES__County_Data_(GIS_Friendly_Format),_2025_release_20260905.csv"
    df = pd.read_csv(url, dtype={'CountyFIPS': str})
    df['CountyFIPS'] = df['CountyFIPS'].str.zfill(5)
    # We don't use the population columns in this project, but if you want to use them,
    # you can uncomment the following lines to convert them to integers
    # df['TotalPopulation'] = df['TotalPopulation'].str.replace(',', '').astype(int)
    # df['TotalPop18plus'] = df['TotalPop18plus'].str.replace(',', '').astype(int)
    return df

def load_acs_profiles() -> pd.DataFrame:
    """Load ACS Profile data from a CSV file and preprocess it."""
    df2 = load_acs_profile('DP02')
    df3 = load_acs_profile('DP03')
    df4 = load_acs_profile('DP04')
    df5 = load_acs_profile('DP05')
    merged_df = df2.merge(df3, on='CountyFIPS', how='outer', suffixes=('_DP02', '_DP03'))
    merged_df = merged_df.merge(df4, on='CountyFIPS', how='outer', suffixes=('', '_DP04'))
    merged_df = merged_df.merge(df5, on='CountyFIPS', how='outer', suffixes=('', '_DP05'))
    return merged_df

def load_acs_cluster() -> pd.DataFrame:
    """Load ACS Cluster data from a CSV file and preprocess it."""
    url = f"{GITHUB_BASE_URL}ACS features - correlations.tsv"
    url = url.replace(" ", "%20")
    df = pd.read_csv(url, sep='\t')
    return df[['Column Name', 'cluster', 'subcluster']]
    
def load_acs_vars() -> pd.DataFrame:
    """Load ACS Data Profile variable metadata from a JSON file.
    
    OUTPUTS:
        pd.DataFrame: The ACS Data Profile variable metadata.
    """
    df = pd.read_json(
        f"{GITHUB_BASE_URL}variables.json"
    )
    return df
