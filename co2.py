import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="CO₂ Dashboard", layout="wide")

st.title("🌍 CO₂ Emission Dashboard")
st.markdown("Compare emissions and costs across energy sources")

# Sample data
sources = ['Hydropower', 'Solar', 'Battery', 'Gas']
emission = [0.02, 0.05, 0.1, 0.3]
cost = [0.05, 0.1, 0.15, 0.2]

df = pd.DataFrame({
    'Source': sources,
    'CO2 Emission (kg/kWh)': emission,
    'Cost (USD/kWh)': cost
})

st.subheader("📊 Bar Chart")
st.plotly_chart(px.bar(df, x="Source", y="CO2 Emission (kg/kWh)", color="Source"))

st.subheader("📈 Line Chart")
st.plotly_chart(px.line(df, x="Source", y="Cost (USD/kWh)", markers=True))

st.subheader("📉 Area Chart")
st.plotly_chart(px.area(df, x="Source", y="CO2 Emission (kg/kWh)", color="Source"))

st.subheader("🍩 Doughnut Chart")
st.plotly_chart(px.pie(df, values="Cost (USD/kWh)", names="Source", hole=0.4))

st.subheader("🥧 Pie Chart")
st.plotly_chart(px.pie(df, values="CO2 Emission (kg/kWh)", names="Source"))

st.subheader("🌡️ Heatmap (Random Example)")
heatmap_data = np.random.rand(5, 5)
st.plotly_chart(px.imshow(heatmap_data, text_auto=True))

st.subheader("📊 Radar Chart")
fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=df["CO2 Emission (kg/kWh)"],
    theta=df["Source"],
    fill='toself',
    name='CO2 Emission'
))
fig_radar.add_trace(go.Scatterpolar(
    r=df["Cost (USD/kWh)"],
    theta=df["Source"],
    fill='toself',
    name='Cost'
))
fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
st.plotly_chart(fig_radar)

st.success("✅ App loaded successfully!")
