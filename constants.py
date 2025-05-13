PHASE1 = "Phase I"
PHASE2 = "Phase II"
ALL_PHASE = "Phase"

PROGRAM_SBIR = "SBIR"
PROGRAM_STTR = "STTR"
ALL_PROGRAMS = "Programs"

OUTPUT_FILE_PATH = './out/csv'
INPUT_FILE_PATH = './award_data_no_abstract.csv'

DEPARTMENTS = [
    "NASA",
    "NATIONAL SCIENCE FOUNDATION",
    "NUCLEAR REGULATORY COMMISSION",
    "ENVIRONMENTAL PROTECTION AGENCY"
    "DEPARTMENT OF ENERGY",
    "DEPARTMENT OF DEFENSE",
    "DEPARTMENT OF COMMERCE",
    "DEPARTMENT OF EDUCATION",
    "DEPARTMENT OF AGRICULTURE",
    "DEPARTMENT OF THE INTERIOR",
    "DEPARTMENT OF TRANSPORTATION",
    "DEPARTMENT OF HOMELAND SECURITY",
    "DEPARTMENT OF HEALTH AND HUMAN SERVICES",
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