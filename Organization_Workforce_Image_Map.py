#
# Organization Image Map 
# Created by: Luis Vera
#

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.markdown("# Organization Image Map")
st.write(
    """
    An organization image map is a visual representation of a company’s workforce, showing departments, roles, and employee demographics. But why create one? Beyond gaining insight into organizational roles and pay bands, an image map can reveal potential current and future challenges. This is especially useful for addressing the common misconception that companies should maintain a pyramid structure—a model that often doesn’t reflect the needs of today’s organizations. Let’s explore this concept further with a case study. 
    """
)

st.markdown("##### Case Study Introduction: A CRISPR-Based Gene Editing Company 🧬")
st.write(
    """
    Imagine a biotech startup specializing in gene editing, with around 200 employees distributed across R&D, Manufacturing & Production, Sales & Marketing, and an Executive Leadership team. Our objective is to examine how this company’s organizational structure compares with that of a key competitor. 
    
    \nThe recently appointed CEO—a former high-level executive from a competing firm—has closely modeled the current structure on that of his previous organization. However, critical differences exist: his prior company had an FDA-approved, commercially viable drug, while this startup is still in the pre-approval stage. 

    \nThis raises important questions: How well does this structure serve a company without an approved product? Are there hidden strengths or potential risks in replicating a model not yet tailored to current challenges? By visualizing and analyzing this data, we can assess the strengths and weaknesses of the current setup and make informed recommendations.
    """
)

st.info("Workforce costs are often a sensitive and confidential topic, for understandable reasons. However, there’s a growing trend toward transparency in disclosing salary information. If you’re curious, a simple online search for the role and company—combined with a bit of industry knowledge—can often reveal the data you need.")

st.write("The table below outlines key details for this business case:")

data = {
    'Workforce':['Scientists', 'Lab Technicians', 'Clinical Researchers', 'Bioinformatics Specialists', 'Project Managers', 'Manufacturing Technicians', 'Quality Assurance/Quality Control (QA/QC)', 'Supply Chain Specialists', 'Sales Representatives', 'Marketing Specialists', 'Product Managers', 'Human Resources', 'Finance and Accounting', 'IT Support', 'Administrative Assistants', 'Executive Leadership'], 
    'Workforce Count':[40, 30, 15, 10, 5, 30, 15, 5, 15, 10, 5, 5, 5, 5, 5, 5],
    'Workforce Cost':[6840000, 2205000, 3037500, 1710000, 415000, 2985000, 1927500, 405000,1200000,775000, 615000, 550000, 700000, 525000, 455000, 1047500]}
df = pd.DataFrame(data)

st.dataframe(df, hide_index=True)

total_row = pd.DataFrame(df.sum()).T
total_row.iloc[0,0] = 'Total'
# st.dataframe(total_row, hide_index=True)

# ----- Headcount Image Map ----- #

st.write("""The visual guide below illustrates the organization by role and headcount.""")

headcount = df.copy()
headcount['Left Side'] = headcount['Workforce Count']/2
headcount['Right Side'] = headcount['Workforce Count']/2
hc_cat = headcount['Workforce']
hc_val = headcount['Left Side']
hc_val2 = headcount['Right Side']

fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0)
fig.add_trace(go.Bar(
            x=hc_val,
            y=hc_cat,
            orientation='h',
            marker_color ='#c0def7'), row=1, col=1)
fig.add_trace(go.Bar(
            x=hc_val2,
            y=hc_cat,
            orientation='h',
            marker_color ='#c0def7',
            text=headcount['Workforce Count'],
            textposition='outside',
            name='Headcount'), row=1, col=2)
fig.update_layout(title_text='Org Headcount Image Map')
fig.update_xaxes(row=1, col=1, autorange="reversed", showticklabels=False)
fig.update_xaxes(row=1, col=2, showticklabels=False)
fig.update_traces(showlegend=False, row=1, col=1)
st.plotly_chart(fig)

st.write(
        """
        The first question to consider is whether the organization’s structure aligns with its intended design. Is the current shape intentional, or did it develop by accident? And, importantly, does the size support the business strategies we aim to accomplish?  

        \nOnce you have a clear view of headcount, a powerful next step is to compare costs. This is especially relevant now, as cost-saving strategies are top of mind in most scenarios. Entering a meeting equipped with insights into cost implications and their impact on different areas will elevate the discussion and add real value.
        """)

# ----- Cost Image Map ----- #

st.write("""The visual guide below illustrates the organization by role and associated costs.""")

cost = df.copy()
cost['Left Side'] = cost['Workforce Cost']/2
cost['Right Side'] = cost['Workforce Cost']/2
cost_cat = cost['Workforce']
cost_val = cost['Left Side']
cost_val2 = cost['Right Side']

fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0)
fig.add_trace(go.Bar(
            x=cost_val,
            y=cost_cat,
            orientation='h',
            marker_color ='#6a92b0'), row=1, col=1)
fig.add_trace(go.Bar(
            x=cost_val2,
            y=cost_cat,
            orientation='h',
            text=headcount['Workforce Cost'].apply(lambda x: "${:.1f}m".format((x/1000000))),
            textposition='outside',
            name='Cost',
            marker_color ='#6a92b0'), row=1, col=2)
fig.update_layout(title_text='Org Cost Image Map')
fig.update_xaxes(row=1, col=1, autorange="reversed", showticklabels=False)
fig.update_xaxes(row=1, col=2, showticklabels=False)
fig.update_traces(showlegend=False, row=1, col=1)
st.plotly_chart(fig)

st.write(
        """
        Here are some insights based on the organizational data:

        1. **High-Cost Roles**:
        - **Scientists** have the highest total cost at \$6.84 million, with 40 employees at \$171,000 each. This likely reflects the research-intensive nature of the company and aligns with a focus on innovation and product development.
        - **Clinical Researchers** also represent a significant cost, totaling $3.04 million with only 15 employees, suggesting this role requires highly specialized expertise, which is essential for a biotech company working on gene editing.

        2. **Core Functional Support**:
        - **Lab Technicians** and **Manufacturing Technicians** are critical support roles, with combined costs of $5.19 million. These roles help sustain the lab and production processes, but at a relatively lower per-person cost compared to specialized scientists and researchers.
        - **QA/QC (Quality Assurance/Quality Control)** also represents a notable expense (\$1.93 million), underscoring the importance of maintaining high standards in research and production, likely crucial for regulatory compliance.

        3. **Executive and Overhead Costs**:
        - **Executive Leadership** costs \$1.05 million for 5 members, reflecting the strategic value attributed to leadership in guiding the organization’s vision. However, compared to R&D costs, it’s a smaller percentage of total expenses.
        - Support roles like **HR, Finance & Accounting, IT Support, and Administrative Assistance** collectively cost $2.23 million, essential for operational stability but a relatively small portion of total costs.

        4. **Cost Efficiency Opportunities**:
        - There may be room to evaluate the balance between the high concentration of scientists and technicians relative to commercial roles like **Sales** (\$1.2 million) and **Marketing** (\$775,000). If the company is approaching commercial viability, increasing investment in these areas might be beneficial to drive market reach.
        - Additionally, the high costs associated with **Clinical Researchers** and **Bioinformatics Specialists** could be monitored closely. If the company’s focus shifts from R&D to commercialization, some of these roles may either require realignment or be scaled down.

        5. **Overall Structure and Strategy Alignment**:
        - The heavy investment in R&D roles (scientists, lab technicians, clinical researchers) suggests the company is currently R&D-focused, potentially pre-revenue, and prioritizing innovation. If this is the case, the structure aligns well with a research-heavy strategy.
        - However, if the company is nearing a product launch or approval, additional focus on commercial and operational roles (like Sales, Marketing, and Supply Chain) might be required to support growth and distribution strategies.

        Overall, the data indicates a structure typical of a biotech startup in the R&D phase, though there may be opportunities for strategic shifts if the company moves towards commercialization. 

        So it appears the new CEO team knows what he is doing. 
        """)

# ----- Side by Side ----- #
test=df.copy()
categories = test['Workforce']
values = test['Workforce Count']
values2 = test['Workforce Cost']

fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0)
fig.add_trace(go.Bar(
            x=values, 
            y=categories, 
            orientation='h', 
            text=values, 
            textposition='outside',
            name='Headcount',
            marker_color ='#c0def7'), row=1, col=1)
fig.add_trace(go.Bar(
            x=values2, 
            y=categories, 
            orientation='h', 
            text=values2.apply(lambda x: "${:.1f}m".format((x/1000000))),
            textposition='outside',
            name='Cost',
            marker_color ='#6a92b0'), row=1, col=2)
fig.update_layout(title_text="Side By Side Comparison")
fig.update_xaxes(row=1, col=1, autorange="reversed")
st.plotly_chart(fig)