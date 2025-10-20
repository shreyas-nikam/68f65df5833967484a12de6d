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

st.markdown(\"\"\"
## Welcome to the AI Career Navigator & Pathway Planner

In this lab, you will explore the **AI-Readiness Score (AI-R)** framework, a comprehensive parametric model designed to quantify an individual's preparedness for AI-enabled careers. This interactive application enables you to:

- **Understand** the decomposition of the AI-Readiness Score into its core components
- **Calculate** your personal AI-R score based on individual capabilities and market opportunities
- **Simulate** the impact of various learning pathways on your career readiness
- **Analyze** different career paths through dynamic "what-if" scenarios

### The AI-Readiness Score Framework

The AI-Readiness Score combines three essential dimensions:

1. **Idiosyncratic Readiness ($V^R$)**: Your individual capabilities across AI-Fluency, Domain-Expertise, and Adaptive-Capacity
2. **Systematic Opportunity ($H^R$)**: Market demand and growth potential for AI-enabled occupations
3. **Synergy Component**: The alignment between your skills and market requirements

The core formula is:

\"\"\"
)

st.latex(r\"\"\"AI-R_{i,t} = \\alpha \\cdot V^R_i(t) + (1-\\alpha) \\cdot H^R_i(t) + \\beta \\cdot \\text{Synergy}\\%(V^R, H^R)\"\"\")

st.markdown(\"\"\"
Where:
- $V^R(t)$ is your **Idiosyncratic Readiness** (normalized to [0, 100])
- $H^R(t)$ is the **Systematic Opportunity** for your target occupation (normalized to [0, 100])
- $\\alpha \\in [0,1]$ weights individual vs. market factors
- $\\beta > 0$ amplifies the synergy when skills align with market needs
- **Synergy%** captures the alignment between your capabilities and market demands (normalized to [0, 100])

This framework empowers you to make data-driven career decisions and optimize your learning investments.
\"\"\"
)

st.divider()

# Navigation
page = st.sidebar.selectbox(
    label="📊 Navigation",
    options=["Page 1: Calculate AI-Readiness Score", 
             "Page 2: What-If Scenario Analysis", 
             "Page 3: Data Explorer"]
)

if page == "Page 1: Calculate AI-Readiness Score":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2: What-If Scenario Analysis":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3: Data Explorer":
    from application_pages.page3 import run_page3
    run_page3()
