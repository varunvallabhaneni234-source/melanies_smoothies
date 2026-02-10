import streamlit as st
import pandas as pd
import requests
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


smoothiefroot_response = requests.get(
    "https://my.smoothiefroot.com/api/fruit/watermelon"
)

st.text(smoothiefroot_response)

sf_json = smoothiefroot_response.json()
st.json(sf_json)

sf_df = pd.DataFrame([sf_json])
st.dataframe(sf_df)
