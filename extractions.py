import pandas as pd

"""
    EXTRACTION GOALS:
    * Identify All Departments
    * Extract Data Per Department
"""

"""
    Read CSV into Memory
"""
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except:
        return FileNotFoundError

"""
    Reduce Data Frame via Label-Based Data Selection
"""
def reduce_data(file_path, df, function):
    
    if df is None and file_path:
        df: pd.DataFrame = load_data(file_path)

    match function:

        case "Phase":
            return get_phase(df)
    
        case "Phase I":
            return get_phase(df, "Phase I")
    
        case "Phase II":
            return get_phase(df, "Phase II")
        
        case "Programs":
            return get_program(df)
        
        case "SBIR":
            return get_program(df, "SBIR")
    
        case "STTR":
            return get_program(df, "STTR")
        
"""
    Return PHASE 1, PHASE 2, or BOTH
"""
def get_phase(df: pd.DataFrame, phase=None):
              
    if phase is None:
        return df
        
    else:
        return df.loc[df['Phase'] == phase]

"""
    Return SBIR, STTR, or BOTH
"""
def get_program(df: pd.DataFrame, program=None):
    
    if program:
        return df.loc[df['Program'] == program]
    
    else:
        return df