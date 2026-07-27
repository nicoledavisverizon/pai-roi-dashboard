import pandas as pd
import streamlit as st

# Set page configuration to make it look professional
st.set_page_config(page_title="PA&I ROI Tracker", page_icon="📈", layout="wide")

# 1. Title and Header
st.title("📊 PA&I Team ROI & Impact Tracker")
st.markdown("### 2026 Focus Area: Leading with AI & Scaling Our Impact")
st.write("Welcome to the interactive ROI dashboard. This tool tracks the time saved, financial impact, and strategic alignment of the People Analytics & Insights (PA&I) team's initiatives.")

# 2. Sidebar Filters for Leaders to Interact With
st.sidebar.header("Filter Dashboard")

# Filter by Strategic Workstream
workstream_options = ["All Workstreams", "Readiness & Enablement", "Hub & Spoke", "EV&E Integration", "Qlik Cloud Transition", "Technology & Design"]
selected_workstream = st.sidebar.selectbox("Select Workstream", workstream_options)

# Interactive Slider for Leaders to "Model" different ROI Scenarios
st.sidebar.subheader("🎛️ ROI Scenario Modeler")
st.sidebar.write("What if we scaled our AI training to more teams?")
trained_users_multiplier = st.sidebar.slider("Increase AI Adoption Multiplier", 1.0, 5.0, 1.0, step=0.5)

# 3. Hackathon Demo Data (Using sample data for a perfect presentation)
data = {
    'Project_Name': ['Qlik Cloud Training', 'Comms Generator Gem', 'ROI Tracker Form', 'Sasquatch Hub Setup', 'EV&E Feedback Loop'],
    'Workstream': ['Readiness & Enablement', 'Readiness & Enablement', 'Technology & Design', 'Hub & Spoke', 'EV&E Integration'],
    'Hours_Saved_Monthly': [120, 80, 45, 150, 60],
    'Estimated_Dollar_Savings': [6000, 4000, 2250, 7500, 3000]
}
df = pd.DataFrame(data)

# Apply Sidebar Workstream Filter
if selected_workstream != "All Workstreams":
    df_filtered = df[df['Workstream'] == selected_workstream]
else:
    df_filtered = df.copy()

# Apply the Multiplier to the Calculations (Modeling Scenario)
df_filtered['Hours_Saved_Monthly'] = df_filtered['Hours_Saved_Monthly'] * trained_users_multiplier
df_filtered['Estimated_Dollar_Savings'] = df_filtered['Estimated_Dollar_Savings'] * trained_users_multiplier

# 4. High-Level Metric Cards (KPIs)
total_hours = int(df_filtered['Hours_Saved_Monthly'].sum())
total_savings = int(df_filtered['Estimated_Dollar_Savings'].sum())
total_projects = len(df_filtered)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🚀 Active PA&I Projects", value=total_projects)
with col2:
    st.metric(label="⏱️ Monthly Hours Saved", value=f"{total_hours:,} Hours")
with col3:
    st.metric(label="💰 Monthly Estimated ROI", value=f"${total_savings:,}")

st.markdown("---")

# 5. Charts and Visuals
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("💡 Impact by Project (Hours Saved)")
    # Simple bar chart
    st.bar_chart(data=df_filtered, x='Project_Name', y='Hours_Saved_Monthly')

with col_right:
    st.subheader("🔍 Project Details Table")
    # Clean data table
    st.dataframe(df_filtered[['Project_Name', 'Workstream', 'Hours_Saved_Monthly', 'Estimated_Dollar_Savings']], use_container_width=True)

st.markdown("---")
st.info("💡 **Interactive Tip:** Adjust the slider in the sidebar to see how increasing AI adoption directly scales our team's monthly hours saved and dollar ROI!")
