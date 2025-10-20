import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def run_page1():
    st.header("📊 Overview & Setup")
    st.markdown("""
    This page provides an overview of the AI-Readiness Score framework and displays the synthetic datasets 
    used throughout the application. These datasets represent individual profiles, occupational opportunities, 
    learning pathways, and skill requirements.
    """)
    
    # Initialize session state for data if not already present
    if 'individual_profiles_df' not in st.session_state:
        initialize_data()
    
    st.divider()
    
    # Display the three main components
    st.subheader("🎯 Core Components of AI-Readiness Score")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 1️⃣ Idiosyncratic Readiness ($V^R$)
        
        Measures **individual capability** through three key dimensions:
        
        **🤖 AI-Fluency** - Your proficiency with AI tools and technologies
        - Technical AI Skills ($S_{i,1}$)
        - AI-Augmented Productivity ($S_{i,2}$)
        - Critical AI Judgment ($S_{i,3}$)
        - AI Learning Velocity ($S_{i,4}$)
        
        **📚 Domain-Expertise** - Your professional knowledge and experience
        - Education Foundation ($E_{\\text{education}}$)
        - Practical Experience ($E_{\\text{experience}}$)
        - Specialization Depth ($E_{\\text{specialization}}$)
        
        **🔄 Adaptive-Capacity** - Your ability to adapt and evolve
        - Cognitive Flexibility
        - Social-Emotional Intelligence
        - Strategic Career Management
        """)
    
    with col2:
        st.markdown("""
        ### 2️⃣ Systematic Opportunity ($H^R$)
        
        Evaluates **market demand** for AI-enabled roles:
        
        **Base Opportunity Score ($H_{\\text{base}}$)**
        - AI-Enhancement Potential
        - Job Growth Projection
        - Wage Premium
        - Entry Accessibility
        
        **Market Multipliers**
        - Growth Multiplier ($M_{\\text{growth}}$)
        - Regional Multiplier ($M_{\\text{regional}}$)
        
        Final calculation:
        """)
        st.latex(r"H^R = H_{\\text{base}} \\cdot M_{\\text{growth}} \\cdot M_{\\text{regional}}")
    
    with col3:
        st.markdown("""
        ### 3️⃣ Synergy Component
        
        Measures the **alignment** between your skills and market needs:
        
        **Skills Match Score**
        - Comparison of individual skills with required skills
        - Weighted by skill importance
        
        **Timing Factor**
        - Considers years of experience
        
        **Alignment Factor**
        - Combines skills match with timing
        
        **Synergy Percentage**
        """)
        st.latex(r"\\text{Synergy}\\% = \\frac{V^R \\cdot H^R \\cdot \\text{Alignment}}{100.0}")
    
    st.divider()
    
    # Data Display Section
    st.subheader("📁 Synthetic Datasets")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Individual Profiles", 
        "Occupational Data", 
        "Learning Pathways", 
        "Required Skills", 
        "Individual Skills"
    ])
    
    with tab1:
        st.markdown("""
        **Individual Profiles Dataset**
        
        This dataset contains individual capability metrics including AI-fluency components, 
        domain expertise indicators, and adaptive capacity measures.
        """)
        st.dataframe(st.session_state.individual_profiles_df, use_container_width=True)
        
    with tab2:
        st.markdown("""
        **Occupational Data Dataset**
        
        This dataset includes market opportunity metrics for various AI-enabled occupations, 
        including job growth rates, wage premiums, and accessibility factors.
        """)
        st.dataframe(st.session_state.occupational_data_df, use_container_width=True)
        
        # Visualization of occupational opportunities
        st.markdown("#### Occupational Comparison")
        fig = px.scatter(
            st.session_state.occupational_data_df,
            x='ai_enhancement_score',
            y='ai_skilled_wage',
            size='job_growth_rate_g',
            color='occupation_name',
            hover_data=['education_years_required', 'experience_years_required'],
            title='AI Enhancement vs Wage (size = growth rate)',
            labels={
                'ai_enhancement_score': 'AI Enhancement Score',
                'ai_skilled_wage': 'AI-Skilled Wage ($)',
                'occupation_name': 'Occupation'
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with tab3:
        st.markdown("""
        **Learning Pathways Dataset**
        
        This dataset describes various learning pathways and their expected impact on 
        AI-fluency, domain expertise, and adaptive capacity.
        """)
        st.dataframe(st.session_state.learning_pathways_df, use_container_width=True)
        
        # Visualization of pathway impacts
        st.markdown("#### Learning Pathway Impact Comparison")
        pathway_impacts = st.session_state.learning_pathways_df[
            ['pathway_name', 'impact_ai_fluency', 'impact_domain_expertise', 'impact_adaptive_capacity']
        ].set_index('pathway_name')
        
        fig = go.Figure()
        fig.add_trace(go.Bar(name='AI-Fluency Impact', x=pathway_impacts.index, y=pathway_impacts['impact_ai_fluency']))
        fig.add_trace(go.Bar(name='Domain Expertise Impact', x=pathway_impacts.index, y=pathway_impacts['impact_domain_expertise']))
        fig.add_trace(go.Bar(name='Adaptive Capacity Impact', x=pathway_impacts.index, y=pathway_impacts['impact_adaptive_capacity']))
        
        fig.update_layout(
            title='Expected Impact by Learning Pathway',
            xaxis_title='Learning Pathway',
            yaxis_title='Impact Score',
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with tab4:
        st.markdown("""
        **Occupation Required Skills Dataset**
        
        This dataset specifies the skills required for each occupation, along with 
        required proficiency levels and skill importance weights.
        """)
        st.dataframe(st.session_state.occupation_required_skills_df, use_container_width=True)
        
    with tab5:
        st.markdown("""
        **Individual Skills Dataset**
        
        This dataset contains the current skill levels for individuals, which will be 
        matched against occupation requirements to calculate synergy.
        """)
        st.dataframe(st.session_state.individual_skills_df, use_container_width=True)
    
    st.divider()
    
    st.info("""
    💡 **Next Steps:** 
    - Navigate to **"Calculate AI-Readiness Score"** to input your personal data and calculate your AI-R score
    - Then explore **"Pathway Simulation"** to see how different learning paths can improve your score
    """)


def initialize_data():
    """Initialize all synthetic datasets in session state"""
    
    # Individual Profiles Data
    individual_profiles_data = {
        'user_id': [1],
        'prompting_score': [0.75],
        'tools_score': [0.6],
        'understanding_score': [0.8],
        'datalit_score': [0.9],
        'output_quality_with_ai': [90],
        'output_quality_without_ai': [60],
        'time_without_ai': [4],
        'time_with_ai': [1],
        'errors_caught': [15],
        'total_ai_errors': [20],
        'appropriate_trust_decisions': [25],
        'total_decisions': [30],
        'delta_proficiency': [0.3],
        'delta_t_hours_invested': [10],
        'education_level': ["Master's"],
        'years_experience': [5],
        'portfolio_score': [0.85],
        'recognition_score': [0.7],
        'credentials_score': [0.9],
        'cognitive_flexibility': [85],
        'social_emotional_intelligence': [90],
        'strategic_career_management': [75]
    }
    st.session_state.individual_profiles_df = pd.DataFrame(individual_profiles_data)
    
    # Occupational Data
    occupational_data = {
        'occupation_name': [
            'Data Analyst with AI Skills',
            'AI UX Researcher',
            'AI Prompt Engineer',
            'Data Scientist',
            'Nursing Informatics',
            'Medical Coding'
        ],
        'ai_enhancement_score': [0.8, 0.9, 0.7, 0.95, 0.75, 0.6],
        'job_growth_rate_g': [0.25, 0.35, 0.4, 0.3, 0.2, 0.15],
        'ai_skilled_wage': [120000, 130000, 140000, 150000, 110000, 90000],
        'median_wage': [90000, 95000, 100000, 110000, 85000, 70000],
        'education_years_required': [4, 4, 4, 4, 4, 2],
        'experience_years_required': [2, 3, 1, 3, 2, 0],
        'current_job_postings': [500, 400, 600, 700, 300, 200],
        'previous_job_postings': [400, 300, 450, 500, 250, 180],
        'remote_work_factor': [0.6, 0.7, 0.8, 0.5, 0.4, 0.3],
        'local_demand': [1.2, 1.1, 1.3, 1.4, 1.0, 0.9],
        'national_avg_demand': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    }
    st.session_state.occupational_data_df = pd.DataFrame(occupational_data)
    
    # Learning Pathways Data
    learning_pathways_data = {
        'pathway_id': [1, 2, 3],
        'pathway_name': [
            'Prompt Engineering Fundamentals',
            'AI for Financial Analysis',
            'Human-AI Collaboration'
        ],
        'pathway_type': ['AI-Fluency', 'Domain+AI Integration', 'Adaptive Capacity'],
        'impact_ai_fluency': [0.2, 0.1, 0.05],
        'impact_domain_expertise': [0.05, 0.2, 0.1],
        'impact_adaptive_capacity': [0.1, 0.05, 0.2]
    }
    st.session_state.learning_pathways_df = pd.DataFrame(learning_pathways_data)
    
    # Occupation Required Skills Data
    occupation_required_skills_data = {
        'occupation_name': ['Data Analyst with AI Skills'] * 3 + ['AI UX Researcher'] * 3,
        'skill_name': [
            'Python', 'Data Visualization', 'Machine Learning',
            'User Research', 'UI Design', 'AI Ethics'
        ],
        'required_skill_score': [80, 70, 60, 90, 80, 75],
        'skill_importance': [0.7, 0.8, 0.5, 0.9, 0.7, 0.6]
    }
    st.session_state.occupation_required_skills_df = pd.DataFrame(occupation_required_skills_data)
    
    # Individual Skills Data
    individual_skills_data = {
        'user_id': [1] * 3,
        'skill_name': ['Python', 'Data Visualization', 'Machine Learning'],
        'individual_skill_score': [70, 60, 40]
    }
    st.session_state.individual_skills_df = pd.DataFrame(individual_skills_data)
