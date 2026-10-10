# UoM SIADS539 Submission

This is the submission for SIADS539 course at University of Michigan.

## File List

We have multiple files in this submission.

- [README.md](README.md)

    This file.

- [requirements.txt](requirements.txt)

    The file contains the list of required packages to run the code.

- [load_data.py](load_data.py)

    Utility file to load data and basic data preprocessing.

- [01_target_variable.ipynb](01_target_variable.ipynb)

    The notebook explores the target variable, `MHLTH_AdjPrev`, and its distribution across U.S. counties.

- [02_correlation.ipynb](02_correlation.ipynb)

    The notebook examines the correlation between the target variable and ACS variables.

- [03_key_independent_variables.ipynb](03_key_independent_variables.ipynb)

    The notebook identifies key independent variables that are highly correlated with the target variable.

- [data/PLACES__County_Data_(GIS_Friendly_Format),_2025_release_20260905.csv](data/PLACES__County_Data_(GIS_Friendly_Format),_2025_release_20260905.csv)

    The PLACES dataset in CSV format.

- [data/variables.json](data/variables.json)

    The ACS variable metadata in JSON format.

- [data/ACS_feature_cluster.tsv](data/ACS_feature_cluster.tsv)

    The ACS variable cluster information in TSV format.
    The cluster information is manually assigned based on the ACS variable metadata.

## Data

In this project, we use PLACES and ACS (American Community Survey) datasets.
The PLACES contains the target variable, `MHLTH_AdjPrev`,
and we use the ACS profile dataset to find regional characteristics that are related to mental health across U.S. counties.

All data is publicly accessible and we got the data via downloading or API calls with API keys.
In this submission code retrieves the ACS data from our public GitHub repository.
It is because the data is too large to be included in the submission,
and API calls require API keys and authentication.
In addition, the original data sources may change over time, which can break the code.

Original data sources are explained below.

### PLACES County Data (GIS Friendly Format) 2025 release

PLACES provides county-level estimates for multiple health measures across the US, including mental health status `MHLTH_AdjPrev`.
We just use MHLTH_AdjPrev in the PLACES dataset.

The data can be downloaded from [https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2025-releas/i46a-9kgh/about_data](https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2025-releas/i46a-9kgh/about_data) as CSV.


### ACS 5-Year Data (2009-2024)

ACS provides demographic, socioeconomic, and housing information for areas across the U.S.
It contains county-level characteristics such as income, education, employment, etc.

ACS data contains several tables such as Detail Tables and Profile Tables.
Detail Tables are the original data, and Profile Tables are summarized data from Detail Tables.
We use Profile Tables.

We downloaded several JSON dataset with API keys.
There is the instruction to get API key is in [https://www.census.gov/data/developers/data-sets/acs-5year.html](https://www.census.gov/data/developers/data-sets/acs-5year.html).

We used the following API calls to get the data.

- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP02)&for=county:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP03)&for=county:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP04)&for=county:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP05)&for=county:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile/variables.json
