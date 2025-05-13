import csv
import heapq
from load import *
import pandas as pd
from models import *
from constants import *
from pprint import pprint
from extractions import *
from transformations import *
from datetime import datetime
from collections import defaultdict, Counter

def extract():
    return reduce_data(None, reduce_data(INPUT_FILE_PATH, None, PHASE1), PROGRAM_SBIR)

def transform(df):
    return iterate(df)

def load(res):
    write_csv(res)

def main():
    res = transform(extract())
    
if __name__ == "__main__":
    main()
