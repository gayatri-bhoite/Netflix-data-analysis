import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Netflix Data Analysis",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# DASHBOARD THEME
# =========================================================

st.markdown("""
<style>

/* =====================================================
   MAIN DASHBOARD
   ===================================================== */

.stApp {
    background-color: #000000;
    color: white;
}

[data-testid="stAppViewContainer"] {
    background-color: #000000;
}

[data-testid="stHeader"] {
    background-color: #000000;
}


/* =====================================================
   SIDEBAR
   ===================================================== */

[data-testid="stSidebar"] {
    background-color: #151515 !important;
    border-right: none !important;
}

[data-testid="stSidebar"] > div:first-child {
    background-color: #151515 !important;
}

[data-testid="stSidebarContent"] {
    background-color: #151515 !important;
    padding-top: 0.8rem !important;
}

[data-testid="stSidebar"] label {
    color: #ffffff !important;
}

[data-testid="stSidebar"] p {
    color: #ffffff !important;
}

[data-testid="stSidebar"] span {
    color: #ffffff !important;
}


/* =====================================================
   SIDEBAR HEADINGS
   ===================================================== */

[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
    margin-top: 0.2rem !important;
    margin-bottom: 0.5rem !important;
}


/* =====================================================
   FILE UPLOADER
   ===================================================== */

[data-testid="stFileUploader"] {
    background-color: #1c1c1c !important;
    border: 1px solid #333333 !important;
    border-radius: 8px !important;
    padding: 8px !important;
}

[data-testid="stFileUploader"] section {
    background-color: #181818 !important;
    border: 1px dashed #555555 !important;
    border-radius: 7px !important;
}

[data-testid="stFileUploader"] button {
    background-color: #E50914 !important;
    color: white !important;
    border: none !important;
}


/* =====================================================
   SIDEBAR DIVIDER
   ===================================================== */

[data-testid="stSidebar"] hr {
    border: none !important;
    border-top: 1px solid #333333 !important;
    margin-top: 8px !important;
    margin-bottom: 8px !important;
}


/* =====================================================
   MULTISELECT
   ===================================================== */

[data-testid="stMultiSelect"] {
    background-color: #1b1b1b !important;
    border-radius: 8px !important;
}

[data-testid="stMultiSelect"] > div {
    background-color: #1b1b1b !important;
}

[data-testid="stMultiSelect"] div[data-baseweb="select"] {
    background-color: #101010 !important;
}

[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
    background-color: #101010 !important;
    border: 1px solid #3a3a3a !important;
    border-radius: 7px !important;
}

[data-testid="stMultiSelect"] div {
    background-color: #101010 !important;
}

[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    background-color: #E50914 !important;
    color: white !important;
    border-radius: 5px !important;
}

[data-testid="stMultiSelect"] [data-baseweb="tag"] span {
    background-color: #E50914 !important;
    color: white !important;
}

[data-testid="stMultiSelect"] input {
    background-color: #101010 !important;
    color: white !important;
}

[data-testid="stMultiSelect"] svg {
    color: white !important;
    fill: white !important;
}


/* =====================================================
   DROPDOWN
   ===================================================== */

[data-baseweb="popover"] {
    background-color: #101010 !important;
}

[data-baseweb="popover"] > div {
    background-color: #101010 !important;
}

[data-baseweb="menu"] {
    background-color: #101010 !important;
}

[data-baseweb="menu"] li {
    background-color: #101010 !important;
    color: white !important;
}

[data-baseweb="menu"] li:hover {
    background-color: #252525 !important;
}


/* =====================================================
   DASHBOARD HEADER
   ===================================================== */

.dashboard-title {
    font-size: 32px;
    font-weight: 700;
    color: white !important;
    margin-top: -10px;
    margin-bottom: 2px;
    text-align: center;
}

.dashboard-subtitle {
    color: #999999 !important;
    font-size: 14px;
    margin-bottom: 15px;
    text-align: center;
}

.red-line {
    width: 100%;
    height: 2px;
    margin-top: 5px;
    margin-bottom: 8px;

    background: linear-gradient(
        to right,
        transparent,
        #E50914 20%,
        #E50914 80%,
        transparent
    );
}


/* =====================================================
   METRIC CARDS
   ===================================================== */

div[data-testid="stMetric"] {
    background-color: #111111 !important;
    border: 1px solid #292929 !important;
    border-left: 3px solid #E50914 !important;
    border-radius: 9px !important;
    padding: 13px !important;
}

div[data-testid="stMetricLabel"] {
    color: #aaaaaa !important;
    font-size: 13px !important;
}

div[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 25px !important;
}


/* =====================================================
   CHART CARDS
   ===================================================== */

.chart-card {
    background-color: #0d0d0d;
    border: 1px solid #292929;
    border-radius: 10px;
    padding: 8px 10px 4px 10px;
    margin-bottom: 15px;
}


/* =====================================================
   SECTION HEADINGS
   ===================================================== */

h1,
h2,
h3 {
    color: white !important;
}


/* =====================================================
   EXPANDER
   ===================================================== */

[data-testid="stExpander"] {
    background-color: #0d0d0d !important;
    border: 1px solid #292929 !important;
    border-radius: 8px !important;
}


/* =====================================================
   FOOTER
   ===================================================== */

.dashboard-footer {
    text-align: center;
    color: #666666 !important;
    font-size: 13px;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    "### 📤 Upload Netflix CSV"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV file",
    type=["csv"]
)


# =========================================================
# LOAD DATA
# =========================================================

if uploaded_file is not None:

    netflix = pd.read_csv(uploaded_file)
    source_name = uploaded_file.name

else:

    netflix = pd.read_csv("netflix.csv")
    source_name = "netflix.csv"


# =========================================================
# SOURCE INFORMATION
# =========================================================

st.sidebar.markdown(
    f"""
    <div style="
        background:#1c1c1c;
        border:1px solid #303030;
        border-radius:7px;
        padding:8px 10px;
        margin-top:5px;
        margin-bottom:10px;
        color:#999999;
        font-size:12px;
    ">
        📁 {source_name}<br>
        📊 {len(netflix)} rows
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DATA CLEANING
# =========================================================

netflix["Watch_Date"] = pd.to_datetime(
    netflix["Watch_Date"]
)

netflix["month"] = netflix[
    "Watch_Date"
].dt.month_name()


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="
        background:#1c1c1c;
        border-left:3px solid #E50914;
        border-radius:6px;
        padding:7px 10px;
        margin-bottom:8px;
        color:white;
        font-size:16px;
        font-weight:600;
    ">
        🔎 Filters
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# REGION FILTER
# =========================================================

regions = sorted(
    netflix["Region"]
    .dropna()
    .unique()
    .tolist()
)

selected_regions = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions
)


# =========================================================
# SUBSCRIPTION PLAN FILTER
# =========================================================

plans = sorted(
    netflix["Subscription_Plan"]
    .dropna()
    .unique()
    .tolist()
)

selected_plans = st.sidebar.multiselect(
    "Subscription Plan",
    plans,
    default=plans
)


# =========================================================
# FILTER DATA
# =========================================================

filtered_data = netflix[
    (netflix["Region"].isin(selected_regions))
    &
    (
        netflix["Subscription_Plan"]
        .isin(selected_plans)
    )
].copy()


# =========================================================
# DASHBOARD HEADER
# =========================================================

logo_col, title_col, banner_col = st.columns([2, 7, 3])

with logo_col:

    st.image(
        "image/netflix_logo.png",
        width=150
    )

with title_col:

    st.markdown(
        """
        <div class="dashboard-title">
            <span>Netflix</span> Data Analysis Dashboard
        </div>

        <div class="red-line"></div>

        <div class="dashboard-subtitle">
            Customer • Revenue • Viewing • Subscription Analysis
        </div>
        """,
        unsafe_allow_html=True
    )


with banner_col:

    st.image(
        "image/netflix_banner.jpg",
        width=200
    )


st.markdown("---")
# =========================================================
# KEY METRICS
# =========================================================

st.markdown("### 📊 Key Metrics")


total_customers = filtered_data[
    "Customer_ID"
].nunique()


total_revenue = filtered_data[
    "Monthly_Revenue"
].sum()


total_watch_count = filtered_data[
    "Watch_Count"
].sum()


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )


with col2:

    st.metric(
        "💰 Total Revenue",
        f"₹{total_revenue:,.0f}"
    )


with col3:

    st.metric(
        "▶️ Total Watch Count",
        f"{total_watch_count:,}"
    )


# =========================================================
# MATPLOTLIB DARK SETTINGS
# =========================================================

plt.rcParams["figure.facecolor"] = "#0d0d0d"
plt.rcParams["axes.facecolor"] = "#0d0d0d"
plt.rcParams["axes.edgecolor"] = "#444444"
plt.rcParams["axes.labelcolor"] = "white"
plt.rcParams["xtick.color"] = "white"
plt.rcParams["ytick.color"] = "white"
plt.rcParams["text.color"] = "white"


# =========================================================
# COMMON CHART SETTINGS
# =========================================================

CHART_SIZE = (5,4)

LABEL_SIZE = 10
TICK_SIZE = 9
PIE_TEXT_SIZE = 9


# =========================================================
# MONTH ORDER
# =========================================================

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# =========================================================
# ROW 1
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# 1. MONTH WISE REVENUE
# =========================================================

with col1:

    st.markdown(
        '<div class="chart-card">',
        unsafe_allow_html=True
    )

    st.subheader("Month Wise Revenue")

    month_revenue = (
        filtered_data
        .groupby("month")["Monthly_Revenue"]
        .sum()
        .reindex(month_order)
        .dropna()
    )

    fig, ax = plt.subplots(
        figsize=CHART_SIZE
    )

    month_revenue.plot(
        kind="bar",
        ax=ax,
        color="#E50914"
    )

    ax.set_xlabel(
        "Month",
        fontsize=LABEL_SIZE
    )

    ax.set_ylabel(
        "Monthly Revenue",
        fontsize=LABEL_SIZE
    )

    ax.tick_params(
        axis="both",
        labelsize=TICK_SIZE
    )

    ax.grid(
        axis="y",
        alpha=0.15,
        linewidth=0.7
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 2. REGION WISE RATING
# =========================================================

with col2:

    st.markdown(
        '<div class="chart-card">',
        unsafe_allow_html=True
    )

    st.subheader("Region Wise Rating")

    region_rating = (
        filtered_data
        .groupby("Region")["Rating"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=CHART_SIZE
    )

    region_rating.plot(
        kind="pie",
        ax=ax,
        autopct="%1.1f%%",
        textprops={
            "fontsize": PIE_TEXT_SIZE,
            "color": "white"
        },
        labeldistance=1.10
    )

    ax.set_ylabel("")

    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# ROW 2
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# 3. DEVICE WISE REVENUE
# =========================================================

with col1:

    st.markdown(
        '<div class="chart-card">',
        unsafe_allow_html=True
    )

    st.subheader("Device Wise Revenue")

    device_revenue = (
        filtered_data
        .groupby("Device")["Monthly_Revenue"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=CHART_SIZE
    )

    device_revenue.plot(
        kind="line",
        marker="o",
        linewidth=2,
        markersize=6,
        ax=ax,
        color="#E50914"
    )

    ax.set_xlabel(
        "Device",
        fontsize=LABEL_SIZE
    )

    ax.set_ylabel(
        "Monthly Revenue",
        fontsize=LABEL_SIZE
    )

    ax.tick_params(
        axis="both",
        labelsize=TICK_SIZE
    )

    ax.grid(
        axis="y",
        alpha=0.15,
        linewidth=0.7
    )


    # Revenue values

    for x, value in enumerate(device_revenue):

        ax.text(
            x,
            value + device_revenue.max() * 0.03,
            f"₹{value:,.0f}",
            ha="center",
            va="bottom",
            color="white",
            fontsize=8,
            fontweight="bold"
        )


    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 4. TOTAL RATING
# =========================================================

with col2:

    st.markdown(
        '<div class="chart-card">',
        unsafe_allow_html=True
    )

    st.subheader("Total Rating")

    rating_count = (
        filtered_data["Rating"]
        .value_counts()
        .sort_index()
    )

    fig, ax = plt.subplots(
        figsize=CHART_SIZE
    )

    rating_count.plot(
        kind="bar",
        ax=ax,
        color="#E50914"
    )

    ax.set_xlabel(
        "Rating",
        fontsize=LABEL_SIZE
    )

    ax.set_ylabel(
        "Count",
        fontsize=LABEL_SIZE
    )

    ax.tick_params(
        axis="both",
        labelsize=TICK_SIZE
    )

    ax.grid(
        axis="y",
        alpha=0.15,
        linewidth=0.7
    )

    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# ROW 3
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# 5. REGION WISE REVENUE
# =========================================================

with col1:

    st.markdown(
        '<div class="chart-card">',
        unsafe_allow_html=True
    )

    st.subheader("Region Wise Revenue")

    region_revenue = (
        filtered_data
        .groupby("Region")["Monthly_Revenue"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=CHART_SIZE
    )

    bars = region_revenue.plot(
        kind="bar",
        ax=ax,
        color="#E50914"
    )

    ax.set_xlabel(
        "Region",
        fontsize=LABEL_SIZE
    )

    ax.set_ylabel(
        "Monthly Revenue",
        fontsize=LABEL_SIZE
    )

    ax.tick_params(
        axis="both",
        labelsize=TICK_SIZE
    )

    ax.grid(
        axis="y",
        alpha=0.15,
        linewidth=0.7
    )


    # Extra space above bars

    ax.set_ylim(
        0,
        region_revenue.max() * 1.15
    )


    total_region_revenue = (
        region_revenue.sum()
    )


    if total_region_revenue > 0:

        for bar in bars.patches:

            value = bar.get_height()

            percentage = (
                value
                / total_region_revenue
                * 100
            )


            # Revenue value

            ax.text(
                bar.get_x()
                + bar.get_width() / 2,
                value
                + region_revenue.max() * 0.025,
                f"₹{value:,.0f}",
                ha="center",
                va="bottom",
                color="white",
                fontsize=8,
                fontweight="bold"
            )


            # Percentage

            ax.text(
                bar.get_x()
                + bar.get_width() / 2,
                value
                + region_revenue.max() * 0.065,
                f"{percentage:.1f}%",
                ha="center",
                va="bottom",
                color="#E50914",
                fontsize=9,
                fontweight="bold"
            )


    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 6. SUBSCRIPTION PLAN WISE WATCH COUNT
# =========================================================

with col2:

    st.markdown(
        '<div class="chart-card">',
        unsafe_allow_html=True
    )

    st.subheader(
        "Subscription Plan Wise Watch Count"
    )

    subscription_watch = (
        filtered_data
        .groupby(
            "Subscription_Plan"
        )["Watch_Count"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=CHART_SIZE
    )

    subscription_watch.plot(
        kind="pie",
        ax=ax,
        autopct="%1.1f%%",
        textprops={
            "fontsize": PIE_TEXT_SIZE,
            "color": "white"
        },
        labeldistance=1.05
    )

    ax.set_ylabel("")

    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# VIEW DATASET
# =========================================================

st.markdown("---")

with st.expander(
    "📋 View Netflix Dataset"
):

    st.dataframe(
        filtered_data,
        use_container_width=True
    )


