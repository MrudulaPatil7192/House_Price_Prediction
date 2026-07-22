import streamlit as st
import pickle
import numpy as np
import os

# Professional Dashboard Configuration
st.set_page_config(
    page_title="Property Valuation Dashboard",
    page_icon="📊",
    layout="wide"  # Wide layout mimics a Power BI landscape canvas
)

# Power BI Style UI Sheet Layout with Explicit Dark Text Controls
st.markdown("""
    <style>
    /* Power BI Canvas Background */
    .stApp {
        background-color: #F3F2F1 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Top Navigation / Title Banner */
    .dashboard-header {
        background-color: #1F1F1F !important;
        padding: 20px 25px;
        border-radius: 6px;
        margin-bottom: 20px;
        color: #FFFFFF !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .dashboard-title {
        font-size: 24px;
        font-weight: 600;
        margin: 0;
        color: #FFFFFF !important;
    }
    .dashboard-subtitle {
        font-size: 13px;
        color: #A19F9D !important;
        margin-top: 4px;
    }
    
    /* Power BI Visual Card Container */
    .powerbi-card {
        background-color: #FFFFFF !important;
        padding: 20px;
        border-radius: 6px;
        border: 1px solid #E1DFDD;
        box-shadow: 0 1.6px 3.6px 0 rgba(0,0,0,0.132), 0 0.3px 0.9px 0 rgba(0,0,0,0.106);
        margin-bottom: 20px;
        color: #201F1E !important;
    }
    
    .card-title {
        font-size: 14px;
        font-weight: 700;
        color: #201F1E !important;
        border-bottom: 2px solid #F3F2F1;
        padding-bottom: 8px;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Force all Streamlit Text Elements & Labels to Dark/Black */
    .stApp p, .stApp span, .stApp label, .stApp div, .stMarkdown {
        color: #1F1F1F !important;
    }
    
    /* Fix input field label text colors explicitly */
    div[data-baseweb="input"] input {
        color: #FFFFFF !important; /* Keep input text inside dark input boxes white */
    }
    
    /* Power BI KPI Card Elements */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #FAFAFA !important;
        padding: 15px;
        border-left: 5px solid #107C41 !important;
        border-radius: 0 4px 4px 0;
        box-shadow: inset 0 0 2px rgba(0,0,0,0.05);
    }
    .kpi-value {
        font-size: 30px;
        font-weight: 700;
        color: #201F1E !important;
    }
    .kpi-label {
        font-size: 11px;
        font-weight: 700;
        color: #605E5C !important;
        letter-spacing: 0.5px;
    }
    
    /* Action Button Customization */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #107C41 !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px;
        font-weight: 600;
        font-size: 15px;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: background-color 0.2s ease;
    }
    div.stButton > button:first-child * {
        color: #FFFFFF !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #0B5931 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Path-safe model loader
@st.cache_resource
def load_model():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "new.pkl")
    with open(file_path, "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading analytical model `new.pkl`: {e}")
    st.info("Make sure `new.pkl` is placed in the exact same directory as `app.py`.")
    st.stop()

# Header Banner Canvas
st.markdown("""
    <div class="dashboard-header">
        <div class="dashboard-title">🏠 Real Estate Valuation & Analytics Workspace</div>
        <div class="dashboard-subtitle">Power BI Executive Summary View • Live Interactive Model Evaluation</div>
    </div>
""", unsafe_allow_html=True)

# Dashboard Workspace Layout Grid
col_left, col_right = st.columns([7, 5])

with col_left:
    st.markdown('<div class="powerbi-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📐 Property Dimensional Features</div>', unsafe_allow_html=True)
    
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        gr_liv_area = st.number_input("Above Ground Living Area (SqFt)", min_value=300, max_value=6000, value=1500, step=50)
        total_bsmt_sf = st.number_input("Total Basement Area (SqFt)", min_value=0, max_value=6000, value=1000, step=50)
    with sub_col2:
        lot_area = st.number_input("Total Lot Land Area (SqFt)", min_value=500, max_value=100000, value=10000, step=250)
        idx = st.number_input("Property ID Reference", min_value=1, max_value=3000, value=1461, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="powerbi-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">⭐ Structural & Quality Metrics</div>', unsafe_allow_html=True)
    
    sub_col3, sub_col4 = st.columns(2)
    with sub_col3:
        overall_qual = st.slider("Overall Material/Finish Quality (1-10)", min_value=1, max_value=10, value=6, step=1)
        year_built = st.number_input("Original Construction Year", min_value=1800, max_value=2026, value=1975, step=1)
    with sub_col4:
        garage_cars = st.slider("Garage Capacity (Vehicle Count)", min_value=0, max_value=5, value=2, step=1)
        full_bath = st.slider("Full Bathrooms", min_value=0, max_value=4, value=2, step=1)
        bedroom_abv_gr = st.slider("Bedrooms (Above Ground)", min_value=0, max_value=8, value=3, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="powerbi-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🔮 Executive Summary Report</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='color: #201F1E !important;'>Review the parameter values configured in the matrix tiles. Click below to compute the analytical appraisal output.</p>", unsafe_allow_html=True)
    
    compute_btn = st.button("📊 Calculate Summary Analytics")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if compute_btn:
        # Construct pipeline inputs matching model expectation
        features = np.array([[
            idx, overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, year_built, full_bath, bedroom_abv_gr, lot_area
        ]])
        
        # Run regression calculation
        raw_prediction = float(model.predict(features)[0])
        
        # Power BI Style KPI Tile
        st.markdown(f"""
            <div class="kpi-container" style="margin-bottom: 20px;">
                <div>
                    <div class="kpi-label">PREDICTED MARKET VALUE (INR)</div>
                    <div class="kpi-value">₹{raw_prediction:,.2f}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Secondary Summary Table
        st.markdown(f"""
            <table style="width:100%; border-collapse: collapse; font-size: 13px; color:#201F1E;">
                <tr style="background-color: #F3F2F1; border-bottom: 1px solid #E1DFDD;">
                    <td style="padding: 10px; font-weight: 600; color:#201F1E;">Data Metric</td>
                    <td style="padding: 10px; font-weight: 600; text-align: right; color:#201F1E;">Value Metric</td>
                </tr>
                <tr style="border-bottom: 1px solid #F3F2F1;">
                    <td style="padding: 10px; color:#404040;">Price Per SqFt</td>
                    <td style="padding: 10px; text-align: right; font-weight:600; color:#201F1E;">₹{(raw_prediction / max(1, gr_liv_area)):,.2f}</td>
                </tr>
                <tr style="border-bottom: 1px solid #F3F2F1;">
                    <td style="padding: 10px; color:#404040;">Asset Class Tier</td>
                    <td style="padding: 10px; text-align: right; font-weight:600; color:#107C41;">
                        {"Premium Tier" if raw_prediction >= 250000 else "Standard Tier" if raw_prediction >= 140000 else "Economy Tier"}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 10px; color:#404040;">Model Engine Reference</td>
                    <td style="padding: 10px; text-align: right; font-weight:600; color:#201F1E;">K-Neighbors Regressor</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)
    else:
        st.info("ℹ️ Input data parameters ready. Select 'Calculate Summary Analytics' to evaluate the valuation KPI dashboard canvas.")
        
    st.markdown('</div>', unsafe_allow_html=True)
