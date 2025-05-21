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

def root_project_header():
    
    st.header(":red[SBA] :blue[AWARD] ANALYSIS (1985 - 2025)", divider=True)

def root_project_description_expander():

    with st.container(border=True):

        with st.expander("What is the SBA?"):
            st.write("An Independent Agency of the United States government that provides support to entrepreneurs and small businesses")

        with st.expander("What are SBA Awards?"):
            st.write("Grants & Contracts for commercializable Research & Development ")

def get_agencies_and_awards_data():

    df = reduce_data(INPUT_FILE_PATH, None, PHASE1)

    df = get_agencies_yearly_awards(df)

    df.index.name = 'Agency'

    return df.loc[DEPARTMENTS]

def charts_tab(data):

     with st.container():

        st.write("Awards Per Year, Agencies (X, Y)")
        
        tab1, tab2= st.tabs(["Bar Chart", "Line Chart"])

        with tab1:
            st.bar_chart(data, horizontal=True, height=800)
    
        with tab2:
            st.line_chart(data, height=800)

def plot_agencies_and_awards():

    data = get_agencies_and_awards_data()
    
    charts_tab(data)
    
def main():

    root_project_header()
    root_project_description_expander()

    with st.spinner("Computing"): 
        plot_agencies_and_awards()

    st.snow()

if __name__ == "__main__":
    if runtime.exists():
        main()
    
    else:
        sys.argc = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())