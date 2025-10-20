import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="QuLab - AI-Readiness Score", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()

st.title("QuLab: AI Career Navigator & Pathway Planner")
st.divider()

st.markdown(\"\"\"
## Introduction

This lab implements the **AI-Readiness Score (AI-R)** framework, enabling you to understand, calculate, and simulate your career readiness in AI-driven labor markets. 

The application provides an interactive environment to explore how individual capabilities, market opportunities, and learning pathways impact career prospects in the age of AI.

### Learning Goals

- **Understand** the AI-Readiness Score framework and its key components
- **Decompose** the AI-R score into systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components
- **Evaluate** the potential impact of various learning pathways on skill development and career readiness
- **Analyze** different career paths through "what-if" scenarios based on market demand and personal capabilities

### The AI-Readiness Score Formula

The core formula for calculating the AI-Readiness Score for an individual $i$ at time $t$ is:

$$AI-R_{i,t} = \\alpha \\cdot V^R_i(t) + (1-\\alpha) \\cdot H^R_i(t) + \\beta \\cdot \\text{Synergy}\\%(V^R, H^R)$$

**Where:**
- $V^R(t)$ = **Idiosyncratic Readiness** (individual capability)
- $H^R(t)$ = **Systematic Opportunity** (market demand)
- $\\alpha \\in [0,1]$ = weight on individual vs. market factors
- $\\beta > 0$ = Synergy coefficient
- Both $V^R$ and $H^R$ are normalized to $[0, 100]$
- $\\text{Synergy}\\%$ is normalized to $[0, 100]$ percentage units

This framework enables dynamic scenario planning to understand how learning pathways and career transitions impact future prospects.

### Navigation

Use the sidebar to navigate between different pages:
- **Page 1: Personal Profile & VR Calculation** - Input your skills and calculate your Idiosyncratic Readiness
- **Page 2: Market Analysis & HR Calculation** - Explore occupational opportunities and calculate Systematic Opportunity
- **Page 3: AI-Readiness Score & Pathway Simulation** - Calculate your complete AI-R score and simulate learning pathways

\"\"\"
)

st.divider()

# Navigation
page = st.sidebar.selectbox(
    label="Navigation",
    options=["Page 1: Personal Profile & VR", "Page 2: Market Analysis & HR", "Page 3: AI-Readiness & Pathways"]
)

if page == "Page 1: Personal Profile & VR":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2: Market Analysis & HR":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3: AI-Readiness & Pathways":
    from application_pages.page3 import run_page3
    run_page3()
