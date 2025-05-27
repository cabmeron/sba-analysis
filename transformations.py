import copy
import os
import json
import jsonpickle
from models import *
from constants import *
from pprint import pprint
from pandas import DataFrame
from datetime import datetime
from dataclasses import asdict
from collections import Counter, defaultdict

#######################################
# MASTER DATA FRAME REDUCERS
#######################################

def get_agencies(df):
    agencies = set()
    for idx, series in df.iterrows():
        agencies.add(series['Agency'])
    return agencies

def iterate(df: DataFrame):
    Companies = defaultdict(list)
    for idx, series in df.iterrows():

        company = Company(
            city = series['City'],
            state = series['State'],
            name = series['Company'],
            website = series['Company Website'],
            address = series['Address1'],
            zip_code = series['Zip'],
            )
        

        pi = PI(
            name = series['PI Name'],
            phone = series['PI Phone'],
            email = series['PI Email'],
            education_level = "Unknown"
        )

        award = Award(
            pi=pi,
            phase = series['Phase'],
            agency = series['Agency'],
            program = series['Program'],
            topic_code = series['Topic Code'],
            award_title = series['Award Title'],
            award_year = series['Award Year'],
            award_amount = series['Award Amount']
        )

        Companies[company.name].append(award)

    data = jsonpickle.encode(Companies, indent=7)

    with open('./json_output.json', "w") as outfile:
        print(data, file=outfile)

#######################################
# STATISTIC AGGREGATORS FOR ALL AGENCY
#######################################

def get_agencies_female_ownership_df(df):

    res = {}

    for agency in get_agencies(df):
        
        agency_data = df.loc[df['Agency'] == agency]

        res[agency] = {
            "male_owned": get_male_owned(agency_data),
            "female_owned": get_female_owned(agency_data),
            "unknown_owned": get_unknown_owned(agency_data),
        }

    return res

def get_agency_disadvantaged_ownership_df(df):

    res = {}

    for agency in get_agencies(df):
        
        agency_data = df.loc[df['Agency'] == agency]

        res[agency] = {
            "disadvantage_owned": get_disadvantaged_owned(agency_data),
            "non_disadvtantage_owned": get_non_disadvantaged_owned(agency_data),
            "unknown_disadvantage_owned": get_unknown_disadvantaged_owned(agency_data),
        }

    return res

def get_agencies_yearly_awards(df: DataFrame, inDollars=False):

    res = {}

    df_locator = "Award Amount" if  inDollars else "Award Year"

    for agency in get_agencies(df):

        res[agency] = copy.deepcopy(AWARD_YEARS_DICT)

        agency_data = df.loc[df['Agency'] == agency]

        for year in agency_data[df_locator]:
            res[agency][year] += 1

    return DataFrame.from_dict(res).transpose()

""""""""""""""""""""""""""""""
""" STATISTICAL GENERATORS """
""""""""""""""""""""""""""""""
def get_prinicpial_investigators(df):
    pis = Counter(df['PI Name'])
    del pis['  ']
    return list(pis.most_common(len(pis)))

def get_companies_awarded(df):
    companies_awarded = Counter(df['Company']).most_common(len(df['Company']))
    return list(companies_awarded)

def get_awards_per_year(df):
    awards_per_year = Counter(df['Award Year']).most_common(len(df['Award Year']))
    return list(awards_per_year)

def get_male_owned(df):
    total_owned = len(df['Woman Owned'])
    woman_owned_n = len(df.loc[df['Woman Owned'] == 'N'])
    return (woman_owned_n / total_owned) * 100

def get_female_owned(df):
    total_owned = len(df['Woman Owned'])
    woman_owned_y = len(df.loc[df['Woman Owned'] == 'Y'])
    return (woman_owned_y / total_owned) * 100

def get_unknown_owned(df):
    total_owned = len(df['Woman Owned'])
    woman_owned_u = len(df.loc[df['Woman Owned'] == 'U'])
    return (woman_owned_u / total_owned) * 100

def get_disadvantaged_owned(df):
    total_owned = len(df['Socially and Economically Disadvantaged'])
    disadvantaged_y = len(df.loc[df['Socially and Economically Disadvantaged'] == 'Y'])
    return (disadvantaged_y / total_owned) * 100

def get_non_disadvantaged_owned(df):
    total_owned = len(df['Socially and Economically Disadvantaged'])
    disadvantaged_n = len(df.loc[df['Socially and Economically Disadvantaged'] == 'N'])
    return (disadvantaged_n / total_owned) * 100

def get_unknown_disadvantaged_owned(df):
    total_owned = len(df['Socially and Economically Disadvantaged'])
    disadvantaged_u = len(df.loc[df['Socially and Economically Disadvantaged'] == 'U'])
    return (disadvantaged_u / total_owned) * 100

