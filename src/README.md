
## File List

We have multiple files in this submission.

- [load_data.py](load_data.py)

    Utility file file to load data and basic data preprocessing.

- [01_target_variable.ipynb](01_target_variable.ipynb)

    The notebook explores the target variable, `MHLTH_AdjPrev`, and its distribution across U.S. counties.

- [02_correlation.ipynb](02_correlation.ipynb)

    The notebook examines the correlation between the target variable and ACS variables.

- [03_key_independent_variables.ipynb](03_key_independent_variables.ipynb)

    The notebook identifies key independent variables that are highly correlated with the target variable.

## Data

In this project, we use PLACES and ACS (American Community Survey) datasets.
The PLACES contains the target variable, `MHLTH_AdjPrev`,
and we use the ACS profile dataset to find regional characteristics that are related to mental health across U.S. counties.

We get the data via downloading or API calls with API keys.
But this submission code retrieves the data from public GitHub repository.
It is because the data is too large to be included in the submission,
and downloading from the original source requires API keys and authentication.

### PLACES County Data (GIS Friendly Format) 2025 release

PLACES provides county-level estimates for multiple health measures across the US, including mental health status MHLTH_AdjPrev.
We just use MHLTH_AdjPrev in the PLACES dataset.

The data can be downloaded from [https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2025-releas/i46a-9kgh/about_data](https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2025-releas/i46a-9kgh/about_data) as CSV without API key.


### ACS 5-Year Data (2009-2024)

ACS provides demographic, socioeconomic, and housing information for areas across the U.S.
It contains county-level characteristics such as income, education, employment, etc.

ACS data contains several tables such as Detail Tables and Profile Tables.
Detail Tables are the original data, and Profile Tables are summarized data from Detail Tables.
We use Profile Tables.

We downloaded several JSON dataset with API keys.
There is the instruction to get API key is in [https://www.census.gov/data/developers/data-sets/acs-5year.html](https://www.census.gov/data/developers/data-sets/acs-5year.html).

- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP02)&for=country:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP03)&for=country:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP04)&for=country:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP05)&for=country:*&in=state:*&key=__YOUR_KEY__
- https://api.census.gov/data/2024/acs/acs5/profile/variables.json
