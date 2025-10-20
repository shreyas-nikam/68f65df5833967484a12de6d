import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="QuLab - AI Career Navigator", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()

st.title("QuLab - AI Career Navigator & Pathway Planner")
st.divider()

st.markdown("""
## Welcome to the AI Career Navigator & Pathway Planner

In this lab, you will explore the **AI-Readiness Score (AI-R)** framework, a comprehensive model designed to quantify your preparedness for AI-enabled careers. This interactive application enables you to:

- **Understand** the key components that contribute to career readiness in AI-driven labor markets
- **Calculate** your personalized AI-Readiness Score based on individual capabilities and market opportunities
- **Simulate** the impact of various learning pathways on your career trajectory
- **Analyze** different career paths through interactive "what-if" scenarios

### The AI-Readiness Score Framework

The AI-Readiness Score combines three critical dimensions:

1. **Idiosyncratic Readiness ($V^R$)**: Your individual capabilities across AI-Fluency, Domain-Expertise, and Adaptive-Capacity
2. **Systematic Opportunity ($H^R$)**: Market demand and opportunity for specific occupations
3. **Synergy**: The alignment between your skills and market requirements

The core formula is:

$$AI-R_{i,t} = \\alpha \\cdot V^R_i(t) + (1-\\alpha) \\cdot H^R_i(t) + \\beta \\cdot \\text{Synergy\\%}(V^R, H^R)$$

Where:
- $\\alpha \\in [0,1]$ represents the weight on individual factors vs. market factors
- $\\beta > 0$ is the synergy coefficient that amplifies alignment
- Both $V^R$ and $H^R$ are normalized to $[0, 100]$

### How to Use This Application

Navigate through the pages using the sidebar:
- **Page 1**: Calculate your current AI-Readiness Score
- **Page 2**: Simulate learning pathway impacts and explore career transitions
- **Page 3**: View and analyze the underlying data and advanced metrics

Each page provides interactive controls, real-time calculations, and visualizations to help you understand and optimize your AI career readiness.
""")

st.divider()

# Navigation
page = st.sidebar.selectbox(
    label="📊 Navigation",
    options=["Page 1: AI-Readiness Calculator", 
             "Page 2: Pathway Simulator", 
             "Page 3: Data Explorer & Advanced Metrics"]
)

if page == "Page 1: AI-Readiness Calculator":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2: Pathway Simulator":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3: Data Explorer & Advanced Metrics":
    from application_pages.page3 import run_page3
    run_page3()
