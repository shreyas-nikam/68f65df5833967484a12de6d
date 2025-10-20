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

In this lab, you will explore the **AI-Readiness Score (AI-R)** framework, a parametric model designed to quantify an individual's preparedness for AI-enabled careers. This interactive application enables you to:

- **Understand** the decomposition of the AI-Readiness Score into systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components
- **Calculate** your personal AI-Readiness Score based on individual capabilities and market opportunities
- **Simulate** the impact of various learning pathways on your career readiness
- **Analyze** different career paths through interactive "what-if" scenarios

### The AI-Readiness Score Formula

The core formula for the AI-Readiness Score for an individual $i$ at time $t$ is:
""")

st.latex(r"AI-R_{i,t} = \\alpha \\cdot V^R_i(t) + (1-\\alpha) \\cdot H^R_i(t) + \\beta \\cdot \\text{Synergy}\\%(V^R, H^R)")

st.markdown("""
**Where:**
- $V^R(t)$ is the **Idiosyncratic Readiness** (individual capability)
- $H^R(t)$ is the **Systematic Opportunity** (market demand)
- $\\alpha \\in [0,1]$ is the weight on individual vs. market factors
- $\\beta > 0$ is the Synergy coefficient
- Both $V^R$ and $H^R$ are normalized to $[0, 100]$
- $\\text{Synergy}\\%$ is also normalized to $[0, 100]$ percentage units

This framework allows for dynamic "what-if" scenario planning, enabling you to understand how different learning pathways and career transitions impact your future career prospects.
""")

st.divider()

# Navigation
page = st.sidebar.selectbox(
    label="Navigation",
    options=["Overview & Setup", "Calculate AI-Readiness Score", "Pathway Simulation"]
)

if page == "Overview & Setup":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Calculate AI-Readiness Score":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Pathway Simulation":
    from application_pages.page3 import run_page3
    run_page3()
