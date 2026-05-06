import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Booklet", page_icon="📚", layout="centered")
st.title("📚 Booklet")
st.caption("A personalised book recommender powered by collaborative filtering")

# --- Load users ---
@st.cache_data
def load_users():
    response = requests.get(f"{API_URL}/users")
    return response.json()["users"]

users = load_users()

# --- UI ---
st.subheader("Get Recommendations")

selected_user = st.selectbox(
    "Select a user",
    options=users,
    format_func=lambda x: x[:16] + "..."  # truncate long IDs
)

n = st.slider("Number of recommendations", min_value=5, max_value=20, value=10)

if st.button("Get Recommendations", type="primary"):
    with st.spinner("Finding books you'll love..."):
        response = requests.get(f"{API_URL}/recommend/{selected_user}?n={n}")
    
    if response.status_code == 200:
        data = response.json()
        recommendations = data["recommendations"]
        
        st.success(f"Top {n} recommendations for user {selected_user[:8]}...")
        
        for i, book in enumerate(recommendations, 1):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{i}. {book['title']}**")
            with col2:
                st.metric("Predicted", f"⭐ {book['predicted_rating']}")
            st.divider()
    else:
        st.error("Something went wrong. Is the API running?")