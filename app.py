import streamlit as st
import folium
from streamlit_folium import st_folium

from utils import load_sample_data, get_risk_color
from analysis import evaluate_corridor_risk

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Wildlife Corridor Intelligence System",
    layout="wide"
)

# -------------------------
# Title
# -------------------------
st.title("🌿 Wildlife Corridor Intelligence System")
st.markdown("Analyze wildlife corridors, detect conflict zones, and visualize risks across India.")

# -------------------------
# Load Data
# -------------------------
habitats, corridors, roads = load_sample_data()

# -------------------------
# Analyze
# -------------------------
evaluated_corridors, conflict_points = evaluate_corridor_risk(corridors, roads)

# -------------------------
# Sidebar Controls
# -------------------------
st.sidebar.header("Controls")

show_roads = st.sidebar.checkbox("Show Roads", True)

risk_filter = st.sidebar.selectbox(
    "Filter by Risk Level",
    ["All", "High", "Low"]
)

# -------------------------
# Metrics
# -------------------------
col1, col2 = st.columns(2)

col1.metric("Total Corridors", len(evaluated_corridors))
col2.metric("Conflict Zones", len(conflict_points))

# -------------------------
# Map
# -------------------------
m = folium.Map(
    location=[22.5, 80.0],
    zoom_start=5,
    tiles="CartoDB positron"
)

# -------------------------
# Add Habitats (Park Names Visible)
# -------------------------
for h in habitats:
    folium.Marker(
        location=h["coords"],
        popup=h["name"],
        tooltip=h["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# -------------------------
# Add Corridors
# -------------------------
for c in evaluated_corridors:

    if risk_filter != "All" and c["risk"] != risk_filter:
        continue

    folium.PolyLine(
        locations=c["coords"],
        color=get_risk_color(c["risk"]),
        weight=5,
        opacity=0.9,
        tooltip=f"{c['name']} ({c['risk']} Risk)"
    ).add_to(m)

# -------------------------
# Add Roads
# -------------------------
if show_roads:
    for r in roads:
        folium.PolyLine(
            locations=r["coords"],
            color="black",
            weight=2,
            opacity=0.6,
            tooltip="Road"
        ).add_to(m)

# -------------------------
# Add Conflict Zones
# -------------------------
for pt in conflict_points:
    folium.CircleMarker(
        location=pt["coords"],
        radius=7,
        color="red",
        fill=True,
        fill_opacity=1,
        popup="Conflict Zone"
    ).add_to(m)

# -------------------------
# Add Legend (Professional Look)
# -------------------------
legend_html = """
<div style="
position: fixed;
bottom: 40px;
left: 40px;
width: 220px;
background-color: white;
border-radius: 10px;
border:2px solid grey;
z-index:9999;
padding:12px;
font-size:14px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
">
<b>Map Legend</b><br><br>
<span style="color:#d73027;">■■</span> High Risk Corridor<br>
<span style="color:#1a9850;">■■</span> Safe Corridor<br>
<span style="color:black;">■■</span> Roads<br>
<span style="color:red;">●</span> Conflict Zone<br>
<span style="color:blue;">●</span> National Parks
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# -------------------------
# Display Map
# -------------------------
st_folium(m, width=1100, height=600)

# -------------------------
# Insights Section
# -------------------------
st.subheader("📊 Insights")

if conflict_points:
    st.error("⚠️ High-risk wildlife conflict zones detected!")
else:
    st.success("✅ No major conflicts detected")

st.markdown("### Corridor Summary")

for c in evaluated_corridors:
    st.write(f"- **{c['name']}** → {c['risk']} Risk")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.caption("Built using Streamlit, Folium, and Shapely for geospatial analysis.")