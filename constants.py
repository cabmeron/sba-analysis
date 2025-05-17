PHASE1 = "Phase I"
PHASE2 = "Phase II"
ALL_PHASE = "Phase"

PROGRAM_SBIR = "SBIR"
PROGRAM_STTR = "STTR"
ALL_PROGRAMS = "Programs"

OUTPUT_FILE_PATH = './out/csv'
INPUT_FILE_PATH = './inp/award_data_no_abstract.csv'

DEPARTMENTS = [
    "Department of Education",
    "Department of Commerce",
    "Department of Energy",
    "Department of Defense",
    "Department of Agriculture",
    "Department of the Interior",
    "National Science Foundation",
    "Environmental Protection Agency",
    "Department of Homeland Security",
    "Department of Transportation",
    "Nuclear Regulatory Commission",
    "Department of Health and Human Services",
    "National Aeronautics and Space Administration",
]

STATES_STATS = {
    "total_awards": 0,
    "total_companies": 0,
}

US_STATES_DICT = {
    "Alabama": STATES_STATS,
    "Alaska": STATES_STATS,
    "Arizona": STATES_STATS,
    "Arkansas": STATES_STATS,
    "California": STATES_STATS,
    "Colorado": STATES_STATS,
    "Connecticut": STATES_STATS,
    "Delaware": STATES_STATS,
    "Florida": STATES_STATS,
    "Georgia": STATES_STATS,
    "Hawaii": STATES_STATS,
    "Idaho": STATES_STATS,
    "Illinois": STATES_STATS,
    "Indiana": STATES_STATS,
    "Iowa": STATES_STATS,
    "Kansas": STATES_STATS,
    "Kentucky": STATES_STATS,
    "Louisiana": STATES_STATS,
    "Maine": STATES_STATS,
    "Maryland": STATES_STATS,
    "Massachusetts": STATES_STATS,
    "Michigan": STATES_STATS,
    "Minnesota": STATES_STATS,
    "Mississippi": STATES_STATS,
    "Missouri": STATES_STATS,
    "Montana": STATES_STATS,
    "Nebraska": STATES_STATS,
    "Nevada": STATES_STATS,
    "New Hampshire": STATES_STATS,
    "New Jersey": STATES_STATS,
    "New Mexico": STATES_STATS,
    "New York": STATES_STATS,
    "North Carolina": STATES_STATS,
    "North Dakota": STATES_STATS,
    "Ohio": STATES_STATS,
    "Oklahoma": STATES_STATS,
    "Oregon": STATES_STATS,
    "Pennsylvania": STATES_STATS,
    "Rhode Island": STATES_STATS,
    "South Carolina": STATES_STATS,
    "South Dakota": STATES_STATS,
    "Tennessee": STATES_STATS,
    "Texas": STATES_STATS,
    "Utah": STATES_STATS,
    "Vermont": STATES_STATS,
    "Virginia": STATES_STATS,
    "Washington": STATES_STATS,
    "West Virginia": STATES_STATS,
    "Wisconsin": STATES_STATS,
    "Wyoming": STATES_STATS
}

US_STATES_LIST = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

AWARD_YEARS = list(range(1983,2026))

AWARD_YEARS_DICT = {
    1983: 0,
    1984: 0,
    1985: 0,
    1986: 0,
    1987: 0,
    1988: 0,
    1989: 0,
    1990: 0,
    1991: 0,
    1992: 0,
    1993: 0,
    1994: 0,
    1995: 0,
    1996: 0,
    1997: 0,
    1998: 0,
    1999: 0,
    2000: 0,
    2001: 0,
    2002: 0,
    2003: 0,
    2004: 0,
    2005: 0,
    2006: 0,
    2007: 0,
    2008: 0,
    2009: 0,
    2010: 0,
    2011: 0,
    2012: 0,
    2013: 0,
    2014: 0,
    2015: 0,
    2016: 0,
    2017: 0,
    2018: 0,
    2019: 0,
    2020: 0,
    2021: 0,
    2022: 0,
    2023: 0,
    2024: 0,
    2025: 0,

}