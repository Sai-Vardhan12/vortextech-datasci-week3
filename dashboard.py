import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv(r"E:\sai\VortexTech Intern\Week-3\dataset.csv")

st.title("Students Placement Dashboard")
st.write(f"Number of columns: {len(df.columns)}")
st.write(f"Number of  rows: {len(df)}")
selected_col = st.selectbox("Select a column", df.columns)

if selected_col not in df.select_dtypes(include=["number"]).columns:
    st.warning("Please choose a numeric column to use the range slider.")
    st.dataframe(df)
    st.stop()

category = st.selectbox("Select a category", df[selected_col].dropna().unique())
filtered_df = df[df[selected_col] == category]

numeric_series = pd.to_numeric(df[selected_col], errors="coerce").dropna()
min_val = float(numeric_series.min())
max_val = float(numeric_series.max())

min_val, max_val = st.slider(
    "Range",
    min_value=min_val,
    max_value=max_val,
    value=(min_val, max_val),
)

filtered_data = filtered_df[
    (pd.to_numeric(filtered_df[selected_col], errors="coerce") >= min_val)
    & (pd.to_numeric(filtered_df[selected_col], errors="coerce") <= max_val)
]

bar_data = filtered_data[selected_col].value_counts().rename_axis("label").reset_index(name="count")

bar_chart = (
    alt.Chart(bar_data)
    .mark_bar()
    .encode(
        x=alt.X("label:N", title=selected_col),
        y=alt.Y("count:Q", title="Count", scale=alt.Scale(domain=[0, 1000])),
    )
    .properties(height=400)
)

st.subheader(f"Bar Chart of {selected_col}")
st.altair_chart(bar_chart, use_container_width=True)

scatter_chart = (
    alt.Chart(bar_data)
    .mark_point(color="#8b0000", size=80)
    .encode(
        x=alt.X("label:N", title=selected_col),
        y=alt.Y("count:Q", title="Count", scale=alt.Scale(domain=[0, 1000])),
    )
    .properties(height=400)
)

st.subheader(f"Scatter Plot of {selected_col}")
st.altair_chart(scatter_chart, use_container_width=True)
st.subheader("Filtered Data")
st.dataframe(filtered_data)