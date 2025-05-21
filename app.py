import sys
import time
import altair as alt
import streamlit as st
from constants import *
from extractions import *
from pprint import pprint
from transformations import *
from streamlit import runtime
from collections import Counter
from streamlit.web import cli as stcli

def get_agencies_and_awards_data():

    
    df = reduce_data(INPUT_FILE_PATH, None, PHASE1)

    df = get_agencies_yearly_awards(df)

    df.index.name = 'Agency'

    return df.loc[DEPARTMENTS]

def plot_agencies_and_awards():

    data = get_agencies_and_awards_data()

    with st.container():

        st.write("Agencies & Awards Per Year (X, Y)")
        
        tab1, tab2 = st.tabs(["Bar Chart", "Line Chart"])

        with tab1:
            st.bar_chart(data, horizontal=True, height=800)
    
        with tab2:
            st.line_chart(data, height=800)


def main():
    st.header(":red[SBA] :blue[AWARD] ANALYSIS (1985 - 2025)", divider=True)
    with st.spinner("Computing"):
        plot_agencies_and_awards()
    st.snow()

if __name__ == "__main__":
    if runtime.exists():
        main()
    
    else:
        sys.argc = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())