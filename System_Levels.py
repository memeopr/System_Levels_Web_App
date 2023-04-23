import streamlit as st
import functions as fu
import pandas as pd


def plot_levels():
    x, y = fu.system_levels2(float(HF), float(HFL), float(LF), float(LFL), SPLIT)
    df = pd.DataFrame(list(zip(x, y)), columns=["Frequency (MHz)", "Level (dBmV)"])
    with col2:
        st.subheader(":blue[_System Levels vs Frequency_]")
        st.bar_chart(df, width=640, height=500, x="Frequency (MHz)", y="Level (dBmV)")
        st.info(f"Total Power is :green[{fu.total_power(y)}] dBmV")


st.set_page_config(page_title="System Levels", layout="wide")
st.title("System Levels")
st.subheader(":green[ A CATV system levels calculator web app]")
st.divider()
col1, col2 = st.columns(2)


with col1:
    HF = st.text_input("Enter High Pilot Frequency (MHz)", key="HF", value=1218)
    HFL = st.text_input("Enter High Pilot Level (dBmV)", key="HFL", value=52)
    st.divider()
    LF = st.text_input("Enter Low Pilot Frequency (MHz)", key="LF", value=54)
    LFL = st.text_input("Enter Low Pilot Level (dBmV)", key="LFL", value=35)
    SPLIT = st.selectbox("Select Split", options=["Low", "Mid", "High"], key="SPLIT")
    Calc = st.button("Plot", key='calculate', on_click=plot_levels)

st.divider()
st.subheader(":green[Find Frequency]")
FIND_FQ = st.text_input("Enter Frequency (MHz)", key="FIND_FQ")
try:
    st.info(f"Level at {FIND_FQ} MHz is:     :green[{fu.mystery_freq2(float(HF), float(HFL), float(LF), float(LFL), float(FIND_FQ), SPLIT)[1]}] dBmV")
except ValueError:
    pass

st.divider()
st.subheader(":green[Find Tilt]")
FIND_LP = st.text_input("Enter Low Pilot (MHz)", key="FIND_LP")
FIND_HP = st.text_input("Enter High Pilot (MHz)", key="FIND_HP")
try:
    tilt = fu.mystery_freq2(float(HF), float(HFL), float(LF), float(LFL), float(FIND_HP), SPLIT)[1] - fu.mystery_freq2(float(HF), float(HFL), float(LF), float(LFL), float(FIND_LP), SPLIT)[1]
    st.info(f"Tilt between :red[{FIND_LP}] MHz and :red[{FIND_HP}] MHz is:     :green[{round(tilt, 4)}] dB")
except ValueError:
    pass

st.divider()
st.subheader(":green[Frequency $\Longleftrightarrow$ Channel Converter]")
FIND_CH = st.text_input("Enter Frequency (MHz)", key="FIND_CH")
try:
    CH_NUMBER = fu.find_channel(float(FIND_CH))
    st.info(f"Channel number is :    :green[{CH_NUMBER}]")
except ValueError:
    pass
FIND_FREQ = st.text_input("Enter Channel Number", key="FIND_FREQ")
try:
    FREQUENCY = fu.find_freq(float(FIND_FREQ))
    st.info(f"QAM Center Frequency is :    :green[{FREQUENCY}] MHz  -  Analog Carrier Frequency is :    :green[{FREQUENCY-1.75}] MHz")
except ValueError:
    pass