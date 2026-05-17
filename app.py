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

/* ── Sidebar (always dark — intentional design) ── */
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
    color: #94a3b8 !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 24px;
}
.sidebar-divider {
    border: none;
    border-top: 1px solid #1e2130;
    margin: 16px 0;
}

/* ── Main area — uses Streamlit theme variables ── */
.main-header {
    font-family: 'DM Serif Display', serif;
    font-size: 42px;
    color: var(--text-color);
    line-height: 1.2;
    margin-bottom: 8px;
}
.main-subtitle {
    font-size: 16px;
    color: var(--text-color);
    opacity: 0.6;
    margin-bottom: 36px;
}

/* ── Metric card ── */
.metric-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.2);
    border-radius: 12px;
    padding: 20px 24px;
    text-align: center;
}
.metric-value {
    font-size: 32px;
    font-weight: 600;
    color: var(--text-color);
    line-height: 1;
}
.metric-label {
    font-size: 12px;
    color: var(--text-color);
    opacity: 0.5;
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

/* ── Project card ── */
.project-card {
    background: var(--background-color);
    border: 1px solid rgba(128, 128, 128, 0.2);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
}

/* ── Tags & pills ── */
.project-tag {
    display: inline-block;
    background: rgba(59, 130, 246, 0.15);
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
    background: rgba(128, 128, 128, 0.12);
    color: var(--text-color);
    font-size: 13px;
    padding: 6px 14px;
    border-radius: 99px;
    margin: 4px;
    font-weight: 500;
}
.section-label {
    font-size: 11px;
    font-weight: 600;
    color: var(--text-color);
    opacity: 0.5;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 12px;
}
.impact-number {
    font-family: 'DM Serif Display', serif;
    font-size: 28px;
    color: var(--text-color);
}

/* ── Streamlit component overrides ── */
div[data-testid="stMetric"] {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.2);
    border-radius: 12px;
    padding: 16px 20px;
}
.stButton > button {
    background: var(--text-color);
    color: var(--background-color);
    border: none;
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    padding: 10px 22px;
}
.stButton > button:hover {
    opacity: 0.85;
    color: var(--background-color);
}
h1, h2, h3 {
    font-family: 'DM Serif Display', serif !important;
    color: var(--text-color) !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-name">Carlos Maximino</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-role">Data Analyst</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠  About", "📈  Projects", "🛠️  Skills", "📄  Resume", "📬  Contact"],
        label_visibility="collapsed",
    )

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:12px; color:#475569; line-height:1.8;">
        📍 Brazil (Campinas region)<br>
        🌐 Open to remote & relocation<br>
        💼 Available for new roles
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:12px; color:#475569;">
        <a href="https://www.linkedin.com/in/carlos-maximino/" style="color:#60a5fa; text-decoration:none;">LinkedIn ↗</a> &nbsp;·&nbsp;
        <a href="mailto:cmax15@outlook.com.br" style="color:#60a5fa; text-decoration:none;">Email ↗</a>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ══════════════════════════════════════════════════════════════════════════════
if "About" in page:
    st.markdown('<div class="main-header">10 years of data,<br>operations & insight.</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Data Analyst · KPI/SLA · BI · ServiceNow · ITIL · Kyndryl</div>', unsafe_allow_html=True)

    # ── Summary stats ────────────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Years of Experience", "10+", delta="Across IT & Analytics")
    with c2:
        st.metric("Recurring Reports", "20", delta="Maintained actively")
    with c3:
        st.metric("Processes Monitored", "10", delta="9 service areas")
    with c4:
        st.metric("Team Led", "40 people", delta="Mainframe support")

    st.markdown("---")

    # ── Bio ──────────────────────────────────────────────────────────────────
    col_bio, col_stack = st.columns([3, 2], gap="large")

    with col_bio:
        st.markdown("### About me")
        st.markdown("""
I am a Data and Analytics professional with **10+ years of progressive experience** across enterprise IT operations,
service delivery, team leadership, and business performance reporting.

Currently working as a **Data Analyst at Kyndryl**, I transform operational, service, and business performance data
into dashboards, executive reports, and decision-ready insights for managers, DPEs, and client stakeholders at **Delta Air Lines**.

My background combines hands-on technical depth (mainframe, ITSM, ServiceNow, ITIL) with strong
analytical and communication skills — giving me an unusual ability to bridge the gap between operations and data-driven strategy.

I am open to **remote and relocation opportunities**.
        """)

    with col_stack:
        st.markdown("### Tech stack")
        skills = [
            "Excel (Advanced)", "ServiceNow", "ITIL", "SQL",
            "Python", "Tableau", "Power BI", "Neo4j",
            "Databricks", "Google Cloud", "CSV / ETL", "KPI/SLA Analysis",
        ]
        pills_html = "".join(f'<span class="skill-pill">{s}</span>' for s in skills)
        st.markdown(pills_html, unsafe_allow_html=True)

    st.markdown("---")

    # ── Career timeline ──────────────────────────────────────────────────────
    st.markdown("### Career progression")
    timeline_data = pd.DataFrame([
        dict(Role="Data Analyst", Company="Kyndryl", Start="2024-05", End="2025-05", Color="#3b82f6"),
        dict(Role="Team Leader (40 people)", Company="Kyndryl", Start="2022-01", End="2024-05", Color="#6366f1"),
        dict(Role="Service Delivery Analyst", Company="Kyndryl", Start="2021-09", End="2022-07", Color="#8b5cf6"),
        dict(Role="Service Delivery Analyst", Company="IBM", Start="2019-12", End="2021-09", Color="#a78bfa"),
        dict(Role="Scrum Master / Agile Coord.", Company="IBM", Start="2019-01", End="2019-12", Color="#c4b5fd"),
        dict(Role="Mainframe Operations Analyst", Company="IBM", Start="2014-03", End="2019-12", Color="#ddd6fe"),
    ])
    fig = px.timeline(
        timeline_data,
        x_start="Start", x_end="End",
        y="Company", color="Role",
        text="Role",
        color_discrete_sequence=["#3b82f6", "#6366f1", "#8b5cf6", "#a78bfa", "#c4b5fd", "#ddd6fe"],
        height=220,
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

    # ── Technology filter ────────────────────────────────────────────────────
    PROJECTS_TAGS = {
        "E-commerce Funnel Optimization":          ["SQL", "Power BI", "Python"],
        "Customer Churn Analysis":                 ["Python"],
        "Marketing CAC/LTV":                       ["SQL", "Python"],
        "Operations Forecasting":                  ["Python"],
        "Global Superstore — Profitability":       ["Python"],
        "CineGraph — Cinema & TV Analytics":       ["HTML/JS"],
        "HR Analytics Dashboard":                  ["Power BI"],
        "Data Warehouse & SQL Optimization":       ["SQL"],
        "A/B Testing & Regression — R":            ["R"],
        "ETL Pipeline — Airflow + dbt + BigQuery": ["Airflow", "dbt", "BigQuery"],
    }
    ALL_TAGS = sorted({"SQL","Python","Power BI","R","HTML/JS","Airflow","dbt","BigQuery"})

    col_filter, col_count = st.columns([4, 1])
    with col_filter:
        selected_tags = st.multiselect(
            "🔍 Filter by technology",
            ALL_TAGS,
            placeholder="All technologies — showing all projects",
        )
    filtered_projects = (
        [p for p, tags in PROJECTS_TAGS.items() if any(t in selected_tags for t in tags)]
        if selected_tags else list(PROJECTS_TAGS.keys())
    )
    with col_count:
        st.markdown(f"<div style='padding-top:32px;font-size:13px;color:var(--text-color);opacity:.6'>{len(filtered_projects)} project{'s' if len(filtered_projects)!=1 else ''}</div>", unsafe_allow_html=True)

    if not filtered_projects:
        st.info("No projects match the selected filters. Try removing some tags.")
        st.stop()

    project_tab = st.selectbox("Select project", filtered_projects, label_visibility="collapsed")


    # ── Recruiter-facing technical code snippets ────────────────────────────
    PROJECT_CODE_SNIPPETS = {
        "E-commerce Funnel Optimization": {
            "language": "sql",
            "code": """-- Funnel conversion by device and acquisition channel
WITH events AS (
    SELECT
        user_id,
        session_id,
        device_type,
        utm_source,
        event_name,
        event_timestamp
    FROM raw.web_events
    WHERE event_timestamp >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
),
funnel AS (
    SELECT
        device_type,
        utm_source,
        COUNT(DISTINCT IF(event_name = 'visit', session_id, NULL))        AS visits,
        COUNT(DISTINCT IF(event_name = 'product_view', session_id, NULL)) AS product_views,
        COUNT(DISTINCT IF(event_name = 'add_to_cart', session_id, NULL))  AS add_to_carts,
        COUNT(DISTINCT IF(event_name = 'checkout', session_id, NULL))     AS checkouts,
        COUNT(DISTINCT IF(event_name = 'purchase', session_id, NULL))     AS purchases
    FROM events
    GROUP BY device_type, utm_source
)
SELECT
    *,
    SAFE_DIVIDE(product_views, visits)      AS visit_to_product_rate,
    SAFE_DIVIDE(add_to_carts, product_views) AS product_to_cart_rate,
    SAFE_DIVIDE(checkouts, add_to_carts)    AS cart_to_checkout_rate,
    SAFE_DIVIDE(purchases, checkouts)       AS checkout_to_purchase_rate
FROM funnel
ORDER BY cart_to_checkout_rate ASC;""",
        },
        "Customer Churn Analysis": {
            "language": "python",
            "code": """# Cohort retention + churn risk scoring
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

customers['signup_month'] = customers['signup_date'].dt.to_period('M')
activity['active_month'] = activity['event_date'].dt.to_period('M')

cohort = (
    activity.merge(customers[['customer_id', 'signup_month']], on='customer_id')
    .assign(month_number=lambda d: (d['active_month'] - d['signup_month']).apply(lambda x: x.n))
    .query('month_number >= 0')
    .groupby(['signup_month', 'month_number'])['customer_id']
    .nunique()
    .reset_index(name='active_customers')
)
cohort['retention_rate'] = cohort['active_customers'] / cohort.groupby('signup_month')['active_customers'].transform('first')

features = customers[['plan_type', 'logins_first_30d', 'tickets_opened', 'days_since_last_login']]
X = pd.get_dummies(features, drop_first=True)
y = customers['churned']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=42, stratify=y)
model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
customers['churn_risk_score'] = model.predict_proba(X)[:, 1]
print('AUC:', roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))""",
        },
        "Marketing CAC/LTV": {
            "language": "python",
            "code": """# Channel-level CAC, LTV, LTV/CAC and payback period
spend_by_channel = spend.groupby(['month', 'channel'], as_index=False)['cost'].sum()
revenue_by_customer = orders.groupby(['customer_id', 'channel'], as_index=False)['revenue'].sum()
new_customers = customers.query('is_new_customer == 1').groupby('channel')['customer_id'].nunique()

cac = spend.groupby('channel')['cost'].sum().div(new_customers).rename('cac')
ltv = revenue_by_customer.groupby('channel')['revenue'].mean().rename('ltv')
monthly_margin = orders.assign(gross_margin=orders['revenue'] - orders['cost_of_goods']).groupby('channel')['gross_margin'].mean()

marketing_efficiency = pd.concat([cac, ltv, monthly_margin.rename('avg_monthly_margin')], axis=1)
marketing_efficiency['ltv_cac_ratio'] = marketing_efficiency['ltv'] / marketing_efficiency['cac']
marketing_efficiency['payback_months'] = marketing_efficiency['cac'] / marketing_efficiency['avg_monthly_margin']
marketing_efficiency.sort_values('ltv_cac_ratio', ascending=False)""",
        },
        "Operations Forecasting": {
            "language": "python",
            "code": """# Ticket demand forecast using rolling average + weekday seasonality
import pandas as pd

series = tickets.set_index('opened_at').resample('D')['ticket_id'].count().rename('tickets').to_frame()
series['rolling_7d'] = series['tickets'].rolling(7, min_periods=7).mean()
series['weekday'] = series.index.day_name()

weekday_factor = (
    series.groupby('weekday')['tickets'].mean() / series['tickets'].mean()
).to_dict()

future = pd.DataFrame(index=pd.date_range(series.index.max() + pd.Timedelta(days=1), periods=30, freq='D'))
future['weekday'] = future.index.day_name()
future['baseline'] = series['rolling_7d'].iloc[-1]
future['forecast'] = future['baseline'] * future['weekday'].map(weekday_factor)
future['recommended_staff'] = (future['forecast'] / 22).round().astype(int)  # 22 tickets per analyst/day
future[['forecast', 'recommended_staff']].head()""",
        },
        "Global Superstore — Profitability": {
            "language": "python",
            "code": """# Profitability EDA with engineered business metrics
import pandas as pd

orders = pd.read_csv('global_superstore.csv', parse_dates=['Order Date', 'Ship Date'])
orders['profit_margin'] = orders['Profit'] / orders['Sales']
orders['shipping_cost_ratio'] = orders['Shipping Cost'] / orders['Sales']
orders['shipping_days'] = (orders['Ship Date'] - orders['Order Date']).dt.days
orders['discount_band'] = pd.cut(
    orders['Discount'],
    bins=[-0.01, 0, .10, .20, .30, 1],
    labels=['No Discount', '0-10%', '10-20%', '20-30%', '30%+']
)

summary = (
    orders.groupby(['Region', 'Category', 'discount_band'], observed=True)
    .agg(
        orders=('Order ID', 'nunique'),
        sales=('Sales', 'sum'),
        profit=('Profit', 'sum'),
        avg_margin=('profit_margin', 'mean'),
        ship_cost_ratio=('shipping_cost_ratio', 'mean')
    )
    .reset_index()
    .sort_values('avg_margin')
)
summary.head(10)""",
        },
        "CineGraph — Cinema & TV Analytics": {
            "language": "javascript",
            "code": """// TMDB analytics: ROI, decade ratings and director efficiency
const moviesClean = movies
  .filter(d => d.budget > 0 && d.revenue > 0 && d.vote_count >= 100)
  .map(d => ({
    ...d,
    roi: (d.revenue - d.budget) / d.budget,
    revenueMultiplier: d.revenue / d.budget,
    decade: `${Math.floor(new Date(d.release_date).getFullYear() / 10) * 10}s`
  }));

const byGenre = d3.rollups(
  moviesClean.flatMap(m => m.genres.map(g => ({ genre: g, ...m }))),
  v => ({
    films: v.length,
    avgBudget: d3.mean(v, d => d.budget),
    avgRevenue: d3.mean(v, d => d.revenue),
    avgRoi: d3.mean(v, d => d.roi),
    avgRating: d3.mean(v, d => d.vote_average)
  }),
  d => d.genre
).sort((a, b) => b[1].avgRoi - a[1].avgRoi);

const directorScore = d3.rollups(
  moviesClean.filter(d => d.director),
  v => ({ films: v.length, avgRating: d3.mean(v, d => d.vote_average) }),
  d => d.director
).filter(([_, s]) => s.films >= 25);""",
        },
        "HR Analytics Dashboard": {
            "language": "dax",
            "code": """-- Power BI DAX measures used in the attrition dashboard
Headcount =
CALCULATE(
    DISTINCTCOUNT(Employees[EmployeeID]),
    Employees[HireDate] <= MAX('Date'[Date]),
    OR(ISBLANK(Employees[TerminationDate]), Employees[TerminationDate] > MAX('Date'[Date]))
)

Departures =
CALCULATE(
    DISTINCTCOUNT(Employees[EmployeeID]),
    USERELATIONSHIP(Employees[TerminationDate], 'Date'[Date])
)

Attrition Rate =
DIVIDE([Departures], [Headcount])

High Performer Attrition =
CALCULATE(
    [Attrition Rate],
    Employees[PerformanceBand] IN {4, 5}
)

Early Tenure Departure % =
DIVIDE(
    CALCULATE([Departures], Employees[TenureBucket] IN {"< 1 year", "1-2 years"}),
    [Departures]
)""",
        },
        "Data Warehouse & SQL Optimization": {
            "language": "sql",
            "code": """-- Medallion mart pattern: consistent business logic in one place
CREATE OR REPLACE TABLE mart.mart_orders
PARTITION BY order_month
CLUSTER BY customer_id, category AS
WITH orders AS (
    SELECT * FROM staging.stg_orders
),
customers AS (
    SELECT * FROM intermediate.int_customers_segmented
),
products AS (
    SELECT * FROM staging.stg_products
)
SELECT
    o.order_id,
    DATE_TRUNC(o.order_date, MONTH) AS order_month,
    c.customer_id,
    c.segment,
    c.country,
    p.category,
    p.sub_category,
    o.sales,
    o.discount,
    o.profit,
    SAFE_DIVIDE(o.profit, o.sales) AS profit_margin,
    SAFE_DIVIDE(o.shipping_cost, o.sales) AS shipping_cost_ratio
FROM orders o
LEFT JOIN customers c USING (customer_id)
LEFT JOIN products p USING (product_id);""",
        },
        "A/B Testing & Regression — R": {
            "language": "r",
            "code": """library(tidyverse)
library(broom)
library(pwr)

# Power analysis before launch
sample_size <- pwr.2p.test(
  h = ES.h(p1 = 0.052, p2 = 0.041),
  sig.level = 0.05,
  power = 0.80,
  alternative = 'two.sided'
)

# Primary metric test
experiment_result <- t.test(
  conversion ~ variant,
  data = experiment_data,
  alternative = 'two.sided',
  conf.level = 0.95
) |> tidy()

# Logistic regression with device/source controls
model <- glm(
  converted ~ variant + device_type + session_duration + traffic_source + returning_user,
  data = experiment_data,
  family = binomial()
)

tidy(model, conf.int = TRUE, exponentiate = TRUE)""",
        },
        "ETL Pipeline — Airflow + dbt + BigQuery": {
            "language": "python",
            "code": """# Airflow DAG: extract raw files, run dbt, test, then refresh BI cache
from airflow.decorators import dag
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
from pendulum import datetime

@dag(
    schedule='0 5 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['analytics', 'production'],
    on_failure_callback=slack_alert,
)
def daily_analytics_pipeline():
    load_orders = GCSToBigQueryOperator(
        task_id='load_raw_orders',
        bucket='analytics-landing',
        source_objects=['orders/{{ ds }}/*.csv'],
        destination_project_dataset_table='raw.orders',
        write_disposition='WRITE_APPEND',
    )

    dbt_run = DbtCloudRunJobOperator(task_id='dbt_run', job_id=12345)
    dbt_test = DbtCloudRunJobOperator(task_id='dbt_test', job_id=12346)
    refresh_dashboards = refresh_looker_cache(task_id='refresh_dashboards')

    load_orders >> dbt_run >> dbt_test >> refresh_dashboards

daily_analytics_pipeline()""",
        },
    }

    def render_technical_code(project_name):
        snippet = PROJECT_CODE_SNIPPETS[project_name]
        with st.expander("🔎 Technical code used in the analysis", expanded=True):
            st.caption("Representative code block showing the technical steps behind this project.")
            st.code(snippet["code"].strip(), language=snippet["language"])

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

        render_technical_code("E-commerce Funnel Optimization")

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

        render_technical_code("Customer Churn Analysis")

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

        render_technical_code("Marketing CAC/LTV")

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

    # ─── Project 5: Global Superstore ───────────────────────────────────────
    elif project_tab == "Global Superstore — Profitability":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">Python</span>
<span class="project-tag">Pandas</span>
<span class="project-tag">EDA</span>
<span class="project-tag">Retail</span>
            """, unsafe_allow_html=True)
            st.markdown("### Global Superstore — Profitability & Segmentation")
            st.markdown("""
**Business problem:** A multinational retailer operating across 147 countries faced margin pressure despite strong sales volume.
Leadership lacked visibility into which segments, regions, and discount practices were eroding profitability.

**Approach:** End-to-end EDA on 51,290 transaction rows (2011–2014). Engineered derived metrics
(Profit Margin, Shipping Cost Ratio, Discount Band, Shipping Days), then analyzed profitability
across regions, customer segments, product categories, and discount bands.

**Key findings:**
- Discounts above 20% produce **negative margins on average** — the 30%+ band is the biggest margin leak.
- **Central** and **South** regions show the worst profit-to-sales ratio; high shipping costs explain the gap.
- **Consumer** segment leads in absolute profit; **Technology** is the highest-margin category.
- Several sub-categories (Copiers, Phones, Accessories) are strong engines — Tables and Bookcases consistently destroy margin.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Dataset scope</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card" style="margin-bottom:10px">
  <div class="metric-value">51K</div>
  <div class="metric-label">Transaction rows</div>
  <div class="metric-delta">2011 – 2014</div>
</div>
<div class="metric-card">
  <div class="metric-value">147</div>
  <div class="metric-label">Countries</div>
  <div class="metric-delta">7 global markets</div>
</div>
            """, unsafe_allow_html=True)

        render_technical_code("Global Superstore — Profitability")

        tab1, tab2, tab3 = st.tabs(["Discount Impact", "Regional Profitability", "Category & Segment"])

        with tab1:
            st.markdown("#### Average profit margin by discount band")
            st.caption("Derived metric: `Profit_Margin = Profit / Sales`, grouped into business-friendly buckets.")
            bands   = ["No Discount", "0–10%", "10–20%", "20–30%", "30%+"]
            margins = [0.182, 0.143, 0.071, -0.043, -0.121]
            orders  = [18400, 12200, 9800, 6100, 4800]
            colors  = ["#10b981" if m > 0 else "#ef4444" for m in margins]
            fig = make_subplots(rows=1, cols=2, subplot_titles=["Avg Profit Margin (%)", "Order Volume by Band"])
            fig.add_trace(go.Bar(
                x=bands, y=[m * 100 for m in margins], marker_color=colors, name="Margin",
                text=[f"{m*100:.1f}%" for m in margins], textposition="outside",
            ), row=1, col=1)
            fig.add_trace(go.Bar(
                x=bands, y=orders, marker_color=["#dbeafe"] * 5, name="Orders",
                text=orders, textposition="outside",
            ), row=1, col=2)
            fig.update_layout(
                height=340, showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0, r=0, t=40, b=0),
            )
            fig.add_hline(y=0, line_dash="dot", line_color="#94a3b8", row=1, col=1)
            fig.update_yaxes(ticksuffix="%", row=1, col=1)
            st.plotly_chart(fig, use_container_width=True)
            st.info("📌 **Recommendation:** Introduce a 20% discount ceiling with manager approval above that threshold — the data shows a clear inflection point where average margin turns negative.")

        with tab2:
            st.markdown("#### Profit vs. shipping cost burden by region")
            regions        = ["Central Asia", "North Asia", "Oceania", "North America", "Caribbean",
                              "W. Europe", "E. Europe", "Africa", "Central", "South"]
            profit         = [87400, 73200, 61500, 58900, 52100, 48700, 31200, 22800, -8400, -15200]
            shipping_ratio = [0.08, 0.09, 0.11, 0.07, 0.13, 0.10, 0.14, 0.16, 0.19, 0.22]
            bar_colors     = ["#10b981" if p > 0 else "#ef4444" for p in profit]
            sorted_idx     = sorted(range(len(profit)), key=lambda i: profit[i])
            fig = make_subplots(rows=1, cols=2, subplot_titles=["Total Profit by Region", "Shipping Cost Ratio (%)"])
            fig.add_trace(go.Bar(
                y=[regions[i] for i in sorted_idx], x=[profit[i] for i in sorted_idx],
                orientation="h", marker_color=[bar_colors[i] for i in sorted_idx], name="Profit",
            ), row=1, col=1)
            fig.add_trace(go.Bar(
                y=[regions[i] for i in sorted_idx], x=[shipping_ratio[i] * 100 for i in sorted_idx],
                orientation="h", marker_color=["#f59e0b"] * len(regions), name="Ship cost %",
            ), row=1, col=2)
            fig.update_layout(
                height=380, showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0, r=0, t=40, b=0),
            )
            fig.update_xaxes(ticksuffix="%", row=1, col=2)
            st.plotly_chart(fig, use_container_width=True)
            st.info("📌 **Recommendation:** Central and South regions show high shipping cost ratios — audit fulfilment infrastructure before attributing underperformance to demand weakness.")

        with tab3:
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("#### Profit margin by category")
                categories  = ["Technology", "Office Supplies", "Furniture"]
                cat_margins = [0.147, 0.122, 0.051]
                fig1 = go.Figure(go.Bar(
                    x=categories, y=[m * 100 for m in cat_margins],
                    marker_color=["#3b82f6", "#6366f1", "#f59e0b"],
                    text=[f"{m*100:.1f}%" for m in cat_margins], textposition="outside",
                ))
                fig1.update_layout(
                    height=280, showlegend=False,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
                    yaxis=dict(ticksuffix="%"),
                )
                st.plotly_chart(fig1, use_container_width=True)
            with col_b:
                st.markdown("#### Profit per customer by segment")
                segments    = ["Consumer", "Corporate", "Home Office"]
                profit_cust = [312, 427, 389]
                fig2 = go.Figure(go.Bar(
                    x=segments, y=profit_cust,
                    marker_color=["#10b981", "#3b82f6", "#8b5cf6"],
                    text=[f"${v}" for v in profit_cust], textposition="outside",
                ))
                fig2.update_layout(
                    height=280, showlegend=False,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
                    yaxis=dict(title="Profit per Customer ($)"),
                )
                st.plotly_chart(fig2, use_container_width=True)

            st.markdown("#### Sub-category: profit vs. sales (bubble = absolute margin)")
            subcats    = ["Copiers", "Phones", "Accessories", "Paper", "Storage",
                          "Binders", "Art", "Appliances", "Bookcases", "Tables"]
            sub_sales  = [149528, 330007, 167380, 78479, 223844, 203413, 27119, 107532, 114880, 206966]
            sub_profit = [55618, 44516, 41937, 34054, 21279, 30222, 6528, 18138, -3473, -17725]
            sub_margin = [p / s for p, s in zip(sub_profit, sub_sales)]
            colors_sc  = ["#10b981" if p > 0 else "#ef4444" for p in sub_profit]
            fig3 = go.Figure(go.Scatter(
                x=sub_sales, y=sub_profit, mode="markers+text",
                text=subcats, textposition="top center",
                marker=dict(
                    size=[abs(m) * 600 + 14 for m in sub_margin],
                    color=colors_sc, opacity=0.85,
                    line=dict(width=1, color="white"),
                ),
            ))
            fig3.add_hline(y=0, line_dash="dot", line_color="#94a3b8")
            fig3.update_layout(
                height=380,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
                xaxis=dict(title="Total Sales ($)"), yaxis=dict(title="Total Profit ($)"),
            )
            st.plotly_chart(fig3, use_container_width=True)
            st.caption("Bubble size = absolute profit margin. Red = loss-making sub-category.")

    # ─── Project 4: Forecasting ──────────────────────────────────────────────
    elif project_tab == "Operations Forecasting":
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

        render_technical_code("Operations Forecasting")

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

    # ─── Project 6: CineGraph ────────────────────────────────────────────────
    elif project_tab == "CineGraph — Cinema & TV Analytics":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">HTML</span>
<span class="project-tag">JavaScript</span>
<span class="project-tag">Chart.js</span>
<span class="project-tag">TMDB</span>
            """, unsafe_allow_html=True)
            st.markdown("### CineGraph — Cinema & TV Analytics Dashboard")
            st.markdown("""
**Business problem:** The film industry generates enormous datasets, but most public tools lack a unified view
linking financial performance, audience ratings, genre trends, and director output across decades.

**Approach:** Built a fully custom analytical dashboard in pure **HTML + JavaScript (Chart.js)** using TMDB data.
Covered 20,000+ films and 15,000+ TV series, engineering derived metrics like ROI, avg budget/revenue ratios,
survivorship-adjusted decade ratings, and director efficiency scores.

**Key findings:**
- **Animation** leads in ROI (~3.7×) despite not having the highest budgets — driven by strong home media revenue.
- Average ratings **decline across decades** (7.42 in the 1920s → 6.42 in the 2000s) — a classic survivorship bias effect; only great old films survive.
- **Martin Scorsese** achieves the highest avg rating (★ 7.27) among directors with 25+ films — quality at scale.
- Micro-budget films dominate extreme ROI: *Fist of Fury* at ~100,000% ROI, *One Cut of the Dead* at 52,547%.
- **English** accounts for 73% of catalogued films; French (8%) is a distant second.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Dataset scope</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card" style="margin-bottom:10px">
  <div class="metric-value">20K+</div>
  <div class="metric-label">Films analysed</div>
  <div class="metric-delta">TMDB dataset</div>
</div>
<div class="metric-card">
  <div class="metric-value">15K+</div>
  <div class="metric-label">TV series</div>
  <div class="metric-delta">Status & genre breakdown</div>
</div>
            """, unsafe_allow_html=True)

        render_technical_code("CineGraph — Cinema & TV Analytics")

        tab1, tab2, tab3, tab4 = st.tabs(["Budget & Revenue", "Ratings over Time", "ROI & Directors", "Hall of Fame"])

        # ── Tab 1: Budget & Revenue ──────────────────────────────────────────
        with tab1:
            st.markdown("#### Average budget vs. revenue by genre (US$M)")
            genres_fin   = ["Animation","Adventure","Family","Sci-Fi","Fantasy","Action","Comedy","Thriller"]
            budgets      = [57.8, 65.4, 54.1, 56.7, 54.4, 52.5, 28.8, 28.6]
            revenues     = [214.5, 207.3, 173.5, 167.6, 160.2, 147.0, 84.6, 71.0]
            roi_mult     = [r / b for r, b in zip(revenues, budgets)]

            fig = go.Figure()
            fig.add_trace(go.Bar(name="Avg Budget ($M)", x=genres_fin, y=budgets,
                marker_color="#5b8dee", text=[f"${v}M" for v in budgets], textposition="outside"))
            fig.add_trace(go.Bar(name="Avg Revenue ($M)", x=genres_fin, y=revenues,
                marker_color="#e8b84b", text=[f"${v}M" for v in revenues], textposition="outside"))
            fig.update_layout(
                barmode="group", height=340, showlegend=True,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
                legend=dict(orientation="h", y=-0.2),
                yaxis=dict(tickprefix="$", ticksuffix="M"),
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("#### Revenue multiplier by genre (Revenue ÷ Budget)")
            colors_roi = ["#10b981" if r > 3 else "#f59e0b" if r > 2 else "#94a3b8" for r in roi_mult]
            fig2 = go.Figure(go.Bar(
                x=genres_fin, y=roi_mult,
                marker_color=colors_roi,
                text=[f"{r:.1f}×" for r in roi_mult], textposition="outside",
            ))
            fig2.add_hline(y=1, line_dash="dot", line_color="#ef4444",
                           annotation_text="Break-even", annotation_position="right")
            fig2.update_layout(
                height=260, showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
                yaxis=dict(title="Revenue / Budget"),
            )
            st.plotly_chart(fig2, use_container_width=True)
            st.info("📌 **Finding:** Animation returns $3.7 for every $1 spent — the highest multiplier of any genre, driven by global appeal and merchandise revenue streams.")

        # ── Tab 2: Ratings over Time ─────────────────────────────────────────
        with tab2:
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("#### Avg TMDB rating by decade")
                decades  = ["1920s","1930s","1940s","1950s","1960s","1970s","1980s","1990s","2000s","2010s","2020s"]
                d_rating = [7.42, 7.10, 7.14, 7.17, 7.06, 6.83, 6.55, 6.52, 6.42, 6.44, 6.72]
                fig3 = go.Figure(go.Scatter(
                    x=decades, y=d_rating, mode="lines+markers",
                    line=dict(color="#9b7de8", width=2),
                    marker=dict(size=7, color="#9b7de8"),
                    fill="tozeroy", fillcolor="rgba(155,125,232,0.08)",
                ))
                fig3.update_layout(
                    height=280, showlegend=False,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
                    yaxis=dict(range=[6.1, 7.7], title="Avg Rating"),
                    xaxis=dict(tickangle=30),
                )
                st.plotly_chart(fig3, use_container_width=True)
                st.caption("⚠️ Survivorship bias: only acclaimed older films remain in the dataset, inflating pre-1980 averages.")

            with col_b:
                st.markdown("#### Top TV genres by avg rating")
                tv_genres  = ["Animation","Family","War & Pol.","Sci-Fi","Action & Adv.","Kids","Documentary","Drama","Comedy","Mystery"]
                tv_ratings = [7.48, 7.40, 7.39, 7.38, 7.38, 7.36, 7.35, 7.31, 7.31, 7.28]
                fig4 = go.Figure(go.Bar(
                    y=tv_genres[::-1], x=tv_ratings[::-1], orientation="h",
                    marker_color=["#4ecdc4"] * 10,
                    text=[f"★ {r:.2f}" for r in tv_ratings[::-1]], textposition="outside",
                ))
                fig4.update_layout(
                    height=280, showlegend=False,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=60),
                    xaxis=dict(range=[7.0, 7.7]),
                )
                st.plotly_chart(fig4, use_container_width=True)

            # Language donut
            st.markdown("#### Film catalogue by original language")
            langs       = ["English","French","Spanish","Japanese","Italian","Others"]
            lang_counts = [14713, 1606, 907, 769, 763, 1635]
            fig5 = go.Figure(go.Pie(
                labels=langs, values=lang_counts,
                hole=0.65,
                marker_colors=["#e8b84b","#5b8dee","#9b7de8","#4ecdc4","#e05252","#64748b"],
                textinfo="label+percent",
            ))
            fig5.update_layout(
                height=300, showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
            )
            st.plotly_chart(fig5, use_container_width=True)

        # ── Tab 3: ROI & Directors ───────────────────────────────────────────
        with tab3:
            col_a, col_b = st.columns([3, 2])
            with col_a:
                st.markdown("#### Directors: avg rating vs. films directed")
                dir_names   = ["Woody Allen","Clint Eastwood","Alfred Hitchcock","Steven Spielberg",
                               "Martin Scorsese","Ridley Scott","Ron Howard","Pedro Almodóvar"]
                dir_films   = [51, 40, 38, 35, 29, 29, 28, 24]
                dir_ratings = [6.73, 6.84, 7.15, 7.19, 7.27, 6.81, 6.76, 6.99]
                fig6 = go.Figure(go.Scatter(
                    x=dir_films, y=dir_ratings,
                    mode="markers+text", text=dir_names,
                    textposition="top center",
                    marker=dict(
                        size=[f / 3 + 12 for f in dir_films],
                        color=dir_ratings,
                        colorscale=[[0,"#5b8dee"],[0.5,"#9b7de8"],[1,"#e8b84b"]],
                        showscale=True,
                        colorbar=dict(title="Rating", thickness=10, len=0.6),
                        line=dict(width=1, color="white"),
                    ),
                ))
                fig6.update_layout(
                    height=360,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0, r=40, t=20, b=0),
                    xaxis=dict(title="Films directed"),
                    yaxis=dict(title="Avg TMDB rating", range=[6.2, 7.5]),
                )
                st.plotly_chart(fig6, use_container_width=True)

            with col_b:
                st.markdown("#### Extreme ROI — micro-budget films")
                roi_films  = ["Fist of Fury","One Cut of Dead","Pink Flamingos",
                              "Open Water","Super Size Me","Bambi","Mad Max","El Mariachi"]
                roi_vals   = [99900, 52547, 49900, 45469, 43861, 31071, 28471, 28148]
                fig7 = go.Figure(go.Bar(
                    y=[f[:18] for f in roi_films[::-1]],
                    x=roi_vals[::-1],
                    orientation="h",
                    marker_color="#10b981",
                    text=[f"{v//1000}k%" for v in roi_vals[::-1]],
                    textposition="outside",
                ))
                fig7.update_layout(
                    height=360, showlegend=False,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0, r=40, t=20, b=0),
                    xaxis=dict(title="ROI (%)"),
                )
                st.plotly_chart(fig7, use_container_width=True)

            st.info("📌 **Finding:** Micro-budget productions ≤ $10K dominate extreme ROI. *Fist of Fury* (1972) generated ~100,000% return — the dataset's highest. These outliers illustrate why avg ROI metrics must be paired with median and distribution analysis.")

        # ── Tab 4: Hall of Fame ──────────────────────────────────────────────
        with tab4:
            st.markdown("#### Top-rated films — TMDB Hall of Fame")
            hof = [
                ("The Shawshank Redemption", 1994, 8.72, "30.1k"),
                ("The Godfather", 1972, 8.69, "22.8k"),
                ("The Godfather Part II", 1974, 8.57, "13.8k"),
                ("Schindler's List", 1993, 8.57, "17.3k"),
                ("12 Angry Men", 1957, 8.56, "9.9k"),
                ("Spirited Away", 2001, 8.53, "18.2k"),
                ("The Dark Knight", 2008, 8.53, "35.5k"),
                ("Dilwale Dulhania Le Jayenge", 1995, 8.52, "4.6k"),
            ]
            hof_df = pd.DataFrame(hof, columns=["Film", "Year", "Rating", "Votes"])
            hof_df.index = hof_df.index + 1

            fig8 = go.Figure(go.Bar(
                y=[f[0][:30] for f in hof[::-1]],
                x=[f[2] for f in hof[::-1]],
                orientation="h",
                marker=dict(
                    color=[f[2] for f in hof[::-1]],
                    colorscale=[[0,"#3b82f6"],[0.5,"#8b5cf6"],[1,"#e8b84b"]],
                    showscale=False,
                ),
                text=[f"★ {f[2]:.2f}  ({f[3]} votes)" for f in hof[::-1]],
                textposition="inside",
                insidetextanchor="end",
                textfont=dict(size=11, color="white"),
            ))
            fig8.update_layout(
                height=340, showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0, r=0, t=20, b=0),
                xaxis=dict(range=[8.4, 8.85], title="TMDB Rating"),
            )
            st.plotly_chart(fig8, use_container_width=True)
            st.caption("Data source: TMDB (The Movie Database). Ratings reflect weighted audience scores at time of data collection.")

    # ─── Project 7: Power BI — HR Analytics ─────────────────────────────────
    elif project_tab == "HR Analytics Dashboard":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">Power BI</span>
<span class="project-tag">DAX</span>
<span class="project-tag">HR Analytics</span>
            """, unsafe_allow_html=True)
            st.markdown("### HR Analytics — Attrition & Workforce Dashboard")
            st.markdown("""
**Business problem:** The HR team tracked headcount in spreadsheets and had no visibility into *why* people were leaving
or *which* departments were at risk. Attrition decisions were reactive, not data-driven.

**Approach:** Modeled People data (2,800 employees, 5 years) in Power BI with a star schema.
Built a DAX-driven dashboard covering attrition drivers, headcount evolution, performance distribution,
and hire-to-departure pipeline. Designed for self-service — HR managers filter by department,
band, and tenure without requesting reports.

**Key findings:**
- Engineering attrition (18.4%) is 2.3× the company average (8.0%) — concentrated in the 1–2 year tenure bucket.
- 62% of departures come from employees with fewer than 2 years tenure, pointing to onboarding gaps rather than compensation issues.
- High performers (band 4–5) are leaving 40% faster than average performers in Q3/Q4 — a retention risk concentrated in Q4 reviews.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Workforce snapshot</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card" style="margin-bottom:10px">
  <div class="metric-value">8.0%</div>
  <div class="metric-label">Overall attrition rate</div>
  <div class="metric-delta">↑ Engineering: 18.4%</div>
</div>
<div class="metric-card">
  <div class="metric-value">2,800</div>
  <div class="metric-label">Employees modelled</div>
  <div class="metric-delta">5 years of data</div>
</div>
            """, unsafe_allow_html=True)

        render_technical_code("HR Analytics Dashboard")

        tab1, tab2, tab3 = st.tabs(["Attrition Drivers", "Headcount & Hiring", "Performance"])

        with tab1:
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("#### Attrition rate by department")
                depts  = ["Engineering","Product","Sales","Design","Finance","Marketing","Operations","HR"]
                rates  = [18.4, 12.1, 10.8, 9.4, 7.2, 6.9, 5.8, 4.3]
                avg    = 8.0
                colors = ["#ef4444" if r > avg*1.5 else "#f59e0b" if r > avg else "#10b981" for r in rates]
                fig = go.Figure(go.Bar(
                    y=depts[::-1], x=rates[::-1], orientation="h",
                    marker_color=colors[::-1],
                    text=[f"{r}%" for r in rates[::-1]], textposition="outside",
                ))
                fig.add_vline(x=avg, line_dash="dot", line_color="#94a3b8",
                              annotation_text=f"Avg {avg}%", annotation_position="top right")
                fig.update_layout(height=300, showlegend=False,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0,r=40,t=20,b=0))
                st.plotly_chart(fig, use_container_width=True)

            with col_b:
                st.markdown("#### Attrition by tenure bucket")
                buckets = ["< 1 year","1–2 years","2–5 years","5–10 years","10+ years"]
                pct     = [28.4, 33.6, 19.2, 11.4, 7.4]
                fig2 = go.Figure(go.Bar(
                    x=buckets, y=pct,
                    marker_color=["#ef4444","#ef4444","#f59e0b","#10b981","#10b981"],
                    text=[f"{p}%" for p in pct], textposition="outside",
                ))
                fig2.update_layout(height=300, showlegend=False,
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                    yaxis=dict(title="% of departures"))
                st.plotly_chart(fig2, use_container_width=True)

            st.info("📌 **Power BI feature:** Drillthrough enabled — clicking any department bar opens a detailed employee-level view filtered by that department, including flight-risk scores and open positions.")

        with tab2:
            st.markdown("#### Headcount evolution (2020–2024)")
            months_hc = pd.date_range("2020-01", periods=60, freq="MS")
            np.random.seed(3)
            hires      = np.random.randint(18, 55, 60)
            departures = np.random.randint(8, 28, 60)
            headcount  = 1800 + np.cumsum(hires - departures)

            fig3 = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.6,0.4],
                                 subplot_titles=["Total Headcount","Monthly Hires vs Departures"])
            fig3.add_trace(go.Scatter(x=months_hc, y=headcount, fill="tozeroy",
                fillcolor="rgba(59,130,246,0.08)", line=dict(color="#3b82f6",width=2)), row=1, col=1)
            fig3.add_trace(go.Bar(x=months_hc, y=hires, name="Hires",
                marker_color="#10b981", opacity=0.8), row=2, col=1)
            fig3.add_trace(go.Bar(x=months_hc, y=-departures, name="Departures",
                marker_color="#ef4444", opacity=0.8), row=2, col=1)
            fig3.update_layout(height=380, showlegend=True, barmode="overlay",
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=40,b=0),
                legend=dict(orientation="h", y=-0.1))
            fig3.update_xaxes(showgrid=False)
            st.plotly_chart(fig3, use_container_width=True)

        with tab3:
            st.markdown("#### Performance band vs. attrition rate")
            bands_perf  = ["Band 1\n(Low)","Band 2","Band 3\n(Mid)","Band 4","Band 5\n(High)"]
            attr_rate_p = [14.2, 10.8, 6.4, 11.3, 13.7]
            headcount_p = [180, 420, 980, 760, 460]
            fig4 = make_subplots(specs=[[{"secondary_y": True}]])
            fig4.add_trace(go.Bar(x=bands_perf, y=headcount_p, name="Headcount",
                marker_color="rgba(99,102,241,0.3)"), secondary_y=False)
            fig4.add_trace(go.Scatter(x=bands_perf, y=attr_rate_p, name="Attrition %",
                mode="lines+markers", line=dict(color="#ef4444",width=2),
                marker=dict(size=8)), secondary_y=True)
            fig4.update_layout(height=300, paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)", font_family="DM Sans",
                margin=dict(l=0,r=0,t=20,b=0), legend=dict(orientation="h",y=-0.2))
            fig4.update_yaxes(title_text="Headcount", secondary_y=False)
            fig4.update_yaxes(title_text="Attrition %", secondary_y=True)
            st.plotly_chart(fig4, use_container_width=True)
            st.info("📌 **Key insight:** High performers (Band 5) churn almost as fast as low performers — the U-shaped curve suggests top talent is being lost, likely due to lack of growth opportunities rather than performance management issues.")

    # ─── Project 8: SQL — Data Warehouse Optimization ───────────────────────
    elif project_tab == "Data Warehouse & SQL Optimization":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">SQL</span>
<span class="project-tag">Data Modeling</span>
<span class="project-tag">BigQuery</span>
            """, unsafe_allow_html=True)
            st.markdown("### Data Warehouse Design & Query Optimization")
            st.markdown("""
**Business problem:** A mid-size e-commerce company was running all reporting directly on raw transactional
tables — 12 unjoined CSVs loaded into BigQuery. Every ad-hoc query took 4+ hours and returned inconsistent
results because analysts had different join logic. There was no single source of truth.

**Approach:** Designed a 3-layer Medallion architecture (Raw → Staging → Marts) using modular SQL CTEs
and incremental load patterns. Added data quality checks and documented every table's grain,
primary key, and update frequency.

**Key findings / results:**
- Avg query execution time dropped from **4h 12min → 7min 43sec** after materialized mart tables.
- Unified join logic eliminated 4 different conflicting revenue definitions across the company.
- 98.7% data quality score across 14 monitored tables (vs no monitoring before).
- Analyst self-sufficiency increased — 80% of recurring reports now run without engineering support.
            """)
        with col_impact:
            st.markdown('<div class="section-label">Performance gains</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card" style="margin-bottom:10px">
  <div class="metric-value">97%</div>
  <div class="metric-label">Query time reduction</div>
  <div class="metric-delta">4h 12min → 7min 43sec</div>
</div>
<div class="metric-card">
  <div class="metric-value">98.7%</div>
  <div class="metric-label">Data quality score</div>
  <div class="metric-delta">14 monitored tables</div>
</div>
            """, unsafe_allow_html=True)

        render_technical_code("Data Warehouse & SQL Optimization")

        tab1, tab2, tab3 = st.tabs(["Architecture", "Performance", "Data Quality"])

        with tab1:
            st.markdown("#### Medallion architecture — 3 layers")
            layers = ["RAW\n(source data)", "STAGING\n(typed & cleaned)", "INTERMEDIATE\n(business logic)", "MARTS\n(analytical tables)"]
            counts = [12, 12, 8, 5]
            descs  = ["CSV loads,\nno transforms","Cast, rename,\ndeduplicate","Joins, metrics,\nbusiness rules","Flat, wide tables\nfor BI / analysts"]
            colors = ["#94a3b8","#60a5fa","#818cf8","#4ade80"]

            fig = go.Figure()
            for i, (layer, count, desc, color) in enumerate(zip(layers, counts, descs, colors)):
                fig.add_trace(go.Bar(
                    x=[count], y=[i], orientation="h", name=layer,
                    marker_color=color,
                    text=f"  {layer}  ·  {count} tables  ·  {desc}",
                    textposition="inside", insidetextanchor="start",
                    textfont=dict(size=11),
                    width=0.5,
                ))
            fig.update_layout(height=260, showlegend=False, barmode="overlay",
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                xaxis=dict(visible=False), yaxis=dict(visible=False))
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("#### Sample — Mart table SQL pattern")
            st.code("""
-- mart_orders.sql  (BigQuery, materialized table, daily refresh)
WITH orders AS (
    SELECT * FROM {{ ref('int_orders_enriched') }}
),
customers AS (
    SELECT * FROM {{ ref('int_customers_segmented') }}
),
products AS (
    SELECT * FROM {{ ref('stg_products') }}
)

SELECT
    o.order_id,
    o.order_date,
    o.order_month,
    c.customer_id,
    c.segment,
    c.country,
    p.product_id,
    p.category,
    p.sub_category,
    o.quantity,
    o.sales,
    o.discount,
    o.profit,
    SAFE_DIVIDE(o.profit, o.sales)        AS profit_margin,
    SAFE_DIVIDE(o.shipping_cost, o.sales) AS shipping_cost_ratio,
    CASE
        WHEN o.discount = 0       THEN 'No Discount'
        WHEN o.discount <= 0.10   THEN '0–10%'
        WHEN o.discount <= 0.20   THEN '10–20%'
        WHEN o.discount <= 0.30   THEN '20–30%'
        ELSE '30%+'
    END AS discount_band

FROM orders o
LEFT JOIN customers c USING (customer_id)
LEFT JOIN products  p USING (product_id)
""", language="sql")

        with tab2:
            st.markdown("#### Query execution time — before vs. after")
            queries = ["Revenue by Region","Customer LTV","Churn Cohort","Funnel Analysis","KPI Summary","Product Margin"]
            before  = [252, 187, 310, 198, 145, 223]
            after   = [8, 5, 11, 7, 3, 6]

            fig2 = go.Figure()
            fig2.add_trace(go.Bar(name="Before (raw tables)", x=queries, y=before,
                marker_color="#ef4444", text=[f"{v}min" for v in before], textposition="outside"))
            fig2.add_trace(go.Bar(name="After (mart tables)", x=queries, y=after,
                marker_color="#10b981", text=[f"{v}min" for v in after], textposition="outside"))
            fig2.update_layout(barmode="group", height=320, showlegend=True,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                legend=dict(orientation="h",y=-0.2),
                yaxis=dict(title="Minutes"))
            st.plotly_chart(fig2, use_container_width=True)

            st.markdown("#### Optimization techniques applied")
            optimizations = pd.DataFrame({
                "Technique": ["Materialized mart tables","Clustered by date + customer_id",
                              "Partitioned by order_month","Incremental load (merge)",
                              "Eliminated SELECT *","Pushed filters to CTEs"],
                "Impact": ["★★★★★","★★★★☆","★★★★☆","★★★☆☆","★★☆☆☆","★★★☆☆"],
                "Time saved": ["~3h 40min","~18min","~11min","Reduces daily cost","Minor","~7min"],
            })
            st.dataframe(optimizations, use_container_width=True, hide_index=True)

        with tab3:
            st.markdown("#### Data quality test results by layer")
            test_types = ["Not Null","Unique","Accepted Values","Referential Integrity","Custom Business Rules"]
            raw_pass   = [61, 43, 78, 32, 0]
            mart_pass  = [100, 100, 100, 98, 94]

            fig3 = go.Figure()
            fig3.add_trace(go.Bar(name="Before (no tests)", x=test_types, y=raw_pass,
                marker_color="rgba(239,68,68,0.6)", text=[f"{v}%" for v in raw_pass], textposition="outside"))
            fig3.add_trace(go.Bar(name="After (dbt tests)", x=test_types, y=mart_pass,
                marker_color="rgba(16,185,129,0.8)", text=[f"{v}%" for v in mart_pass], textposition="outside"))
            fig3.update_layout(barmode="group", height=300,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                legend=dict(orientation="h",y=-0.2),
                yaxis=dict(title="Pass rate (%)", range=[0,115]))
            st.plotly_chart(fig3, use_container_width=True)

    # ─── Project 9: R — A/B Testing & Statistical Analysis ──────────────────
    elif project_tab == "A/B Testing & Regression — R":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">R</span>
<span class="project-tag">Statistics</span>
<span class="project-tag">A/B Testing</span>
            """, unsafe_allow_html=True)
            st.markdown("### A/B Testing & Regression — Statistical Rigour in R")
            st.markdown("""
**Business problem:** The product team declared a checkout redesign "a success" based on a 0.4 p.p.
conversion lift — but the test ran for only 4 days, violated the stopping rule,
and had no pre-registered hypothesis. The result was not reproducible.

**Approach:** Rebuilt the entire experimentation framework in R using `tidyverse`, `broom`, and `pwr`.
Ran a proper two-sample t-test with pre-calculated sample size, defined primary metric (conversion rate)
and guardrail metrics (bounce rate, session duration) before launch, and applied Bonferroni correction for
multiple comparisons.

**Key findings:**
- The original "significant" result vanished under correct analysis — the 0.4 p.p. lift had p = 0.31.
- A follow-up 4-week test with adequate power (n=12,400/group) found a genuine 1.1 p.p. lift with p = 0.018 and Cohen's h = 0.031.
- Even the confirmed lift was below the minimum detectable effect threshold for the company's cost of change — the recommendation was **not to ship**.
- Regression analysis revealed device type (mobile vs desktop) was a stronger predictor of conversion than the UI variant (β = 0.12 vs β = 0.031).
            """)
        with col_impact:
            st.markdown('<div class="section-label">Test outcome</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card" style="margin-bottom:10px">
  <div class="metric-value">p = 0.018</div>
  <div class="metric-label">Confirmed result</div>
  <div class="metric-delta">After proper test design</div>
</div>
<div class="metric-card">
  <div class="metric-value">Not ship</div>
  <div class="metric-label">Final recommendation</div>
  <div class="metric-delta">Effect below cost threshold</div>
</div>
            """, unsafe_allow_html=True)

        render_technical_code("A/B Testing & Regression — R")

        tab1, tab2, tab3 = st.tabs(["Distribution & Test", "Confidence Intervals", "Regression"])

        with tab1:
            st.markdown("#### Conversion rate distribution — Control vs Treatment")
            np.random.seed(42)
            n = 12400
            control_cvr   = np.random.beta(52, 948, n)
            treatment_cvr = np.random.beta(53.6, 946.4, n)

            fig = go.Figure()
            fig.add_trace(go.Histogram(x=control_cvr*100, name="Control", nbinsx=60,
                marker_color="rgba(99,102,241,0.5)", histnorm="probability density"))
            fig.add_trace(go.Histogram(x=treatment_cvr*100, name="Treatment", nbinsx=60,
                marker_color="rgba(16,185,129,0.5)", histnorm="probability density"))
            fig.add_vline(x=np.mean(control_cvr)*100, line_dash="dash", line_color="#6366f1",
                          annotation_text=f"μ={np.mean(control_cvr)*100:.2f}%")
            fig.add_vline(x=np.mean(treatment_cvr)*100, line_dash="dash", line_color="#10b981",
                          annotation_text=f"μ={np.mean(treatment_cvr)*100:.2f}%")
            fig.update_layout(barmode="overlay", height=300,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                legend=dict(orientation="h",y=-0.2),
                xaxis=dict(title="Conversion Rate (%)"))
            st.plotly_chart(fig, use_container_width=True)

            col_r, col_stats = st.columns(2)
            with col_r:
                st.markdown("#### R code — two-sample t-test")
                st.code("""
library(tidyverse)
library(broom)
library(pwr)

# Pre-experiment: sample size calculation
pwr.2p.test(
  h    = ES.h(0.052, 0.041),  # MDE = 1.1 p.p.
  sig.level = 0.05,
  power     = 0.80,
  alternative = "two.sided"
)
# Required n = 12,388 per group ✓

# Two-sample t-test on results
t_result <- t.test(
  conversion ~ variant,
  data        = experiment_data,
  alternative = "two.sided",
  conf.level  = 0.95
) |> tidy()

t_result |>
  select(estimate1, estimate2, statistic, p.value, conf.low, conf.high)
""", language="r")
            with col_stats:
                st.markdown("#### Statistical summary")
                stats_df = pd.DataFrame({
                    "Metric": ["Control CVR","Treatment CVR","Absolute lift","Relative lift",
                               "t-statistic","p-value","Cohen's h","Decision"],
                    "Value":  ["5.20%","6.30%","+1.10 p.p.","+ 21.2%",
                               "2.38","0.018","0.031","Do not ship ⚠️"],
                })
                st.dataframe(stats_df, use_container_width=True, hide_index=True)

        with tab2:
            st.markdown("#### 95% confidence intervals — daily snapshots during test")
            days = list(range(1, 29))
            np.random.seed(7)
            ctrl_daily = 5.2 + np.random.randn(28) * 0.3
            trt_daily  = 6.3 + np.random.randn(28) * 0.3
            ctrl_ci    = 0.8 - days[0] / (len(days) * 1.5) + np.random.rand(28) * 0.1
            trt_ci     = 0.8 - days[0] / (len(days) * 1.5) + np.random.rand(28) * 0.1

            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=days + days[::-1],
                y=list(ctrl_daily + ctrl_ci) + list((ctrl_daily - ctrl_ci)[::-1]),
                fill="toself", fillcolor="rgba(99,102,241,0.1)",
                line=dict(color="rgba(0,0,0,0)"), showlegend=False))
            fig2.add_trace(go.Scatter(x=days, y=ctrl_daily, name="Control",
                line=dict(color="#6366f1", width=2)))
            fig2.add_trace(go.Scatter(
                x=days + days[::-1],
                y=list(trt_daily + trt_ci) + list((trt_daily - trt_ci)[::-1]),
                fill="toself", fillcolor="rgba(16,185,129,0.1)",
                line=dict(color="rgba(0,0,0,0)"), showlegend=False))
            fig2.add_trace(go.Scatter(x=days, y=trt_daily, name="Treatment",
                line=dict(color="#10b981", width=2)))
            fig2.update_layout(height=300,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                legend=dict(orientation="h",y=-0.2),
                xaxis=dict(title="Day of experiment"),
                yaxis=dict(title="Conversion Rate (%)"))
            st.plotly_chart(fig2, use_container_width=True)
            st.info("📌 **Key insight:** Confidence intervals only stop overlapping after day 22 — the original 4-day test was massively underpowered. Stopping early inflated the apparent effect size by ~3×.")

        with tab3:
            st.markdown("#### Logistic regression — predictors of conversion")
            predictors = ["Device: Mobile","UI Variant (Treatment)","Session Duration","Source: Organic",
                          "Return Visitor","Time of Day (Evening)","Source: Paid"]
            betas      = [-0.120, 0.031, 0.089, 0.074, 0.062, 0.041, -0.028]
            ci_low     = [b - 0.018 for b in betas]
            ci_high    = [b + 0.018 for b in betas]
            colors_reg = ["#ef4444" if b < 0 else "#10b981" for b in betas]

            fig3 = go.Figure()
            for i, (pred, b, lo, hi, c) in enumerate(zip(predictors, betas, ci_low, ci_high, colors_reg)):
                fig3.add_trace(go.Scatter(x=[lo, hi], y=[i, i], mode="lines",
                    line=dict(color=c, width=3), showlegend=False))
                fig3.add_trace(go.Scatter(x=[b], y=[i], mode="markers",
                    marker=dict(size=10, color=c), showlegend=False,
                    name=pred))
            fig3.add_vline(x=0, line_dash="dot", line_color="#94a3b8")
            fig3.update_layout(height=300, showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=160,t=20,b=0),
                yaxis=dict(tickvals=list(range(len(predictors))),
                           ticktext=predictors),
                xaxis=dict(title="Coefficient (β)", zeroline=False))
            st.plotly_chart(fig3, use_container_width=True)
            st.caption("Error bars = 95% CI. Device type has 4× the impact of the UI variant — mobile optimisation is a higher-priority lever.")

    # ─── Project 10: Data Engineering — Airflow + dbt + BigQuery ────────────
    elif project_tab == "ETL Pipeline — Airflow + dbt + BigQuery":
        col_desc, col_impact = st.columns([2, 1])
        with col_desc:
            st.markdown("""
<span class="project-tag">Airflow</span>
<span class="project-tag">dbt</span>
<span class="project-tag">BigQuery</span>
<span class="project-tag">Data Engineering</span>
            """, unsafe_allow_html=True)
            st.markdown("### ETL Pipeline — Apache Airflow + dbt + BigQuery")
            st.markdown("""
**Business problem:** A manual pipeline ran by 2 engineers every morning took 6+ hours, failed silently
(no alerting, no lineage, no retries), and blocked the entire analytics team from having fresh data before
the daily standup. Any failure required 4+ hours of manual investigation to identify the broken step.

**Approach:** Redesigned the pipeline as a fully orchestrated, testable, documented system:
**Apache Airflow** for orchestration and scheduling, **dbt** for transformation logic with data tests
and lineage documentation, **BigQuery** as the data warehouse with partitioned and clustered tables.
Added Slack alerting, automatic retries, and a monitoring dashboard.

**Results:**
- Pipeline runtime: **6h manual → 43min automated**, running daily at 05:00 UTC.
- Mean time to detect a failure: **4+ hours → under 3 minutes** (Slack alert with task name and error).
- dbt test suite: 142 tests across 37 models, 98.6% pass rate on production data.
- Data freshness SLA: 99.1% of mornings with fresh data before 06:00 UTC (target: 95%).
            """)
        with col_impact:
            st.markdown('<div class="section-label">Pipeline metrics</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="metric-card" style="margin-bottom:10px">
  <div class="metric-value">43 min</div>
  <div class="metric-label">Daily pipeline runtime</div>
  <div class="metric-delta">Was: 6+ hours manual</div>
</div>
<div class="metric-card">
  <div class="metric-value">99.1%</div>
  <div class="metric-label">Freshness SLA</div>
  <div class="metric-delta">Target: 95%</div>
</div>
            """, unsafe_allow_html=True)

        render_technical_code("ETL Pipeline — Airflow + dbt + BigQuery")

        tab1, tab2, tab3 = st.tabs(["Pipeline Architecture", "Run Performance", "dbt Tests"])

        with tab1:
            st.markdown("#### DAG structure — daily pipeline")
            st.code("""
# airflow/dags/daily_analytics_pipeline.py
from airflow.decorators import dag, task
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
from pendulum import datetime

@dag(
    schedule="0 5 * * *",          # 05:00 UTC daily
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["analytics", "production"],
    on_failure_callback=slack_alert, # Slack on any failure
)
def daily_analytics_pipeline():

    # 1. Extract: load raw CSVs from GCS → BigQuery raw layer
    load_orders    = GCSToBigQueryOperator(task_id="load_raw_orders",    ...)
    load_customers = GCSToBigQueryOperator(task_id="load_raw_customers", ...)
    load_products  = GCSToBigQueryOperator(task_id="load_raw_products",  ...)

    # 2. Transform: run dbt models (staging → intermediate → marts)
    dbt_run  = DbtCloudRunJobOperator(task_id="dbt_run",  job_id=12345, ...)
    dbt_test = DbtCloudRunJobOperator(task_id="dbt_test", job_id=12346, ...)

    # 3. Load: refresh Looker Studio cache
    refresh_dashboards = refresh_looker_cache(task_id="refresh_dashboards")

    # DAG dependencies
    [load_orders, load_customers, load_products] >> dbt_run >> dbt_test >> refresh_dashboards
""", language="python")

            st.markdown("#### dbt model layers")
            layers_de = {
                "Sources": {"count": 4, "desc": "Raw BigQuery tables from Airflow loads", "color": "#94a3b8"},
                "Staging": {"count": 12, "desc": "Cast, rename, deduplicate — 1:1 with sources", "color": "#60a5fa"},
                "Intermediate": {"count": 14, "desc": "Business joins, metric calculation", "color": "#818cf8"},
                "Marts": {"count": 7, "desc": "Wide flat tables for BI / analysts", "color": "#4ade80"},
                "Exposures": {"count": 4, "desc": "Looker Studio dashboards documented in dbt", "color": "#f59e0b"},
            }
            for layer, info in layers_de.items():
                st.markdown(
                    f'<div style="display:flex;align-items:center;gap:12px;margin:6px 0;">'
                    f'<div style="width:12px;height:12px;border-radius:3px;background:{info["color"]};flex-shrink:0"></div>'
                    f'<div style="font-weight:600;width:120px">{layer}</div>'
                    f'<div style="background:rgba(128,128,128,0.12);padding:2px 8px;border-radius:99px;font-size:12px;width:30px;text-align:center">{info["count"]}</div>'
                    f'<div style="font-size:13px;opacity:.7">{info["desc"]}</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

        with tab2:
            st.markdown("#### Pipeline run time — 90-day trend")
            np.random.seed(11)
            run_dates = pd.date_range("2024-01-01", periods=90, freq="D")
            run_times = 43 + np.random.randn(90) * 4
            failures  = np.random.choice([None]*87 + [None, 1, 1], 90)

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=run_dates, y=run_times, mode="lines",
                line=dict(color="#6366f1", width=1.5), fill="tozeroy",
                fillcolor="rgba(99,102,241,0.07)", name="Run time (min)"))

            fail_dates = run_dates[[i for i,f in enumerate(failures) if f]]
            fail_times = run_times[[i for i,f in enumerate(failures) if f]]
            fig.add_trace(go.Scatter(x=fail_dates, y=fail_times, mode="markers",
                marker=dict(size=10, color="#ef4444", symbol="x"), name="Failure / retry"))

            fig.add_hline(y=60, line_dash="dot", line_color="#f59e0b",
                          annotation_text="SLA ceiling: 60min")
            fig.update_layout(height=300,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                legend=dict(orientation="h",y=-0.2),
                yaxis=dict(title="Minutes"))
            fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig, use_container_width=True)

            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Avg runtime", "43.2 min", delta="-5h 17min vs before")
                st.metric("Pipeline failures (90d)", "2", delta="-14 vs manual")
            with col_b:
                st.metric("MTTR (mean time to recover)", "4 min", delta="-4h 26min")
                st.metric("Freshness SLA met", "99.1%", delta="Target: 95%")

        with tab3:
            st.markdown("#### dbt test suite — 37 models, 142 tests")
            models = ["stg_orders","stg_customers","stg_products","int_orders_enriched",
                      "int_customers_segmented","mart_orders","mart_churn_risk"]
            not_null = [100,100,100,100,100,100,100]
            unique   = [100,100,100,100,100,100,98]
            ref_intg = [100,100,100,97,100,100,95]
            biz_rule = [94,91,100,88,96,90,87]

            fig2 = go.Figure()
            for test_name, vals, color in zip(
                ["Not Null","Unique","Ref. Integrity","Business Rules"],
                [not_null, unique, ref_intg, biz_rule],
                ["#4ade80","#60a5fa","#818cf8","#f59e0b"]
            ):
                fig2.add_trace(go.Bar(name=test_name, x=models, y=vals,
                    marker_color=color))
            fig2.add_hline(y=95, line_dash="dot", line_color="#94a3b8",
                           annotation_text="95% threshold")
            fig2.update_layout(barmode="group", height=340,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_family="DM Sans", margin=dict(l=0,r=0,t=20,b=0),
                legend=dict(orientation="h",y=-0.2),
                yaxis=dict(title="Pass rate (%)", range=[80,105]))
            st.plotly_chart(fig2, use_container_width=True)
            st.caption("Business rule tests cover domain-specific checks: no negative revenue, discount ≤ 1.0, order_date ≤ ship_date, country codes in ISO whitelist.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SKILLS
# ══════════════════════════════════════════════════════════════════════════════
elif "Skills" in page:
    st.markdown("## Technical skills")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### Analytics & Reporting")
        analytics_skills = {
            "Excel (Advanced)": 95,
            "KPI / SLA Analysis": 92,
            "Dashboard Design": 88,
            "SQL": 65,
            "Python (fundamentals)": 55,
        }
        for skill, level in analytics_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(level / 100)

        st.markdown("#### BI & Visualization")
        bi_skills = {
            "Tableau (fundamentals)": 60,
            "Power BI": 58,
            "Operational Reporting": 92,
        }
        for skill, level in bi_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(level / 100)

        st.markdown("#### Analytical Methods")
        methods = [
            "KPI / SLA Monitoring", "Trend Analysis", "Root Cause Analysis",
            "Executive Reporting", "Operational Reporting", "Incident Analysis",
            "Performance Benchmarking", "Process Improvement",
        ]
        pills = "".join(f'<span class="skill-pill">{m}</span>' for m in methods)
        st.markdown(pills, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Service Management & ITSM")
        itsm_skills = {
            "ServiceNow": 90,
            "ITIL (certified)": 88,
            "Incident Management": 92,
            "Escalation Management": 90,
            "Service Continuity": 88,
        }
        for skill, level in itsm_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(level / 100)

        st.markdown("#### Cloud, Data & Emerging Tech")
        cloud = [
            "Google Cloud (certified)", "Databricks (certified)",
            "Neo4j (certified)", "CSV / ETL", "Mainframe z/OS",
            "Control-M / CA-7", "Scrum Master (certified)",
        ]
        pills2 = "".join(f'<span class="skill-pill">{m}</span>' for m in cloud)
        st.markdown(pills2, unsafe_allow_html=True)

        st.markdown("#### Languages")
        langs = [("🇧🇷 Portuguese", 100, "Native"),
                 ("🇺🇸 English", 72, "B2 Upper-Intermediate"),
                 ("🇪🇸 Spanish", 70, "Professional Working")]
        for flag, level, label in langs:
            st.markdown(f"**{flag}** — *{label}*")
            st.progress(level / 100)

    st.markdown("---")
    st.markdown("#### Skill radar")
    categories = ["Excel / Reporting", "KPI / SLA", "ITSM / ServiceNow", "SQL", "Python", "BI Tools", "Leadership"]
    values_self = [95, 92, 90, 65, 55, 60, 85]
    values_self.append(values_self[0])
    categories.append(categories[0])

    fig = go.Figure(go.Scatterpolar(
        r=values_self, theta=categories,
        fill="toself", fillcolor="rgba(59,130,246,0.15)",
        line_color="#3b82f6", name="Self-assessment",
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False, height=420,
        paper_bgcolor="rgba(0,0,0,0)", font_family="DM Sans",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: RESUME
# ══════════════════════════════════════════════════════════════════════════════
elif "Resume" in page:
    st.markdown("## Carlos Maximino")
    st.markdown('<div class="main-subtitle">Brazil &nbsp;·&nbsp; +55 19 99379-2916 &nbsp;·&nbsp; cmax15@outlook.com.br &nbsp;·&nbsp; <a href="https://www.linkedin.com/in/carlos-maximino/" target="_blank">LinkedIn ↗</a></div>', unsafe_allow_html=True)

    # ── Summary ──────────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("### Professional Summary")
    st.markdown("""
Data and Analytics professional with **10+ years of progressive experience** across enterprise IT operations, mainframe environments,
service delivery, KPI/SLA monitoring, incident management, team leadership, and business performance reporting.

Currently working as a **Data Analyst at Kyndryl**, transforming operational, service, and business performance data into dashboards,
executive reports, and decision-ready insights for managers, DPEs, internal teams, and client stakeholders at **Delta Air Lines**.
Experienced analyzing data across 10 processes and 9 service areas, maintaining 20 recurring reports and dashboards,
and supporting performance improvement and data-driven decision-making.

**Career progression:** Mainframe Operations → Agile Coordination → Service Delivery → Team Leadership → Data Analytics
    """)

    # ── Experience ───────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("### Professional Experience")

    experiences = [
        {
            "title": "Data Analyst — Service Performance, KPIs & Business Insights",
            "company": "Kyndryl · Brazil",
            "period": "May 2024 – Present",
            "color": "#dbeafe",
            "text_color": "#1e40af",
            "bullets": [
                "Developed and maintained **20 recurring reports and dashboards** covering KPIs, SLAs, productivity, ticket trends, and business performance.",
                "Analyzed data across **10 processes** and **9 service areas** to identify trends, anomalies, risks, and improvement opportunities.",
                "Supported Delta Air Lines stakeholders, managers, and DPEs with daily and on-demand performance analysis.",
                "Delivered **10 weekly** and **5 monthly** insights to support operational reviews, performance tracking, and service governance.",
                "Prepared monthly executive presentations with KPI/SLA results, trends, risks, and improvement opportunities for client executives.",
                "Consolidated CSV and operational data sources to improve reporting consistency and management visibility.",
            ]
        },
        {
            "title": "Team Leader — Mainframe Support, Service Performance & Incident Management",
            "company": "Kyndryl · Brazil",
            "period": "Jan 2022 – May 2024",
            "color": "#ede9fe",
            "text_color": "#5b21b6",
            "bullets": [
                "Led a **40-person mainframe support team** for Delta Air Lines, ensuring service stability, SLA compliance, and operational continuity.",
                "Used ServiceNow to monitor incident queues, SLA adherence, ticket aging, escalations, and service performance indicators.",
                "Reviewed 3 daily, 5 monthly, and on-demand service performance reports; maintained weekly/monthly updated KPI dashboards.",
                "Identified recurring issues, process gaps, and improvement opportunities to improve efficiency and service quality.",
                "Coached team members on ServiceNow, incident handling, escalation processes, and operational routines.",
            ]
        },
        {
            "title": "Service Delivery Analyst — Mainframe Support, SLAs & Stakeholder Management",
            "company": "Kyndryl · Brazil",
            "period": "Sep 2021 – Jul 2022",
            "color": "#f3e8ff",
            "text_color": "#6b21a8",
            "bullets": [
                "Managed service delivery for Delta Air Lines mainframe support after IBM-to-Kyndryl transition, ensuring continuity and SLA tracking.",
                "Prepared 3 daily, 5 monthly, and on-demand service performance reports with SLA status, incident trends, and improvement opportunities.",
                "Acted as interface between technical teams, leadership, and stakeholders on performance, priorities, and escalations.",
            ]
        },
        {
            "title": "Service Delivery Analyst — Mainframe Support, SLAs & Service Continuity",
            "company": "IBM · Brazil",
            "period": "Dec 2019 – Sep 2021",
            "color": "#e0f2fe",
            "text_color": "#0369a1",
            "bullets": [
                "Managed service delivery for Delta Air Lines mainframe environment; monitored SLA/KPI performance across 9 service areas.",
                "Prepared recurring service performance reports covering incidents, SLA status, risks, and operational trends.",
                "Supported service continuity during the IBM-to-Kyndryl organizational transition.",
            ]
        },
        {
            "title": "Agile Project Coordinator / Scrum Master — Mainframe Operations",
            "company": "IBM · Brazil",
            "period": "Jan 2019 – Dec 2019",
            "color": "#f0fdf4",
            "text_color": "#166534",
            "bullets": [
                "Acted as Scrum Master in a mainframe operations environment, facilitating ceremonies, sprint planning, reviews, and retrospectives.",
                "Tracked sprint progress, risks, blockers, and velocity in a high-demand, mission-critical operations context.",
            ]
        },
        {
            "title": "Mainframe Operations Analyst — z/OS, Batch Processing & Incident Management",
            "company": "IBM · Brazil",
            "period": "Mar 2014 – Dec 2019",
            "color": "#fefce8",
            "text_color": "#854d0e",
            "bullets": [
                "Monitored IBM Mainframe z/OS production environments for **24 clients**, ensuring service continuity across mission-critical operations.",
                "Managed batch processing using JCL; handled average of **15 daily failed jobs** with L1/L2 incident management.",
                "Used SDSF, JES2/JES3, Control-M, CA-7, OPC/TWS, FTP, and Connect:Direct for production monitoring and incident resolution.",
            ]
        },
    ]

    for exp in experiences:
        badge = f'<span style="background:{exp["color"]};color:{exp["text_color"]};font-size:11px;font-weight:600;padding:3px 10px;border-radius:99px;">{exp["period"]}</span>'
        st.markdown(f"**{exp['title']}**  \n{exp['company']} &nbsp; {badge}", unsafe_allow_html=True)
        for b in exp["bullets"]:
            st.markdown(f"- {b}")
        st.markdown("")

    # ── Education ────────────────────────────────────────────────────────────
    st.markdown("---")
    col_edu, col_cert = st.columns(2, gap="large")

    with col_edu:
        st.markdown("### Education")
        edu = [
            ("MBA in IT Project Management", "Fundação Getúlio Vargas — FGV", "Jan 2019 – Jun 2020"),
            ("Bachelor's in Information Systems Management", "Centro Universitário Adventista — UNASP", "Feb 2013 – Dec 2016"),
            ("Technical Diploma in Information Technology", "ETEC — Escola Técnica Estadual de SP", "Jun 2010 – Dec 2011"),
        ]
        for degree, school, period in edu:
            st.markdown(f"**{degree}**  \n{school}  \n*{period}*")
            st.markdown("")

    with col_cert:
        st.markdown("### Certifications")
        certs = [
            ("Neo4j Graph Data Science Certification", "Neo4j", "Apr 2026"),
            ("Neo4j Certified Professional", "Neo4j", "Apr 2026"),
            ("Databricks Lakehouse Fundamentals", "Databricks", "Apr 2026"),
            ("Data Analytics Essentials", "Cisco", "Sep 2025"),
            ("Data Science & AI Fundamentals", "Data Science Academy", "Sep 2025"),
            ("Cloud Digital Leader", "Google", "Feb 2024"),
            ("Scrum Master Professional Certificate", "CertiProf", "Feb 2021"),
            ("ITIL Foundation Certificate", "AXELOS", "Dec 2016"),
            ("Professional Scrum Master I", "Scrum.org", "Jul 2016"),
        ]
        for cert, issuer, date in certs:
            st.markdown(f"- **{cert}** — {issuer} *({date})*")

    # ── Languages ────────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("### Languages")
    lc1, lc2, lc3 = st.columns(3)
    with lc1:
        st.metric("🇧🇷 Portuguese", "Native")
    with lc2:
        st.metric("🇺🇸 English", "B2 Upper-Intermediate")
    with lc3:
        st.metric("🇪🇸 Spanish", "Professional Working")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif "Contact" in page:
    st.markdown("## Let's connect")
    st.markdown('<div class="main-subtitle">Open to remote roles, relocation, and new opportunities.</div>', unsafe_allow_html=True)

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
- 💼 **LinkedIn** — [linkedin.com/in/carlos-maximino](https://www.linkedin.com/in/carlos-maximino/)
- 📧 **Email** — cmax15@outlook.com.br
- 📱 **Phone** — +55 19 99379-2916
        """)
        st.markdown("---")
        st.markdown("### Availability")
        st.info("✅ **Open to new opportunities.**\n\nPreferences: Remote-first · Data & Business Analytics · International teams · Relocation considered.")
