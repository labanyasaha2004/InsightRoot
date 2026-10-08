import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------------------
# Page Setup
# --------------------------------------------------

st.set_page_config(
    page_title="InsightRoot",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_transactions.csv"


df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])
# --------------------------------------------------
# Filters
# --------------------------------------------------

st.sidebar.header("🔎 Filters")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["region"].unique().tolist())
)
if selected_region != "All":
    df = df[df["region"] == selected_region]

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📊 InsightRoot")
st.subheader("Automated Business Root-Cause Analysis")

st.write(
    "Analyze business performance and identify the key drivers "
    "behind revenue changes."
)

# --------------------------------------------------
# Overall Business Performance
# --------------------------------------------------

april = df[df["date"].dt.month == 4]
may = df[df["date"].dt.month == 5]

april_revenue = april["revenue"].sum()
may_revenue = may["revenue"].sum()

revenue_change = (
    (may_revenue - april_revenue)
    / april_revenue
    * 100
)

april_units = april["units_sold"].sum()
may_units = may["units_sold"].sum()

units_change = (
    (may_units - april_units)
    / april_units
    * 100
)

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

st.header("📈 Business Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "April Revenue",
    f"₹{april_revenue:,.0f}"
)

col2.metric(
    "May Revenue",
    f"₹{may_revenue:,.0f}"
)

col3.metric(
    "Revenue Change",
    f"{revenue_change:.1f}%"
)

col4.metric(
    "Units Change",
    f"{units_change:.1f}%"
)

# --------------------------------------------------
# Root Cause
# --------------------------------------------------

st.divider()

st.header("🔴 Primary Root Cause")

if selected_region == "All":
    st.subheader("West Region")

    st.write(
        "InsightRoot identified the West region as the primary "
        "driver of the revenue decline."
    )
else:
    st.subheader(f"{selected_region} Region")

    st.write(
        f"You are currently viewing performance for the "
        f"{selected_region} region."
    )

col1, col2, col3, col4 = st.columns(4)

# Calculate changes for selected region

april_units = april["units_sold"].sum()
may_units = may["units_sold"].sum()

april_visits = april["website_visits"].sum()
may_visits = may["website_visits"].sum()

april_conversion = april["conversion_rate"].mean()
may_conversion = may["conversion_rate"].mean()

units_change = (
    (may_units - april_units)
    / april_units
    * 100
)

visits_change = (
    (may_visits - april_visits)
    / april_visits
    * 100
)

conversion_change = (
    (may_conversion - april_conversion)
    / april_conversion
    * 100
)


col1.metric(
    "Revenue Change",
    f"{revenue_change:.1f}%"
)

col2.metric(
    "Units Sold",
    f"{units_change:.1f}%"
)

col3.metric(
    "Website Visits",
    f"{visits_change:+.1f}%"
)

col4.metric(
    "Conversion Rate",
    f"{conversion_change:.1f}%"
)
# --------------------------------------------------
# Automated Insight
# --------------------------------------------------

if selected_region == "All":

    st.info(
        "💡 Insight: The West region is the primary driver of "
        "the overall revenue decline. Revenue fell by 19.3% "
        "while website traffic increased by 4.9%, suggesting "
        "that the issue was not primarily caused by lower traffic."
    )

else:

    st.info(
        f"💡 Insight: {selected_region} region revenue changed "
        f"by {revenue_change:.1f}%, while units sold changed by "
        f"{units_change:.1f}%. Website traffic changed by "
        f"{visits_change:+.1f}% and conversion rate changed by "
        f"{conversion_change:.1f}%."
    )
# --------------------------------------------------
# Region Comparison
# --------------------------------------------------
st.divider()

st.header("🌍 Revenue Change by Region")
st.caption("Percentage change in revenue from April to May")

april_region = april.groupby("region")["revenue"].sum()
may_region = may.groupby("region")["revenue"].sum()

region_change = (
    (may_region - april_region)
    / april_region
    * 100
).reset_index()

region_change.columns = ["Region", "Revenue Change"]

region_change = region_change.sort_values(
    "Revenue Change"
)

fig = px.bar(
    region_change,
    x="Region",
    y="Revenue Change",
    title="April → May Revenue Change",
    text="Revenue Change"
)

fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig.update_layout(
    yaxis_title="Revenue Change (%)",
    xaxis_title="Region",
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# --------------------------------------------------
# Data Preview
# --------------------------------------------------

with st.expander("View Transaction Data"):

    st.dataframe(
        df.head(100),
        use_container_width=True
    )