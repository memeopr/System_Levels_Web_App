import streamlit as st
import functions as fu
import pandas as pd

digits = 2
step_size_freq = 6
step_size_ch = 1


def plot_levels():
    x, y = fu.system_levels(float(HF), float(HFL), float(LF), float(LFL), SPLIT)
    df = pd.DataFrame(list(zip(x, y)), columns=["Frequency (MHz)", "Level (dBmV)"])
    with col2:
        st.subheader(":blue[_System Levels vs Frequency_]")
        st.bar_chart(df, width=640, height=500, x="Frequency (MHz)", y="Level (dBmV)")
        st.info(f"Total Power is :green[{round(fu.total_power(y), digits)}] dBmV")


st.set_page_config(page_title="System Levels Tilt method", layout="wide", initial_sidebar_state='collapsed')
col3, col4 = st.columns(2)
with col3:
    st.title("System Levels")
    st.subheader(":green[A Web APP to calculate CATV system levels.]")
with col4:
    st.image("sys_lev.png", width=400)
st.divider()


col1, col2 = st.columns(2)


with col1:
    HF = st.number_input("Enter High Frequency (MHz)", key="HF", value=1218, min_value=54, step=step_size_freq)
    HFL = st.number_input("Enter Tilt at High Frequency (dB)", key="HFL", value=17, step=step_size_ch)
    st.divider()
    LF = st.number_input("Enter Carrier Frequency (MHz)", key="LF", value=1218, min_value=54, step=step_size_freq)
    LFL = st.number_input("Enter Level at Carrier Frequency (dBmV)", key="LFL", value=52, step=step_size_ch)
    SPLIT = st.selectbox("Select Split", options=["Low", "Mid", "High"], key="SPLIT")
    Calc = st.button("Show Plot", key='calculate', on_click=plot_levels, type="primary")

checkbox = st.checkbox("Display Data Points")
if checkbox:
    divisor = st.divider()
    x, y = fu.system_levels(float(HF), float(HFL), float(LF), float(LFL), SPLIT)
    df = pd.DataFrame(list(zip(x, y)), columns=["Frequency (MHz)", "Level (dBmV)"])
    data_frame_display = st.dataframe(df)


st.divider()
st.subheader(":green[Find Frequency]")
FIND_FQ = st.number_input("Enter Frequency (MHz)", key="FIND_FQ", step=step_size_freq)
try:
    st.info(f"Level at {FIND_FQ} MHz is:     :green[{round(fu.mystery_freq(float(HF), float(HFL), float(LF), float(LFL), float(FIND_FQ), SPLIT)[1], digits)}] dBmV")
except ValueError:
    pass

st.divider()
st.subheader(":green[Find Tilt]")
FIND_LP = st.number_input("Enter Low  Carrier's Frequency (MHz)", key="FIND_LP", min_value=54, step=step_size_freq)
FIND_HP = st.number_input("Enter High  Carrier's Frequency (MHz)", key="FIND_HP", step=step_size_freq)
try:
    tilt = fu.mystery_freq(float(HF), float(HFL), float(LF), float(LFL), float(FIND_HP), SPLIT)[1] - fu.mystery_freq(float(HF), float(HFL), float(LF), float(LFL), float(FIND_LP), SPLIT)[1]
    st.info(f"Tilt between :red[{FIND_LP}] MHz and :red[{FIND_HP}] MHz is:     :green[{round(tilt, digits)}] dB")
except ValueError:
    pass

st.divider()
st.subheader(":green[Frequency $\Longleftrightarrow$ Channel Converter]")
FIND_CH = st.number_input("Enter Frequency (MHz)", key="FIND_CH", step=step_size_freq)
try:
    CH_NUMBER = fu.find_channel(float(FIND_CH))
    st.info(f"Channel number is :    :green[{CH_NUMBER}]")
except ValueError:
    pass
FIND_FREQ = st.number_input("Enter Channel Number", key="FIND_FREQ", min_value=2, step=step_size_ch)
try:
    FREQUENCY = fu.find_freq(float(FIND_FREQ))
    st.info(f"QAM Center Frequency is :    :green[{FREQUENCY}] MHz  -  Analog Carrier Frequency is :    :green[{FREQUENCY-1.75}] MHz")
except ValueError:
    pass
