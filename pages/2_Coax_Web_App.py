import streamlit as st
import pandas as pd
import altair as alt


def total_loss(x, distance_arg):
    return x * distance_arg / 100


def temp_change(x, temp_arg):
    return x*(1+((.01/10)*(temp_arg-68)))


st.set_page_config(page_title="Coax Cable", layout="wide", initial_sidebar_state='collapsed')
st.title("Coax Cable Loss vs Frequency")
st.subheader(":green[A Web APP to Visualize CATV Coaxial Cable Loss vs. Frequency.]")


st.divider()
distance_units = st.radio(":blue[Select Length Units]", options=["Feet", "Meters"])
distance = st.number_input(f":blue[Enter Cable length in {distance_units}]", value=200.0)
st.divider()
if distance_units == "Meters":
    coax_data = pd.read_csv("new_coax_db_per_100_meters.csv", encoding="UTF-8")
else:
    coax_data = pd.read_csv("new_coax_db_per_100_feet.csv", encoding="UTF-8")


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
    coax[coax_selected] = coax[coax_selected].map(lambda x: temp_change(x, temp))\

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

    chart1 = alt.Chart(coax, height=600).mark_line(strokeDash=[5,5], color="BlueViolet").encode(
        alt.X("Frequency:O", title="Frequency (MHz)"),
        alt.Y(coax_selected + " at 68F", title="Attenuation (dB)")
    )
    chart2 = alt.Chart(coax, height=600).mark_line().encode(
        alt.X("Frequency:O", title="Frequency (MHz)"),
        alt.Y(coax_selected, title="Attenuation (dB)")
    )

    st.altair_chart(chart1 + chart2, use_container_width=True, theme="streamlit")

with col2:

    if st.checkbox("Show Data Points"):
        st.write(coax)

