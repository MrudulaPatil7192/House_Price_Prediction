import streamlit as st
import pickle
import numpy as np

# Set page configuration with a cute flower/garden theme
st.set_page_config(
    page_title="Garden Castle Price Predictor 🌸",
    page_icon="🧚🏡",
    layout="centered"
)

# 3D Cottagecore Flower Cartoon UI Styling
st.markdown("""
    <style>
    /* Vibrant, cute pastel fairy garden gradient background */
    .stApp {
        background: linear-gradient(135deg, #fef08a 0%, #bbf7d0 50%, #a7f3d0 100%);
    }
    
    /* 3D Soft Clay Outer Card Container with thick cartoon borders */
    .garden-card {
        background: #ffffff;
        padding: 35px;
        border-radius: 30px;
        box-shadow: 
            0px 10px 0px #22c55e,
            0px 20px 30px rgba(34, 197, 94, 0.15);
        border: 4px solid #14532d; /* Deep moss green borders for a vintage cartoon look */
        margin-bottom: 25px;
    }
    
    /* Cute Botanical Header Bubble */
    .bubble-header {
        background: #f43f5e; /* Vibrant berry pink */
        border: 4px solid #14532d;
        border-radius: 22px;
        padding: 18px;
        text-align: center;
        box-shadow: 5px 5px 0px #14532d;
        margin-bottom: 35px;
    }
    
    .bubble-title {
        color: #ffffff;
        font-size: 30px;
        font-weight: 900;
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
        margin: 0;
        text-shadow: 3px 3px 0px #14532d;
    }
    
    .bubble-subtitle {
        color: #ffe4e6;
        font-size: 14px;
        font-weight: 700;
        margin-top: 5px;
        letter-spacing: 0.5px;
    }
    
    /* Transforming Input Blocks into 3D Cartoon Panels */
    div[data-testid="stNumberInput"], div[data-testid="stSlider"] {
        background: #f0fdf4 !important; /* Soft meadow green tint */
        padding: 18px !important;
        border-radius: 20px !important;
        border: 3px solid #14532d !important;
        box-shadow: 4px 4px 0px #14532d !important;
        margin-bottom: 24px !important;
        transition: transform 0.1s ease !important;
    }
    
    div[data-testid="stNumberInput"]:focus-within, div[data-testid="stSlider"]:focus-within {
        transform: translate(-2px, -2px) !important;
        box-shadow: 6px 6px 0px #14532d !important;
        background: #ffffff !important;
    }
    
    /* Chunky 3D Cartoon Magic Button */
    .stButton > button {
        width: 100%;
        background: #ec4899; /* Bright pink */
        color: #ffffff !important;
        border: 4px solid #14532d;
        border-radius: 20px;
        padding: 16px 24px;
        font-size: 20px;
        font-weight: 900;
        font-family: 'Comic Sans MS', sans-serif;
        box-shadow: 0px 6px 0px #14532d;
        transition: all 0.1s ease;
    }
    
    .stButton > button:hover {
        background: #db2777;
        color: #ffffff !important;
        transform: translateY(2px);
        box-shadow: 0px 4px 0px #14532d;
    }
    
    .stButton > button:active {
        transform: translateY(6px);
        box-shadow: 0px 0px 0px #14532d;
    }
    
    /* Aesthetic 3D Result Box */
    .garden-result {
        margin-top: 30px;
        padding: 25px;
        background: #ffffff;
        border-radius: 24px;
        border: 4px solid #14532d;
        box-shadow: 6px 6px 0px #14532d;
        text-align: center;
    }
    
    .garden-badge {
        display: inline-block;
        padding: 8px 18px;
        font-size: 15px;
        font-weight: 900;
        border-radius: 30px;
        border: 3px solid #14532d;
        box-shadow: 2px 2px 0px #14532d;
        margin-bottom: 15px;
        font-family: 'Comic Sans MS', sans-serif;
    }
    
    .garden-score {
        font-size: 42px;
        font-weight: 900;
        color: #14532d;
        font-family: 'Comic Sans MS', sans-serif;
        margin: 5px 0;
    }
    
    .garden-subtext {
        font-size: 13px;
        color: #166534;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Load your custom KNeighborsRegressor pipeline safely
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"🌱 Oh no! Error loading model binary: {e}")
    st.stop()

# Wrap whole UI inside a centralized card container block
st.markdown('<div class="garden-card">', unsafe_allow_html=True)

# Cute Floral Cartoon Header Bubble
st.markdown("""
    <div class="bubble-header">
        <h1 class="bubble-title">🏡 Fairy Cottage Appraiser 🌸</h1>
        <div class="bubble-subtitle">Let's calculate the value of your dream home! 🌷✨🎈</div>
    </div>
""", unsafe_allow_html=True)

# Form layout mapped perfectly to model.feature_names_in_
col1, col2 = st.columns(2)

with col1:
    idx = st.number_input("🆔 Property Identification ID", min_value=1, max_value=3000, value=1461, step=1)
    overall_qual = st.slider("⭐ Overall Material Quality (1-10)", min_value=1, max_value=10, value=6, step=1)
    gr_liv_area = st.number_input("📐 Above Ground Living Area (SqFt)", min_value=300, max_value=6000, value=1500, step=50)
    total_bsmt_sf = st.number_input("🧱 Total Basement Area (SqFt)", min_value=0, max_value=6000, value=1000, step=50)
    lot_area = st.number_input("🍀 Total Lot Land Area (SqFt)", min_value=500, max_value=100000, value=10000, step=250)

with col2:
    year_built = st.number_input("📅 Original Construction Year", min_value=1800, max_value=2026, value=1975, step=1)
    garage_cars = st.slider("🚗 Garage Car Capacity", min_value=0, max_value=5, value=2, step=1)
    full_bath = st.slider("🛁 Full Bathrooms Above Ground", min_value=0, max_value=4, value=2, step=1)
    bedroom_abv_gr = st.slider("🛌 Bedrooms Above Ground", min_value=0, max_value=8, value=3, step=1)

st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

# Execution Action State
if st.button("🔮 Cast Appraiser Spell! ✨"):
    # Array mapping exactly to: Id, OverallQual, GrLivArea, GarageCars, TotalBsmtSF, YearBuilt, FullBath, BedroomAbvGr, LotArea
    features = np.array([[
        idx, overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, year_built, full_bath, bedroom_abv_gr, lot_area
    ]])
    
    # Process prediction value from KNeighborsRegressor
    prediction = float(model.predict(features)[0])
    
    # Determine custom badges dynamically based on valuation
    if prediction >= 250000:
        badge_bg, badge_text = "#dcfce7", "🏰 Grand Royal Palace! 💎"
    elif prediction >= 140000:
        badge_bg, badge_text = "#fef9c3", "🏡 Sweet Cozy Cottage! ✨"
    else:
        badge_bg, badge_text = "#fee2e2", "🍄 Little Tiny Mushroom Treehouse! 🌱"
        
    # Render cute aesthetic 3D result card
    st.markdown(f"""
        <div class="garden-result">
            <span class="garden-badge" style="background-color: {badge_bg}; color: #14532d;">
                {badge_text}
            </span>
            <div class="garden-score">🌸 ${prediction:,.2f}</div>
            <p class="garden-subtext">Calculated perfectly by your magical forest helper bot!</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
