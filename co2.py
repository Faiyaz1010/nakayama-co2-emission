code = """

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="CO₂ Emission Dashboard", layout="wide")

st.title("🌍 CO₂ Emission Dashboard")
st.markdown("Compare emissions and cost from different energy sources")

st.sidebar.header("⚙️ Input Parameters")
energy_sources = ['Hydropower', 'Solar', 'Battery', 'Gas']
co2_emissions = [0.02, 0.05, 0.1, 0.3]
cost_per_kwh = [0.05, 0.1, 0.15, 0.2]

df = pd.DataFrame({
    'Energy Source': energy_sources,
    'CO₂ Emission (kg/kWh)': co2_emissions,
    'Cost (USD/kWh)': cost_per_kwh
})

df['Cost Efficiency (kWh/USD)'] = 1 / df['Cost (USD/kWh)']
df['Emission Rank'] = df['CO₂ Emission (kg/kWh)'].rank()

selected_source = st.sidebar.selectbox("Select Energy Source", energy_sources)
hours_used = st.sidebar.slider("Usage per Week (in hours)", 0, 168, 40)

emission = df[df['Energy Source'] == selected_source]['CO₂ Emission (kg/kWh)'].values[0]
cost = df[df['Energy Source'] == selected_source]['Cost (USD/kWh)'].values[0]
total_emission = emission * hours_used * 7
total_cost = cost * hours_used * 7

st.subheader(f"📊 Weekly Summary for: {selected_source}")
col1, col2 = st.columns(2)
col1.metric("Total Weekly CO₂ Emission", f"{total_emission:.2f} kg")
col2.metric("Total Weekly Cost", f"${total_cost:.2f}")

st.markdown("---")

st.subheader("💨 CO₂ Emission by Energy Source")
fig_bar = px.bar(df, x='Energy Source', y='CO₂ Emission (kg/kWh)',
                 color='Energy Source', text='CO₂ Emission (kg/kWh)',
                 color_discrete_sequence=px.colors.qualitative.Bold)
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("💰 Cost per kWh")
fig_line = px.line(df, x='Energy Source', y='Cost (USD/kWh)',
                   markers=True, line_shape='linear')
st.plotly_chart(fig_line, use_container_width=True)

st.subheader("📈 CO₂ Emission Share")
fig_pie = px.pie(df, names='Energy Source', values='CO₂ Emission (kg/kWh)',
                 hole=0.3, title='Emission Distribution')
st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("📊 Radar Comparison (Lower = Better Emission)")
fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=df['CO₂ Emission (kg/kWh)'],
    theta=df['Energy Source'],
    fill='toself',
    name='CO₂ Emission'
))
fig_radar.add_trace(go.Scatterpolar(
    r=df['Cost (USD/kWh)'],
    theta=df['Energy Source'],
    fill='toself',
    name='Cost'
))
fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True)),
                        showlegend=True)
st.plotly_chart(fig_radar, use_container_width=True)

st.subheader("🌡️ Randomized CO₂ Heatmap (Example)")
heat_data = np.random.rand(10, 10)
fig_heat = px.imshow(heat_data, color_continuous_scale='Viridis',
                     labels=dict(color="Emission Level"))
st.plotly_chart(fig_heat, use_container_width=True)

st.markdown("---")
st.markdown("Made with ❤️ for sustainability and data transparency.")
"""

with open("co2.py", "w", encoding="utf-8") as f:
    f.write(code)
