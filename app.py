import streamlit as st

st.set_page_config(
    page_title="Ensemble Methods Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .method-card {
        background: #f8fafc;
        border-left: 4px solid #667eea;
        padding: 1rem 1.2rem;
        border-radius: 0 8px 8px 0;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🤖 Ensemble Methods Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload your dataset · Explore · Train Bagging, Boosting & Stacking models</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="method-card">
        <strong>🎒 Bagging</strong><br>
        <small>Parallel training on bootstrap samples · Reduces variance · Random Forest</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="method-card" style="border-color: #f59e0b;">
        <strong>⚡ Boosting</strong><br>
        <small>Sequential error correction · Reduces bias · XGBoost / AdaBoost / GBM</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="method-card" style="border-color: #10b981;">
        <strong>📚 Stacking</strong><br>
        <small>Diverse learners + meta-model · Most flexible · Learns to combine</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### 🚀 How to use this app

1. **Upload Data** → Go to **📁 Upload & EDA** in the sidebar to upload your CSV, Excel, or TXT file and explore it
2. **Train Models** → Head to **🎒 Bagging**, **⚡ Boosting**, or **📚 Stacking** to train each ensemble method
3. **Compare** → Visit **📊 Model Comparison** to see all models side-by-side

> ✅ Supports **classification** and **regression** tasks — auto-detected from your target column.
""")

st.info("👈 Use the sidebar to navigate between pages.")
