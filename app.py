import streamlit as st
import pandas as pd

health_problems = pd.read_csv("health problems.csv", sep=';', encoding='utf-8')
phrases = pd.read_csv("phrases.csv", sep=';', encoding='utf-8')

doctors = ["Dentysta", "Laryngolog", "Okulista", "Ortopeda", "Psychiatra"]

sellected_doctor = st.selectbox(
    "Wybierz lekarza specjalistę",
    doctors
)

problems = health_problems.loc[health_problems['Doctor'] == sellected_doctor, 'Problems_PL'].tolist()

health_problem = st.selectbox(
    "Wybierz problem zdrowotny",
    problems
)

form_help = phrases[phrases['Problem'] == health_problem]


for index, row in form_help.iterrows():
    phrase_de = row['Phrase_DE']
    phrase_pl = row['Phrase_PL']
    st.markdown(
            f"""
            <p style='color:navy; font-size:24px; text-align:left; font-weight:bold;'>
                {phrase_de}
            </p>
            <p style='color:black; font-style:italic; font-size:18px; text-align:left; margin-top:-10px;'>
                {phrase_pl}
            </p>
            """,
            unsafe_allow_html=True
        )