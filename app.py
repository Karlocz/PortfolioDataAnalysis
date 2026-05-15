import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0f1117;
    border-right: 1px solid #1e2130;
}
section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}
.sidebar-name {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: #f8fafc !important;
    margin-bottom: 4px;
}
.sidebar-role {
    font-size: 12px;
    color: #64748b !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 24px;
}
.sidebar-divider {
    border: none;
    border-top: 1px solid #1e2130;
    margin: 16px 0;
}

/* Main area */
.main-header {
    font-family: 'DM Serif Display', serif;
    font-size: 42px;
    color: #0f1117;
    line-height: 1.2;
    margin-bottom: 8px;
}
.main-subtitle {
    font-size: 16px;
    color: #64748b;
    margin-bottom: 36px;
}

/* Metric card */
.metric-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px 24px;
    text-align: center;
}
.metric-value {
    font-size: 32px;
    font-weight: 600;
    color: #0f172a;
    line-height: 1;
}
.metric-label {
    font-size: 12px;
    color: #94a3b8;
    margin-top: 6px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
.metric-delta {
    font-size: 13px;
    color: #10b981;
    margin-top: 4px;
    font-weight: 500;
}

/* Project card */
.project-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
    transition: box-shadow 0.2s;
}
.project-tag {
    display: inline-block;
    background: #eff6ff;
    color: #3b82f6;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 99px;
    margin-right: 6px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.skill-pill {
    display: inline-block;
    background: #f1f5f9;
    color: #475569;
    font-size: 13px;
    padding: 6px 14px;
    border-radius: 99px;
    margin: 4px;
    font-weight: 500;
}
.section-label {
    font-size: 11px;
    font-weight: 600;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 12px;
}
.impact-number {
    font-family: 'DM Serif Display', serif;
    font-size: 28px;
    color: #0f172a;
}

/* Streamlit overrides */
div[data-testid="stMetric"] {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px 20px;
}
.stButton > button {
    background: #0f172a;
    color: white;
    border: none;
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    padding: 10px 22px;
}
.stButton > button:hover {
    background: #1e293b;
    color: white;
}
h1, h2, h3 {
    font-family: 'DM Serif Display', serif !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-name">Your Name</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-role">Data Analyst</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠  About", "📈  Projects", "🛠️  Skills", "📬  Contact"],
        label_visibility="collapsed",
    )

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:12px; color:#475569; line-height:1.8;">
        📍 São Paulo, Brazil<br>
        🌐 Open to remote & relocation<br>
        💼 Available for new roles
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:12px; color:#475569;">
        <a href="https://github.com" style="color:#60a5fa; text-decoration:none;">GitHub ↗</a> &nbsp;·&nbsp;
        <a href="https://linkedin.com" style="color:#60a5fa; text-decoration:none;">LinkedIn ↗</a>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ══════════════════════════════════════════════════════════════════════════════
if "About" in page:
    st.markdown('<div class="main-header">Turning data<br>into decisions.</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Data Analyst · SQL · Python · BI · Experimentation</div>', unsafe_allow_html=True)

    # ── Summary stats ────────────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Years of Experience", "3+", delta="Growing")
    with c2:
        st.metric("Projects Delivered", "20+", delta="End-to-end")
    with c3:
        st.metric("Revenue Impact", "$400K+", delta="Identified")
    with c4:
        st.metric("Reports Automated", "70%", delta="Time saved")

    st.markdown("---")

    # ── Bio ──────────────────────────────────────────────────────────────────
    col_bio, col_stack = st.columns([3, 2], gap="large")

    with col_bio:
        st.markdown("### About me")
        st.markdown("""
I am a Data Analyst with experience translating complex datasets into strategic business decisions.
I work with **SQL**, **Python**, and **BI tools** to build reliable metrics, scalable dashboards, and clear narratives for stakeholders.

My core strengths include KPI design, funnel analysis, cohort analysis, and experimentation support.
I'm particularly motivated by international, data-driven teams where ownership and communication are critical.

I'm open to **remote and relocation opportunities**.
        """)

    with col_stack:
        st.markdown("### Tech stack")
        skills = [
            "SQL (Advanced)", "Python", "Power BI", "Tableau",
            "Looker Studio", "BigQuery", "Git", "A/B Testing",
            "Cohort Analysis", "Pandas", "Plotly", "Excel",
        ]
        pills_html = "".join(f'<span class="skill-pill">{s}</span>' for s in skills)
        st.markdown(pills_html, unsafe_allow_html=True)

    st.markdown("---")

    # ── Experience timeline (Plotly Gantt-style) ─────────────────────────────
    st.markdown("### Career timeline")
    timeline_data = pd.DataFrame([
        dict(Role="Data Analyst", Company="TechCorp", Start="2022-06", End="2024-12", Color="#3b82f6"),
        dict(Role="Jr. Data Analyst", Company="RetailCo", Start="2021-01", End="2022-05", Color="#8b5cf6"),
        dict(Role="Data Intern", Company="StartupXYZ", Start="2020-03", End="2020-12", Color="#10b981"),
    ])
    fig = px.timeline(
        timeline_data,
        x_start="Start", x_end="End",
        y="Company", color="Company",
        text="Role",
        color_discrete_sequence=["#3b82f6", "#8b5cf6", "#10b981"],
        height=200,
    )
    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_family="DM Sans",
    )
    fig.update_traces(textposition="inside", insidetextanchor="middle")
    fig.update_yaxes(title=None)
    fig.update_xaxes(title=None)
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
elif "Projects" in page:
    st.markdown("## Featured projects")
    st.markdown('<div class="main-subtitle">End-to-end analyses with measurable business impact.</div>', unsafe_allow_html=True)

    project_tab = st.selectbox(
        "Select project",
        ["E-commerce Funnel Optimization", "Customer Churn Analysis", "Marketing CAC/LTV", "Operations Forecasting"],
        label_visibility="collapsed",
    )

    # ─── Project 1: Funnel ───────────────────────────────────────────────────
    if project_tab == "E-commerce Funnel Optimization":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">SQL</span>
<span class="project-tag">Power BI</span>
<span class="project-tag">Funnel Analysis</span>
            """, unsafe_allow_html=True)
            st.markdown("### E-commerce Funnel Optimization")
            st.markdown("""
**Business problem:** The growth team suspected significant drop-off before checkout but lacked visibility across devices and acquisition channels.

**Approach:** Built a multi-step SQL funnel from raw event logs, modeled conversion at each stage, and segmented by device type and UTM source to isolate the worst bottlenecks.

**Key finding:** Mobile users dropped off 2.3× more at the add-to-cart → checkout step compared to desktop — traced to a non-responsive cart UI on iOS.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Impact estimate</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card">
  <div class="metric-value">$48K</div>
  <div class="metric-label">Monthly revenue uplift</div>
  <div class="metric-delta">+1.5 p.p. checkout conversion</div>
</div>
            """, unsafe_allow_html=True)

        # Funnel chart
        st.markdown("#### Conversion funnel")
        stages = ["Visit", "Product View", "Add to Cart", "Checkout", "Purchase"]
        values = [100000, 62000, 34000, 21000, 14700]
        pcts   = [100, 62, 34.0, 21.0, 14.7]

        fig = go.Figure(go.Funnel(
            y=stages, x=values,
            textinfo="percent initial+value",
            marker_color=["#dbeafe", "#93c5fd", "#60a5fa", "#3b82f6", "#1d4ed8"],
            connector={"line": {"color": "#e2e8f0", "width": 1}},
        ))
        fig.update_layout(
            height=360, margin=dict(l=0, r=0, t=20, b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_family="DM Sans",
        )
        st.plotly_chart(fig, use_container_width=True)

        # Device breakdown
        st.markdown("#### Conversion by device")
        device_data = pd.DataFrame({
            "Stage":  stages * 3,
            "Device": ["Desktop"] * 5 + ["Mobile"] * 5 + ["Tablet"] * 5,
            "Rate":   [100,68,42,28,20, 100,55,24,12,7, 100,60,32,20,14],
        })
        fig2 = px.line(
            device_data, x="Stage", y="Rate", color="Device",
            markers=True,
            color_discrete_map={"Desktop": "#3b82f6", "Mobile": "#f43f5e", "Tablet": "#a78bfa"},
            labels={"Rate": "Conversion Rate (%)"},
            height=300,
        )
        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
            legend=dict(orientation="h", y=-0.2),
        )
        st.plotly_chart(fig2, use_container_width=True)

    # ─── Project 2: Churn ────────────────────────────────────────────────────
    elif project_tab == "Customer Churn Analysis":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">Python</span>
<span class="project-tag">Cohort Analysis</span>
<span class="project-tag">SaaS</span>
            """, unsafe_allow_html=True)
            st.markdown("### Customer Churn Analysis")
            st.markdown("""
**Business problem:** A SaaS company with 6.2% monthly churn needed to identify at-risk segments before cancellation intent was expressed.

**Approach:** Built 12-month retention cohorts, segmented customers by plan type and engagement score, and developed a simple logistic-regression risk score to flag accounts for proactive outreach.

**Key finding:** Customers on monthly plans who logged in < 3× in their first 30 days churned at 4× the rate of highly engaged users.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Impact estimate</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card">
  <div class="metric-value">$120K</div>
  <div class="metric-label">ARR preserved per quarter</div>
  <div class="metric-delta">Churn 6.2% → 5.4%</div>
</div>
            """, unsafe_allow_html=True)

        # Cohort heatmap
        st.markdown("#### Retention cohort heatmap")
        np.random.seed(42)
        months = [f"Month {i}" for i in range(1, 13)]
        cohorts = [f"Cohort {2023 + i//12}-{(i%12)+1:02d}" for i in range(8)]
        base = np.array([100, 78, 62, 52, 45, 40, 36, 33, 30, 28, 27, 26])
        data = np.array([base * (0.97 ** i) * (1 + np.random.randn(12) * 0.02) for i in range(8)])
        data[:, 0] = 100
        for i in range(8):
            for j in range(i + 1, 8):
                data[j, 12 - j + i - 1:] = np.nan

        fig = go.Figure(go.Heatmap(
            z=data.round(1),
            x=months,
            y=cohorts,
            colorscale=[[0, "#dbeafe"], [0.5, "#3b82f6"], [1, "#1e3a8a"]],
            text=np.where(np.isnan(data), "", data.round(1).astype(str) + "%"),
            texttemplate="%{text}",
            showscale=True,
            colorbar=dict(title="Retention %"),
        ))
        fig.update_layout(
            height=320, margin=dict(l=0, r=0, t=20, b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_family="DM Sans",
        )
        st.plotly_chart(fig, use_container_width=True)

    # ─── Project 3: CAC/LTV ──────────────────────────────────────────────────
    elif project_tab == "Marketing CAC/LTV":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">SQL</span>
<span class="project-tag">Python</span>
<span class="project-tag">Growth</span>
            """, unsafe_allow_html=True)
            st.markdown("### Marketing Efficiency: CAC / LTV")
            st.markdown("""
**Business problem:** Marketing budget was distributed equally across channels despite very different acquisition costs and customer quality.

**Approach:** Consolidated spend and revenue data across 5 channels using SQL + Python. Calculated blended and per-channel CAC, estimated LTV by cohort, and modeled payback periods.

**Key finding:** Organic search delivered 3× higher LTV/CAC ratio than paid social, yet received only 12% of budget allocation.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Impact estimate</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card">
  <div class="metric-value">+12%</div>
  <div class="metric-label">Blended ROAS improvement</div>
  <div class="metric-delta">18% budget reallocation</div>
</div>
            """, unsafe_allow_html=True)

        channels = ["Organic Search", "Paid Search", "Paid Social", "Email", "Referral"]
        cac      = [28, 95, 140, 18, 42]
        ltv      = [420, 380, 290, 310, 510]
        spend    = [12, 35, 28, 8, 17]

        fig = make_subplots(rows=1, cols=2, subplot_titles=["LTV / CAC Ratio by Channel", "Budget Allocation vs. LTV/CAC"])
        ratios = [l / c for l, c in zip(ltv, cac)]
        colors = ["#10b981" if r > 5 else "#f59e0b" if r > 3 else "#ef4444" for r in ratios]

        fig.add_trace(go.Bar(x=channels, y=ratios, marker_color=colors, name="LTV/CAC"), row=1, col=1)
        fig.add_trace(go.Scatter(
            x=spend, y=ratios, mode="markers+text", text=channels,
            textposition="top center", marker_size=14,
            marker_color=["#3b82f6"] * 5, name="",
        ), row=1, col=2)

        fig.update_layout(
            height=340, showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_family="DM Sans", margin=dict(l=0, r=0, t=40, b=0),
        )
        fig.update_xaxes(row=1, col=2, title="Budget Share (%)")
        fig.update_yaxes(row=1, col=1, title="LTV/CAC Ratio")
        fig.update_yaxes(row=1, col=2, title="LTV/CAC Ratio")
        st.plotly_chart(fig, use_container_width=True)

    # ─── Project 4: Forecasting ──────────────────────────────────────────────
    else:
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">Python</span>
<span class="project-tag">Time Series</span>
<span class="project-tag">Operations</span>
            """, unsafe_allow_html=True)
            st.markdown("### Operations & Demand Forecasting")
            st.markdown("""
**Business problem:** A service operations team was over/understaffed 40% of the time because scheduling relied on gut feel rather than demand patterns.

**Approach:** Modeled historical ticket volume with a 7-day rolling average + seasonal adjustment. Built a weekly staffing recommendation dashboard that updates automatically.

**Key finding:** Strong weekly seasonality (Mon–Tue peak, Fri trough) was being ignored, leading to consistent Monday SLA breaches.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Impact estimate</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card">
  <div class="metric-value">−14%</div>
  <div class="metric-label">SLA breaches reduced</div>
  <div class="metric-delta">Forecast-driven staffing</div>
</div>
            """, unsafe_allow_html=True)

        # Time series chart
        st.markdown("#### Demand forecast — next 30 days")
        np.random.seed(7)
        dates_hist = pd.date_range("2024-01-01", periods=90, freq="D")
        dates_fore = pd.date_range("2024-04-01", periods=30, freq="D")
        seasonality = np.array([1.3, 1.1, 0.9, 0.85, 0.75, 0.8, 1.0] * 20)[:90]
        actual = (200 + seasonality[:90] * 80 + np.random.randn(90) * 15).clip(50)
        forecast = (200 + seasonality[:30] * 80 + np.random.randn(30) * 8).clip(50)
        upper = forecast + 25
        lower = forecast - 25

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates_hist, y=actual, name="Actual", line=dict(color="#3b82f6", width=2)))
        fig.add_trace(go.Scatter(
            x=list(dates_fore) + list(dates_fore[::-1]),
            y=list(upper) + list(lower[::-1]),
            fill="toself", fillcolor="rgba(99,102,241,0.1)",
            line=dict(color="rgba(0,0,0,0)"), name="95% CI",
        ))
        fig.add_trace(go.Scatter(x=dates_fore, y=forecast, name="Forecast", line=dict(color="#6366f1", width=2, dash="dash")))
        fig.update_layout(
            height=320, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
            legend=dict(orientation="h", y=-0.2),
        )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridcolor="#f1f5f9", title="Tickets / Day")
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SKILLS
# ══════════════════════════════════════════════════════════════════════════════
elif "Skills" in page:
    st.markdown("## Technical skills")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### Languages & Libraries")
        lang_skills = {"SQL": 95, "Python (pandas/numpy)": 85, "Python (plotly/matplotlib)": 80, "Git": 75}
        for skill, level in lang_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(level / 100)

        st.markdown("#### Analytical Methods")
        methods = [
            "Funnel & Conversion Analysis", "Cohort & Retention Analysis",
            "Churn Prediction", "A/B Test Design & Analysis",
            "Segmentation & RFM", "Time Series Forecasting",
            "KPI Design", "Customer LTV / CAC",
        ]
        pills = "".join(f'<span class="skill-pill">{m}</span>' for m in methods)
        st.markdown(pills, unsafe_allow_html=True)

    with col2:
        st.markdown("#### BI & Visualization")
        bi_skills = {"Power BI": 90, "Tableau": 80, "Looker Studio": 75, "Plotly / Dash": 70}
        for skill, level in bi_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(level / 100)

        st.markdown("#### Cloud & Data")
        cloud = [
            "BigQuery", "Snowflake", "Redshift",
            "ETL Fundamentals", "dbt (basic)", "Airflow (basic)",
        ]
        pills2 = "".join(f'<span class="skill-pill">{m}</span>' for m in cloud)
        st.markdown(pills2, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Skill radar")
    categories = ["SQL", "Python", "BI / Dashboards", "Statistics", "Communication", "Cloud", "Product Sense"]
    values_self = [95, 82, 88, 74, 85, 65, 80]
    values_self.append(values_self[0])
    categories.append(categories[0])

    fig = go.Figure(go.Scatterpolar(
        r=values_self, theta=categories,
        fill="toself", fillcolor="rgba(59,130,246,0.15)",
        line_color="#3b82f6", name="Self-assessment",
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False, height=400,
        paper_bgcolor="rgba(0,0,0,0)", font_family="DM Sans",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif "Contact" in page:
    st.markdown("## Let's connect")
    st.markdown('<div class="main-subtitle">Open to remote roles, relocation, and freelance projects.</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("### Send a message")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message", height=140)
        if st.button("Send message →"):
            if name and email and message:
                st.success("✅ Message sent! I'll get back to you within 48 hours.")
            else:
                st.warning("Please fill in all fields.")

    with c2:
        st.markdown("### Quick links")
        st.markdown("""
- 🔗 **GitHub** — [github.com/yourhandle](https://github.com)
- 💼 **LinkedIn** — [linkedin.com/in/yourname](https://linkedin.com)
- 📄 **Resume** — [Download PDF](#)
- 📧 **Email** — your@email.com
        """)
        st.markdown("---")
        st.markdown("### Availability")
        st.info("✅ **Available** for new opportunities starting January 2025.\n\nPreferences: Remote-first · Data & Product Analytics · International teams.")
