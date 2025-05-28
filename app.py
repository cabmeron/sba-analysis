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
    
    st.header(":red[SBA] :blue[AWARD] ANALYSIS 1983-2025", divider=True)

def root_project_description_expander():

    with st.container(border=True):

        st.write("Frequently Asked Questions")

        with st.expander("What is the SBA?", expanded=True):
            st.write("An Independent Agency of the United States government that provides support to entrepreneurs and small businesses")

        with st.expander("What are SBA Awards?", expanded=True):
            st.write("Grants & Contracts for commercializable Research & Development ")

def get_agencies_and_awards_data():

    df = reduce_data(INPUT_FILE_PATH, None, PHASE1)

    df = get_agencies_yearly_awards(df)

    df.index.name = 'Agency'

    return df.loc[DEPARTMENTS]

def get_absent_pi_awards_per_department():

    df = reduce_data(INPUT_FILE_PATH, None, PHASE1)

    return get_agency_absentee_pi_awards(df)

@st.cache_data
def render_top_awardees_dataframe():

    df = reduce_data(INPUT_FILE_PATH, None, PHASE1)

    top_awardees_data = get_agency_top_awardees(df)

    null_pi_awards_per_agency_data, percent_undefined_data = get_absent_pi_awards_per_department()

    with st.container():

        st.header("SBIR PHASE 1: Most Awarded PI's")

        st.dataframe(top_awardees_data)

        st.subheader("Who is awarding undefined PI's?")

        st.bar_chart(null_pi_awards_per_agency_data)

        st.subheader("What % of their awards does this represent?")

        st.bar_chart(percent_undefined_data)


@st.cache_data
def render_agencies_awards_per_year_charts_tab():
     
     data = get_agencies_and_awards_data()

     with st.container():

        st.header("SBIR PHASE 1: Awards per Agency")
        
        tab1, tab2= st.tabs(["Bar Chart", "Line Chart"])

        with tab1:
            
            st.bar_chart(data, horizontal=True, height=800)
    
        with tab2:
            st.line_chart(data, height=800)

@st.cache_data
def render_dei_bar_charts():

    data = [
        DataFrame.from_dict(get_agencies_female_ownership_df(reduce_data(INPUT_FILE_PATH, None, PHASE1))).transpose(),
        DataFrame.from_dict(get_agency_disadvantaged_ownership_df(reduce_data(INPUT_FILE_PATH, None, PHASE1))).transpose()
    ]

    with st.container():

        st.header("SBIR PHASE 1: Awards for DEI")

        tab1, tab2 = st.tabs(["Gender", "Economic Advantage"])

        with tab1:
            st.bar_chart(data[0], horizontal=True, height=800)
        
        with tab2:

            st.bar_chart(data[1], horizontal=True, height=800)
        

def plot_agencies_and_awards():

    with st.expander('SBIR PHASE 1: Awards Per Agency ', expanded=True):

        render_agencies_awards_per_year_charts_tab()

    with st.expander('SBIR PHASE 1: DEI Award Distribtions Per Agency', expanded=True):

        render_dei_bar_charts()
    
    with st.expander('SBIR PHASE 1: Top Awardees', expanded=True):

        render_top_awardees_dataframe()
        
def main():

    root_project_header()
    root_project_description_expander()    
    plot_agencies_and_awards()

    st.snow()

if __name__ == "__main__":
    if runtime.exists():
        main()
    
    else:
        sys.argc = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())