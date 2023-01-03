import streamlit as st
from catboost import CatBoostRegressor


@st.cache
def load_model() -> CatBoostRegressor:
    model = CatBoostRegressor()
    model.load_model("CatB_simple")
    
    return model