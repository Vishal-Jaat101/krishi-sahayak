"""
app.py

This is the main Streamlit application for KrishiSahayak.
It features a single-page mobile-first dashboard with an English/Hindi toggle,
a Crop Leaf Scan diagnostic panel, a unified Chat interface, and quick farming tools.
"""

import os
import asyncio
import streamlit as st
from PIL import Image
import io
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the workflow runner
from agent_graph import run_krishisahayak

# 1. UI Configuration & Responsive Styling
st.set_page_config(
    page_title="KrishiSahayak - AI Farmer Companion",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium CSS for HSL colors, responsive design, and fonts
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

/* Font Override */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* Base style adjustments */
.main-title {
    font-weight: 700;
    color: #2e6f40;
    margin-bottom: 0px;
}
.sub-title {
    font-weight: 400;
    color: #7da086;
    margin-top: 0px;
    margin-bottom: 20px;
}

/* Card layout for mock info & stats */
.farming-card {
    background-color: rgba(46, 111, 64, 0.08);
    border: 1px solid rgba(46, 111, 64, 0.2);
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
}
.farming-card h4 {
    margin-top: 0px;
    color: #1b4d2b;
}

/* Micro-interaction effects on sidebar inputs */
div[data-testid="stSidebar"] {
    background-color: #f7f9f6;
    border-right: 1px solid #e1e7e0;
}

/* Custom button styling */
.stButton > button {
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s ease;
}
</style>
""", unsafe_allow_html=True)


# 2. Multi-lingual UI Strings Dictionary
UI_STRINGS = {
    "en": {
        "title": "🌾 KrishiSahayak",
        "subtitle": "Smart AI Agronomist & Farmer Companion",
        "tagline": "Empowering Rajasthan's farmers with Google ADK 2.0 and Gemini 2.5 Flash",
        "api_key_header": "🔑 API Configuration",
        "api_key_label": "Enter Gemini API Key",
        "api_key_help": "Get your key from Google AI Studio. Sourced from environment by default.",
        "api_key_env": "✅ Sourced from system environment",
        "api_key_missing": "⚠️ API Key not found. Please enter it below:",
        "lang_toggle": "🌐 Choose Language / भाषा चुनें",
        "location_header": "📍 Location Context",
        "location_val": "Bharatpur, Rajasthan",
        "land_header": "📐 Farmer Profile Settings",
        "land_label": "Landholding Size (Hectares)",
        "diagnose_tab": "📷 Crop Leaf Scan (रोग जांच)",
        "chat_tab": "💬 Krishi Chatbot (सलाहकार)",
        "upload_label": "Upload leaf image for disease diagnosis...",
        "upload_help": "Supports JPG, JPEG, or PNG.",
        "diagnose_btn": "🔍 Analyze Crop Health",
        "diagnosing": "Analyzing crop image with Gemini 2.5 Flash...",
        "diagnosis_result": "Crop Health Diagnosis Report",
        "chat_placeholder": "Ask about Mustard rates, solar pump subsidies, or irrigation advice...",
        "quick_actions": "🚀 Quick Actions",
        "action_mandi": "📈 Mustard Mandi Rate",
        "action_weather": "🌦️ 5-Day Irrigation Weather",
        "action_schemes": "📜 Check Subsidies",
        "mandi_prompt": "What are the current mandi rates and 30-day trends for Mustard?",
        "weather_prompt": "Show me the 5-day weather forecast and irrigation advice for Bharatpur.",
        "scheme_prompt": "Which Rajasthan agricultural schemes am I eligible for with {} hectares of land?",
        "system_info": "📊 System Architecture Info",
        "powered_by": "Powered by Gemini 2.5 Flash & Google ADK 2.0 Graph Workflow API"
    },
    "hi": {
        "title": "🌾 कृषि सहायक",
        "subtitle": "स्मार्ट एआई कृषि विशेषज्ञ और किसान मित्र",
        "tagline": "गूगल ADK 2.0 और जेमिनी 2.5 फ्लैश द्वारा संचालित",
        "api_key_header": "🔑 एपीआई कॉन्फ़िगरेशन",
        "api_key_label": "जेमिनी एपीआई कुंजी दर्ज करें",
        "api_key_help": "गूगल एआई स्टूडियो से कुंजी प्राप्त करें। डिफ़ॉल्ट रूप से पर्यावरण से ली गई है।",
        "api_key_env": "✅ सिस्टम पर्यावरण से प्राप्त कुंजी",
        "api_key_missing": "⚠️ एपीआई कुंजी नहीं मिली। कृपया दर्ज करें:",
        "lang_toggle": "🌐 Choose Language / भाषा चुनें",
        "location_header": "📍 स्थान संदर्भ",
        "location_val": "भरतपुर, राजस्थान",
        "land_header": "📐 किसान प्रोफ़ाइल सेटिंग्स",
        "land_label": "भूमि का आकार (हेक्टेयर में)",
        "diagnose_tab": "📷 फसल रोग जांच (Crop Scan)",
        "chat_tab": "💬 कृषि चैटबॉट (Krishi Chat)",
        "upload_label": "रोग निदान के लिए पत्ती की छवि अपलोड करें...",
        "upload_help": "JPG, JPEG, या PNG फाइलों का समर्थन।",
        "diagnose_btn": "🔍 फसल स्वास्थ्य का विश्लेषण करें",
        "diagnosing": "जेमिनी 2.5 फ्लैश द्वारा विश्लेषण किया जा रहा है...",
        "diagnosis_result": "फसल स्वास्थ्य निदान रिपोर्ट",
        "chat_placeholder": "सरसों के भाव, सोलर पंप सब्सिडी, या सिंचाई सलाह के बारे में पूछें...",
        "quick_actions": "🚀 त्वरित क्रियाएं",
        "action_mandi": "📈 सरसों का मंडी भाव",
        "action_weather": "🌦️ ५-दिवसीय सिंचाई मौसम",
        "action_schemes": "📜 सरकारी अनुदान चेक करें",
        "mandi_prompt": "सरसों के वर्तमान मंडी भाव और 30 दिनों के रुझान क्या हैं?",
        "weather_prompt": "भरतपुर के लिए 5 दिवसीय मौसम पूर्वानुमान और सिंचाई सलाह दिखाएं।",
        "scheme_prompt": "मेरी {} हेक्टेयर भूमि के लिए मैं किन सरकारी कृषि योजनाओं के लिए पात्र हूं?",
        "system_info": "📊 सिस्टम आर्किटेक्चर जानकारी",
        "powered_by": "जेमिनी 2.5 फ्लैश और गूगल ADK 2.0 ग्राफ वर्कफ़्लो एपीआई द्वारा संचालित"
    }
}


# 3. Sidebar Configuration (Key, Profile Settings, and Concepts)
st.sidebar.markdown(f"## KrishiSahayak Config")

# Language Selector
lang_option = st.sidebar.selectbox(
    "Select Language / भाषा चुनें",
    options=["English", "हिन्दी"],
    index=0
)
lang = "hi" if lang_option == "हिन्दी" else "en"
texts = UI_STRINGS[lang]

st.sidebar.divider()

# API Key Check
api_key = os.environ.get("GEMINI_API_KEY")

if api_key:
    st.sidebar.success(texts["api_key_env"])
else:
    st.sidebar.error("⚠️ GEMINI_API_KEY not found in environment!")

st.sidebar.divider()

# Farmer settings context (land size injected into scheme tool automatically)
st.sidebar.markdown(f"### {texts['land_header']}")
land_size = st.sidebar.number_input(
    texts["land_label"],
    min_value=0.0,
    max_value=100.0,
    value=1.5,
    step=0.1
)

st.sidebar.markdown(f"### {texts['location_header']}")
st.sidebar.info(texts["location_val"])

st.sidebar.divider()

# ASCII Concepts documentation in sidebar for Hack2Skill & Kaggle judges
st.sidebar.markdown(f"### {texts['system_info']}")
st.sidebar.code("""
[User Request]
      │
      ▼
┌──────────────┐
│  Guardrail   ├─► [Reject] (In Hindi)
└──────┬───────┘
       │ (Safe)
       ▼
┌──────────────┐
│ ADK 2.0 Graph│
│ Router Node  │
└──────┬───────┘
       ├─► [Disease Vision Node]
       ├─► [Mandi Price Tool]
       ├─► [Weather Irrigation Tool]
       └─► [Scheme Eligibility Tool]
""", language="text")


# 4. Main Panel Header
st.markdown(f"<h1 class='main-title'>{texts['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='sub-title'>{texts['subtitle']} — <em>{texts['tagline']}</em></p>", unsafe_allow_html=True)


# 5. Core Interface Tabs
tab_scan, tab_chat = st.tabs([texts["diagnose_tab"], texts["chat_tab"]])

# TAB 1: CROP DISEASE DIAGNOSIS (VISION NODE)
with tab_scan:
    st.markdown(f"### {texts['diagnose_tab']}")
    uploaded_file = st.file_uploader(
        texts["upload_label"],
        type=["jpg", "jpeg", "png"],
        help=texts["upload_help"]
    )
    
    if uploaded_file is not None:
        # Show uploaded image in a responsive layout container
        col_img, col_diag = st.columns([1, 2])
        with col_img:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Crop Sample", use_container_width=True)
            
        with col_diag:
            diagnose_btn = st.button(texts["diagnose_btn"])
            if diagnose_btn:
                if not api_key:
                    st.error("Please provide a Gemini API Key in the sidebar to run the diagnosis.")
                else:
                    with st.spinner(texts["diagnosing"]):
                        # Convert image to bytes for ADK workflow Part.from_bytes input
                        img_byte_arr = io.BytesIO()
                        image.save(img_byte_arr, format=image.format if image.format else "JPEG")
                        img_bytes = img_byte_arr.getvalue()
                        img_mime = uploaded_file.type
                        
                        # Execute ADK Workflow vision node
                        diagnosis_report = asyncio.run(run_krishisahayak(
                            user_query="Diagnose crop leaf health",
                            image_bytes=img_bytes,
                            image_mime=img_mime,
                            language=lang,
                            api_key=api_key
                        ))
                        
                        st.markdown(f"#### {texts['diagnosis_result']}")
                        st.info(diagnosis_report)


# TAB 2: UNIFIED CHATBOT WITH QUICK ACTIONS (MCP TOOLS & GENERAL ADVICE)
with tab_chat:
    st.markdown(f"### {texts['chat_tab']}")
    
    # 2a. Quick actions dashboard layout
    st.markdown(f"**{texts['quick_actions']}**")
    col1, col2, col3 = st.columns(3)
    
    prefilled_prompt = None
    
    with col1:
        if st.button(texts["action_mandi"], use_container_width=True):
            prefilled_prompt = texts["mandi_prompt"]
    with col2:
        if st.button(texts["action_weather"], use_container_width=True):
            prefilled_prompt = texts["weather_prompt"]
    with col3:
        if st.button(texts["action_schemes"], use_container_width=True):
            # Injects the land size dynamically from sidebar
            prefilled_prompt = texts["scheme_prompt"].format(land_size)
            
    # 2b. Setup chat state history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Render chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # Process prefilled quick action if clicked
    if prefilled_prompt:
        st.session_state.messages.append({"role": "user", "content": prefilled_prompt})
        with st.chat_message("user"):
            st.markdown(prefilled_prompt)
            
        with st.chat_message("assistant"):
            if not api_key:
                response = "Error: Please set your GEMINI_API_KEY in the sidebar to chat."
                st.error(response)
            else:
                with st.spinner("KrishiSahayak is thinking..."):
                    response = asyncio.run(run_krishisahayak(
                        user_query=prefilled_prompt,
                        language=lang,
                        api_key=api_key
                    ))
                    st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

    # 2c. Handle text input from user
    if chat_input := st.chat_input(texts["chat_placeholder"]):
        st.session_state.messages.append({"role": "user", "content": chat_input})
        with st.chat_message("user"):
            st.markdown(chat_input)
            
        with st.chat_message("assistant"):
            if not api_key:
                response = "Error: Please set your GEMINI_API_KEY in the sidebar to chat."
                st.error(response)
            else:
                with st.spinner("KrishiSahayak is thinking..."):
                    response = asyncio.run(run_krishisahayak(
                        user_query=chat_input,
                        language=lang,
                        api_key=api_key
                    ))
                    st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()


# Footer
st.divider()
st.markdown(f"<p style='text-align: center; color: gray; font-size: 0.8rem;'>{texts['powered_by']}</p>", unsafe_allow_html=True)
