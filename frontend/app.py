import streamlit as st
import plotly.graph_objects as go
import requests

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Agentic BI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* ---------- Global ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 10%,
                rgba(99, 102, 241, 0.10),
                transparent 28%
            ),
            radial-gradient(
                circle at 10% 90%,
                rgba(14, 165, 233, 0.07),
                transparent 25%
            ),
            #080b12;
        color: #f1f5f9;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"] {
        background: #0b0f18;
        border-right: 1px solid rgba(255,255,255,0.07);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    .brand {
        padding: 0 0.8rem 1.5rem 0.8rem;
    }

    .brand-title {
        font-size: 1.45rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .brand-subtitle {
        color: #64748b;
        font-size: 0.75rem;
        margin-top: 3px;
    }

    .nav-label {
        color: #64748b;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin: 1.5rem 0 0.5rem 0.8rem;
        text-transform: uppercase;
    }

    /* ---------- Header ---------- */

    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
    }

    .eyebrow {
        color: #818cf8;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -1.2px;
        line-height: 1.1;
    }

    .main-subtitle {
        color: #94a3b8;
        margin-top: 0.6rem;
        font-size: 0.95rem;
    }

    .status-pill {
        background: rgba(34, 197, 94, 0.08);
        border: 1px solid rgba(34, 197, 94, 0.2);
        border-radius: 999px;
        color: #86efac;
        padding: 0.5rem 0.9rem;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* ---------- AI Search ---------- */

    .ai-panel {
        background:
            linear-gradient(
                135deg,
                rgba(99,102,241,0.14),
                rgba(14,165,233,0.05)
            );
        border: 1px solid rgba(129,140,248,0.20);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .ai-title {
        font-size: 1.05rem;
        font-weight: 750;
        margin-bottom: 0.3rem;
    }

    .ai-description {
        color: #94a3b8;
        font-size: 0.82rem;
        margin-bottom: 1rem;
    }

    /* ---------- KPI Cards ---------- */

    .kpi-card {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 16px;
        padding: 1.2rem 1.25rem;
        min-height: 125px;
    }

    .kpi-label {
        color: #94a3b8;
        font-size: 0.78rem;
        font-weight: 600;
    }

    .kpi-value {
        color: #f8fafc;
        font-size: 1.65rem;
        font-weight: 800;
        margin-top: 0.4rem;
        letter-spacing: -0.5px;
    }

    .kpi-meta {
        color: #64748b;
        font-size: 0.72rem;
        margin-top: 0.35rem;
    }

    /* ---------- Section ---------- */

    .section-title {
        font-size: 1.15rem;
        font-weight: 750;
        margin-top: 1.8rem;
        margin-bottom: 0.9rem;
    }

    /* ---------- Insight ---------- */

    .insight-card {
        background: rgba(15,23,42,0.70);
        border-left: 3px solid #818cf8;
        border-radius: 12px;
        padding: 1rem 1.1rem;
        margin-bottom: 0.7rem;
    }

    .insight-heading {
        font-size: 0.8rem;
        color: #a5b4fc;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }

    .insight-text {
        font-size: 0.84rem;
        color: #cbd5e1;
        line-height: 1.5;
    }

    /* ---------- Recommendation ---------- */

    .recommendation-card {
        background: rgba(15,23,42,0.70);
        border-left: 3px solid #38bdf8;
        border-radius: 12px;
        padding: 1rem 1.1rem;
        margin-bottom: 0.7rem;
    }

    .recommendation-heading {
        font-size: 0.8rem;
        color: #7dd3fc;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }

    .recommendation-text {
        font-size: 0.84rem;
        color: #cbd5e1;
        line-height: 1.5;
    }

    /* ---------- Buttons ---------- */

    .stButton > button {
        border-radius: 10px;
        font-weight: 700;
        min-height: 42px;
    }

    /* ---------- Hide Streamlit Branding ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-title">◈ Agentic BI</div>
            <div class="brand-subtitle">
                AI-Powered Business Intelligence
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="nav-label">Workspace</div>',
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "AI Analyst",
            "Insights",
            "Reports",
            "History",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="nav-label">System</div>',
        unsafe_allow_html=True,
    )

    st.caption("● PostgreSQL Connected")
    st.caption("● AI Engine Ready")
    st.caption("v0.1.0")


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="top-header">
        <div>
            <div class="eyebrow">Business Intelligence Platform</div>
            <div class="main-title">Decision Intelligence</div>
            <div class="main-subtitle">
                Explore business performance using natural language,
                AI-generated analysis, and strategic recommendations.
            </div>
        </div>


    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# AI QUESTION PANEL
# ---------------------------------------------------------

st.markdown(
    """
    <div class="ai-panel">
        <div class="ai-title">✦ Ask your business data</div>
        <div class="ai-description">
            Ask questions naturally. The AI will understand your request,
            generate the required analysis, and return actionable results.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

query = st.text_input(
    "Business question",
    placeholder="e.g. Which region generated the highest profit?",
    label_visibility="collapsed",
)

analyze_clicked = st.button(
    "✦  Analyze Business Question",
    type="primary",
    use_container_width=True,
)


# ---------------------------------------------------------
# KPI CARDS
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Business Overview</div>',
    unsafe_allow_html=True,
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">TOTAL ORDERS</div>
            <div class="kpi-value">12,000</div>
            <div class="kpi-meta">Across all regions</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi2:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">CUSTOMERS</div>
            <div class="kpi-value">750</div>
            <div class="kpi-meta">Active customer records</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi3:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">PRODUCTS</div>
            <div class="kpi-value">140</div>
            <div class="kpi-meta">Across product categories</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi4:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">ORDER ITEMS</div>
            <div class="kpi-value">22.8K</div>
            <div class="kpi-meta">Transaction line items</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# DEMO CHART
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Regional Profit Performance</div>',
    unsafe_allow_html=True,
)

chart_col, ranking_col = st.columns([2.2, 1])

regions = ["East", "South", "North", "West"]
profits = [
    6551101.40,
    6220000.00,
    6100000.00,
    5882957.71,
]

figure = go.Figure()

figure.add_trace(
    go.Bar(
        x=regions,
        y=profits,
        text=[
            f"₹{value / 1_000_000:.2f}M"
            for value in profits
        ],
        textposition="outside",
    )
)

figure.update_layout(
    height=390,
    margin=dict(l=10, r=10, t=25, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#cbd5e1"),
    xaxis=dict(
        title="Region",
        gridcolor="rgba(255,255,255,0.05)",
    ),
    yaxis=dict(
        title="Profit",
        gridcolor="rgba(255,255,255,0.05)",
    ),
)

with chart_col:
    st.plotly_chart(
        figure,
        use_container_width=True,
        config={"displayModeBar": False},
    )

with ranking_col:

    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-heading">
                TOP PERFORMER
            </div>
            <div class="insight-text">
                <strong>East</strong><br>
                ₹6.55M total profit
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-heading">
                NEEDS ATTENTION
            </div>
            <div class="insight-text">
                <strong>West</strong><br>
                ₹5.88M total profit
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# AI INSIGHTS
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">✦ AI Insights</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="insight-card">
        <div class="insight-heading">INSIGHT 01</div>
        <div class="insight-text">
            East is currently the strongest region based on total
            profit performance.
        </div>
    </div>

    <div class="insight-card">
        <div class="insight-heading">INSIGHT 02</div>
        <div class="insight-text">
            West has the lowest regional profit and may require
            further investigation into its underlying business drivers.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# STRATEGIC RECOMMENDATIONS
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">✦ Strategic Recommendations</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="recommendation-card">
        <div class="recommendation-heading">
            RECOMMENDATION 01
        </div>
        <div class="recommendation-text">
            Consider increasing investment in the highest-performing
            region to sustain growth.
        </div>
    </div>

    <div class="recommendation-card">
        <div class="recommendation-heading">
            RECOMMENDATION 02
        </div>
        <div class="recommendation-text">
            Investigate the lowest-performing region and identify
            targeted corrective actions.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# CURRENT PAGE MESSAGE
# ---------------------------------------------------------

if analyze_clicked:

    if not query.strip():

        st.warning(
            "Please enter a business question."
        )

    else:

        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/analyze",
                json={
                    "query": query
                },
                timeout=30,
            )

            if response.status_code == 200:

                result = response.json()

                st.session_state["analysis_result"] = result

                st.success(
                    "Analysis completed successfully."
                )
                st.markdown(
                    '<div class="section-title">✦ Analysis Result</div>',
                    unsafe_allow_html=True,
                )

                st.write(
                    f"**Question:** {result['query']}"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Region",
                        result["data"][0]["region"]
                    )

                with col2:
                    st.metric(
                        "Total Profit",
                        f"₹{result['data'][0]['total_profit']:,.2f}"
                    )

                st.markdown(
                    '<div class="section-title">Generated SQL</div>',
                    unsafe_allow_html=True,
                )

                st.code(
                    result["sql"],
                    language="sql",
                )

                st.markdown(
                '<div class="section-title">✦ Visual Analysis</div>',
                unsafe_allow_html=True,
            )

            chart_data = result["data"]

            if chart_data:

                regions = [
                    row["region"]
                    for row in chart_data
                ]

                profits = [
                    row["total_profit"]
                    for row in chart_data
                ]

                figure = go.Figure()

                figure.add_trace(
                    go.Bar(
                        x=regions,
                        y=profits,
                        text=[
                            f"₹{value:,.2f}"
                            for value in profits
                        ],
                        textposition="outside",
                        hovertemplate=(
                            "<b>%{x}</b><br>"
                            "Profit: ₹%{y:,.2f}"
                            "<extra></extra>"
                        ),
                    )
                )

                figure.update_layout(
                    height=420,
                    margin=dict(
                        l=10,
                        r=10,
                        t=30,
                        b=10,
                    ),
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(
                        color="#cbd5e1",
                    ),
                    xaxis=dict(
                        title="Region",
                        gridcolor="rgba(255,255,255,0.04)",
                    ),
                    yaxis=dict(
                        title="Total Profit",
                        gridcolor="rgba(255,255,255,0.04)",
                    ),
                )

                st.plotly_chart(
                    figure,
                    use_container_width=True,
                    config={
                        "displayModeBar": False,
                    },
                )

                st.markdown(
                    '<div class="section-title">Query Result</div>',
                    unsafe_allow_html=True,
                )

                st.dataframe(
                    chart_data,
                    use_container_width=True,
                    hide_index=True,
                )

            else:

                st.error(
                    f"Backend error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to FastAPI. "
                "Make sure the backend server is running."
            )

        except requests.exceptions.RequestException as error:

            st.error(
                f"Request failed: {error}"
            )