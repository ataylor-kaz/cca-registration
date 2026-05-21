import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="CCA Registration Portal", page_icon="📘", layout="centered")

# Initialize an internal cache to save registrations as long as the app is running
if "registrations" not in st.session_state:
    st.session_state.registrations = []

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #16a085; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 16px; color: #7f8c8d; text-align: center; margin-bottom: 30px; }
    .category-header { font-size: 20px; font-weight: bold; color: #2c3e50; border-bottom: 2px solid #16a085; padding-bottom: 5px; margin-top: 25px; margin-bottom: 15px; }
    .cca-container { background-color: #f8f9fa; border-left: 4px solid #16a085; padding: 12px; margin-bottom: 10px; border-radius: 0 4px 4px 0; }
    .cca-name { font-weight: bold; font-size: 16px; color: #1a252f; }
    .framework-label { font-size: 13px; color: #7f8c8d; font-weight: bold; }
    .framework-value { font-size: 13px; color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

# Application Data Structured cleanly without text explanations
cca_data = {
    "🏆 Sports & Athletics": [
        {"name": "Football", "dofe": "Physical Recreation", "hpl": "Hard Working, Working Meaningfully with Others, Agile"},
        {"name": "Basketball", "dofe": "Physical Recreation", "hpl": "Working Meaningfully with Others, Advanced Thinking, Hard Working"},
        {"name": "Volleyball", "dofe": "Physical Recreation", "hpl": "Working Meaningfully with Others, Agile, Hard Working"},
        {"name": "Swimming", "dofe": "Physical Recreation", "hpl": "Hard Working, Meta-Cognition, Advanced Thinking"},
    ],
    "🎭 Speech Arts": [
        {"name": "School Play", "dofe": "Skills", "hpl": "Hard Working, Working Meaningfully with Others, Agile"},
        {"name": "Debate Sr", "dofe": "Skills", "hpl": "Advanced Thinking, Agile, Meta-Cognition"},
        {"name": "Debate Jr", "dofe": "Skills", "hpl": "Advanced Thinking, Hard Working, Working Meaningfully with Others"},
        {"name": "MUN & MUN Academy", "dofe": "Skills", "hpl": "Concern for Society, Advanced Thinking, Working Meaningfully with Others"},
        {"name": "LAMDA", "dofe": "Skills", "hpl": "Hard Working, Meta-Cognition, Agile"},
        {"name": "Kazakh Debate", "dofe": "Skills", "hpl": "Advanced Thinking, Agile, Hard Working"},
    ],
    "💻 Comp Sci / STEM": [
        {"name": "Comp Sci (Non-Competitive)", "dofe": "Skills", "hpl": "Intellectual Playfulness, Advanced Thinking, Hard Working"},
        {"name": "Computer Science Competitive", "dofe": "Skills", "hpl": "Advanced Thinking, Working Meaningfully with Others, Hard Working"},
        {"name": "Physics Extension (Olympiad)", "dofe": "Skills", "hpl": "Advanced Thinking, Agile, Hard Working"},
        {"name": "Chess", "dofe": "Skills", "hpl": "Advanced Thinking, Meta-Cognition"},
        {"name": "Maths Olympiad", "dofe": "Skills", "hpl": "Advanced Thinking, Intellectual Playfulness, Hard Working"},
    ],
    "🎵 Music, Art & Creative": [
        {"name": "Jazz Club", "dofe": "Skills", "hpl": "Agile, Working Meaningfully with Others, Hard Working"},
        {"name": "Dombra Ensemble", "dofe": "Skills", "hpl": "Concern for Society, Working Meaningfully with Others, Hard Working"},
        {"name": "Music Development Club", "dofe": "Skills", "hpl": "Intellectual Playfulness, Working Meaningfully with Others, Agile"},
        {"name": "Art Club (Y7-13)", "dofe": "Skills", "hpl": "Intellectual Playfulness, Meta-Cognition, Agile"},
        {"name": "Digital Animation", "dofe": "Skills", "hpl": "Agile, Intellectual Playfulness, Advanced Thinking"},
    ],
    "📚 Humanities & Languages": [
        {"name": "Literature Society: Read a Great Novel", "dofe": "Skills", "hpl": "Advanced Thinking, Agile, Intellectual Playfulness"},
        {"name": "Creative Writing", "dofe": "Skills", "hpl": "Intellectual Playfulness, Agile, Meta-Cognition"},
        {"name": "Philosophy", "dofe": "Skills", "hpl": "Advanced Thinking, Agile, Concern for Society"},
        {"name": "MFL Speaking French", "dofe": "Skills", "hpl": "Advanced Thinking, Hard Working, Agile"},
        {"name": "MFL Speak Mandarin", "dofe": "Skills", "hpl": "Hard Working, Advanced Thinking, Agile"},
        {"name": "Business Economics & Finance Society", "dofe": "Skills", "hpl": "Advanced Thinking, Concern for Society, Intellectual Playfulness"},
    ],
    "🌍 Service, Sustainability & Leadership": [
        {"name": "DofE Silver / Bronze", "dofe": "Core Program Framework", "hpl": "Hard Working, Working Meaningfully with Others, Meta-Cognition"},
        {"name": "Charity and Service (combination)", "dofe": "Voluntary Service", "hpl": "Concern for Society, Working Meaningfully with Others, Intellectual Playfulness"},
        {"name": "Eco Committee", "dofe": "Voluntary Service", "hpl": "Concern for Society, Intellectual Playfulness, Working Meaningfully with Others"},
    ]
}

# Flatten list for selection menus
all_ccas_flat = ["Select an option..."] + [item["name"] for cat in cca_data.
