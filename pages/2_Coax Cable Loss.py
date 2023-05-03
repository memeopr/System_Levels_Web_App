import streamlit as st
import pandas as pd
import altair as alt
import functions as fu

st.set_page_config(page_title="Coax Web APP", layout="wide", initial_sidebar_state='expanded')

if "HFL_" not in st.session_state:
    if "HFL2_" not in st.session_state:
        for k in st.session_state.keys():
            st.session_state[f"{k}_"] = st.session_state[k]


def save_states():
    if "new_HFL" not in st.session_state:
        for k in st.session_state.keys():
            st.session_state[f"new_{k}"] = st.session_state[k]


def total_loss(x, distance_arg):
    return x * distance_arg / 100


def temp_change(x, temp_arg):
    return x * (1 + ((.01 / 10) * (temp_arg - 68)))


@st.cache_data
def load_cable_data_100f():
    return pd.read_csv("new_coax_db_per_100_feet.csv", encoding="UTF-8")


@st.cache_data
def load_cable_100m():
    return pd.read_csv("new_coax_db_per_100_meters.csv", encoding="UTF-8")


st.title("Coax Cable Loss vs Frequency")
st.subheader(":green[A Web APP to Visualize CATV Coaxial Cable Loss vs. Frequency.]")

st.divider()
distance_units = st.radio(":blue[Select Length Units]", options=["Feet", "Meters"])
distance = st.number_input(f":blue[Enter Cable length in {distance_units}]", value=200.0)
st.divider()
if distance_units == "Meters":
    coax_data = load_cable_100m()
else:
    coax_data = load_cable_data_100f()

cable_types = list(coax_data.columns.values)[1:]

index_val = cable_types.index("QR® 540 JCAT 3G AJ SM")

coax_selected = st.selectbox(":blue[Select Coax Cable]", options=cable_types, index=index_val)
st.divider()

coax = coax_data.loc[:, ["Frequency", coax_selected]]
coax[coax_selected] = coax[coax_selected].map(lambda x: total_loss(x, distance))
coax[coax_selected + " at 68F"] = coax.loc[:, coax_selected]

checkbox = st.checkbox(":blue[Display Data Points]")

if checkbox:
    st.dataframe(coax.loc[:, ["Frequency", coax_selected]])

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.subheader(f":green[{coax_selected}] - :blue[Attenuation vs. Frequency]")
    st.text(f"{distance} {distance_units} of {' '.join(coax_selected.split(' ')[:2])}")

    temp = st.slider(":red[Temperature $\degree F$]", min_value=-80, max_value=200, value=68)
    coax[coax_selected] = coax[coax_selected].map(lambda x: temp_change(x, temp)) \
 \
        # coax = coax.melt("Frequency", var_name="Cable Type", value_name="Loss")
    coax["delta"] = coax[coax_selected] - coax[coax_selected + " at 68F"]

    col1a, col1b = st.columns(2)
    with col1a:
        choice = st.selectbox(":blue[Select Frequency Range to Plot]", options=["Full", "Return", "Forward"])
    if choice != "Full":
        with col1b:
            choice2 = st.selectbox(":blue[Select Split to Plot]", options=["Low", "Mid", "High"])

    if choice == "Return":
        if choice2 == "Low":
            coax = coax[coax["Frequency"] < 54]
        elif choice2 == "Mid":
            coax = coax[coax["Frequency"] < 108]
        else:
            coax = coax[coax["Frequency"] < 254]
    if choice == "Forward":
        if choice2 == "Low":
            coax = coax[(coax["Frequency"] >= 54) & (coax["Frequency"] <= 1218)]
        elif choice2 == "Mid":
            coax = coax[(coax["Frequency"] >= 108) & (coax["Frequency"] <= 1218)]
        else:
            coax = coax[(coax["Frequency"] >= 254) & (coax["Frequency"] <= 1218)]

    chart1 = alt.Chart(coax, height=500).mark_line(strokeDash=[5, 5], color="BlueViolet").encode(
        alt.X("Frequency:O", title="Frequency (MHz)"),
        alt.Y(coax_selected + " at 68F", title="Attenuation (dB)")
    )
    chart2 = alt.Chart(coax, height=500).mark_line().encode(
        alt.X("Frequency:O", title="Frequency (MHz)"),
        alt.Y(coax_selected, title="Attenuation (dB)")
    )

    st.altair_chart(chart1 + chart2, use_container_width=True, theme="streamlit")

    display_system_levels_checkbox = st.checkbox(" Display System Levels", value=False)

    if display_system_levels_checkbox:

        if ("HF" in st.session_state) or ("HF_" in st.session_state):

            if "HF_" in st.session_state:
                HF = st.session_state.HF_
                HFL = st.session_state.HFL_
                LF = st.session_state.LF_
                LFL = st.session_state.LFL_
                SPLIT = st.session_state.SPLIT_
            elif "HF" in st.session_state:
                HF = st.session_state.HF
                HFL = st.session_state.HFL
                LF = st.session_state.LF
                LFL = st.session_state.LFL
                SPLIT = st.session_state.SPLIT
            st.divider()
            st.write([HF, HFL, LF, LFL, SPLIT])
            x, y = fu.system_levels2(float(HF), float(HFL), float(LF), float(LFL), SPLIT)
            df = pd.DataFrame(list(zip(x, y)), columns=["Frequency (MHz)", "Level (dBmV)"])

            coax_Freq_Modified = coax[coax["Frequency"].isin(x)]

            st.subheader(f":blue[System Levels vs Frequency]")

            if distance > 0:
                distance_slider = st.slider(":blue[Distance Slider - Move Slider to see Effect on System Levels]",
                                            min_value=0,
                                            max_value=int(distance), value=0)
            else:
                distance_slider = 0

            df = pd.concat([df.set_index("Frequency (MHz)"),
                            coax_Freq_Modified.set_index("Frequency")[coax_selected].rename("Loss")],
                           axis=1).reset_index(names="Frequency (MHz)")

            df["Loss"] = df["Loss"].map(lambda x: total_loss(x, distance_slider / distance * 100))

            df["Level (dBmV)"] = df["Level (dBmV)"] + df["Loss"]

            st.bar_chart(df, width=640, height=500, x="Frequency (MHz)", y="Level (dBmV)")

        elif ("HF2" in st.session_state) or ("HF2_" in st.session_state):
            if "HF2_" in st.session_state:
                HF = st.session_state.HF2_
                HFL = st.session_state.HFL2_
                LF = st.session_state.LF2_
                LFL = st.session_state.LFL2_
                SPLIT = st.session_state.SPLIT2_
            elif "HF2" in st.session_state:
                HF = st.session_state.HF2
                HFL = st.session_state.HFL2
                LF = st.session_state.LF2
                LFL = st.session_state.LFL2
                SPLIT = st.session_state.SPLIT2
            st.write([HF, HFL, LF, LFL, SPLIT])
            st.divider()
            x, y = fu.system_levels(float(HF), float(HFL), float(LF), float(LFL), SPLIT)
            df = pd.DataFrame(list(zip(x, y)), columns=["Frequency (MHz)", "Level (dBmV)"])

            coax_Freq_Modified = coax[coax["Frequency"].isin(x)]

            st.subheader(f":blue[System Levels vs Frequency]")

            if distance > 0:
                distance_slider = st.slider(":blue[Distance Slider - Move Slider to see Effect on System Levels]",
                                            min_value=0,
                                            max_value=int(distance), value=0)
            else:
                distance_slider = 0

            df = pd.concat([df.set_index("Frequency (MHz)"),
                            coax_Freq_Modified.set_index("Frequency")[coax_selected].rename("Loss")],
                           axis=1).reset_index(names="Frequency (MHz)")

            df["Loss"] = df["Loss"].map(lambda x: total_loss(x, distance_slider / distance * 100))

            df["Level (dBmV)"] = df["Level (dBmV)"] + df["Loss"]

            st.bar_chart(df, width=640, height=500, x="Frequency (MHz)", y="Level (dBmV)")

with col2:
    if st.checkbox("Show Data Points"):
        st.write(coax)
