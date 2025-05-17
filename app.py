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
    
    df = reduce_data(INPUT_FILE_PATH, None, PHASE1)

    df = get_agencies_yearly_awards(df)

    df.index.name = 'Agency'

    Agencies = st.multiselect(
        "Choose Agencies", list(df.index), ["Department of Defense", "National Science Foundation"]
    )

    if not Agencies:
        st.error("Please Select at least one Agency")
    
    else:
        
        data = df.loc[DEPARTMENTS]
        st.subheader("Awards Per Year")

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Awards Per Year"}
        )

        pprint(data)

        # chart = (
        #     alt.Chart(data)
        #     .mark_area(opacity=0.3)
        #     .encode(
        #         x="Award Year",
        #         y="Award Amount",
        #         color="Agency:N"   
        #     )   
        # )

        # st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    if runtime.exists():
        main()
    
    else:
        sys.argc = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())