import os
import csv
import pandas as pd
from datetime import datetime
from constants import OUTPUT_FILE_PATH

def write_csv(res: dict):
    
    write_time = datetime.now()

    if not os.path.exists(OUTPUT_FILE_PATH):
        os.makedirs(OUTPUT_FILE_PATH)
    
    try:
        df = pd.DataFrame.from_dict(res)
        df.to_csv(f'{OUTPUT_FILE_PATH}/{write_time}.csv')

    except:
        ChildProcessError
