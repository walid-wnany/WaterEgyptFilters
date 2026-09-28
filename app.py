import streamlit as st

LOGO = "assets/logo.png"

st.set_page_config(
    page_title="المصرية للفلاتر | فلاتر مياه وتركيب وصيانة",
    page_icon=LOGO,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stSidebar"], [data-testid="stHeader"] {
        direction: rtl !important;
        font-family: Cairo, Tahoma, Arial, sans-serif !important;
    }
    .stApp { background:#f5fbff; }
    [data-testid="stSidebar"] { border-left:1px solid #dceef7; border-right:0; }
    [data-testid="stSidebar"] * { text-align:right !important; }
    [data-testid="stSidebarNav"], [data-testid="stSidebarNav"] ul, [data-testid="stSidebarNav"] a { direction:rtl !important; }
    [data-testid="stSidebarNav"] ul { padding-right:0 !important; }
    [data-testid="stMain"], .stHorizontalBlock, [data-testid="column"] { direction:rtl !important; }
    .stMarkdown, .stText, .stCaption, .stSelectbox, .stMultiSelect, .stTextInput, .stNumberInput, .stTextArea, .stRadio, .stCheckbox, .stButton, .stLinkButton { direction:rtl !important; }
    button, [role="button"], input, textarea, select { direction:rtl !important; }
    input, textarea { text-align:right !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

home = st.Page("home.py", title="المصرية للفلاتر", icon="🏠", default=True)
areas = st.Page("pages/areas.py", title="المناطق المخدومة", icon="🗺️", url_path="service-areas")
cairo = st.Page("pages/cairo.py", title="فلاتر مياه في القاهرة", icon="📍", url_path="water-filters-cairo")
giza = st.Page("pages/giza.py", title="فلاتر مياه في الجيزة", icon="📍", url_path="water-filters-giza")
qalyubia = st.Page("pages/qalyubia.py", title="فلاتر مياه في القليوبية", icon="📍", url_path="water-filters-qalyubia")
installation = st.Page("pages/installation.py", title="تركيب فلاتر المياه", icon="🔧", url_path="water-filter-installation")
maintenance = st.Page("pages/maintenance.py", title="صيانة فلاتر المياه", icon="🛠️", url_path="water-filter-maintenance")
cartridges = st.Page("pages/cartridges.py", title="تغيير شمعات الفلاتر", icon="💧", url_path="filter-cartridge-change")
spare_parts = st.Page("pages/spare_parts.py", title="قطع غيار فلاتر المياه", icon="🔩", url_path="filter-spare-parts")

pages = {
    "الرئيسية": [home],
    "المناطق": [areas, cairo, giza, qalyubia],
    "الخدمات": [installation, maintenance, cartridges, spare_parts],
}

st.session_state["_navigation_pages"] = {
    "home": home,
    "areas": areas,
    "cairo": cairo,
    "giza": giza,
    "qalyubia": qalyubia,
    "installation": installation,
    "maintenance": maintenance,
    "cartridges": cartridges,
    "spare_parts": spare_parts,
}

pg = st.navigation(pages, position="sidebar")
pg.run()
