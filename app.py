import sys
import altair as alt
import streamlit as st
from constants import *
from extractions import *
from pprint import pprint
from transformations import *
from streamlit import runtime
from collections import Counter
from streamlit.web import cli as stcli

def main():

    st.title("SBA AWARD ANALYSIS")
    
    df = reduce_data(INPUT_FILE_PATH, None, PHASE1)

    df = get_agencies_yearly_awards(df)

    df.index.name = 'Agency'

    data = df.loc[DEPARTMENTS]
    
    with st.container():
        
        st.write("Agencies & Awards (1987-2025)")
        st.bar_chart(data, horizontal=True, width=1200, height=800)
    
    st.snow()

if __name__ == "__main__":
    if runtime.exists():
        main()
    
    else:
        sys.argc = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())