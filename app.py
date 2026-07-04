import streamlit as st
import joblib
import pandas as pd

# Load Trained Model
model = joblib.load("student_performance_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# Premium CSS
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#334155);
}

.main-title{
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #ffffff !important;
    text-shadow: 0px 0px 12px rgba(255,255,255,0.35);
    margin-bottom: 10px;
}
.sub-title{
    text-align:center;
    color:#cbd5e1 !important;
    font-size:18px;
    margin-bottom:30px;
}

.block-container{
    padding-top:2rem;
}

div[data-testid="stNumberInput"]{
    background:white;
    border-radius:12px;
    padding:10px;
}

div[data-testid="stSelectbox"]{
    background:white;
    border-radius:12px;
    padding:8px;
}

.stButton>button{
    width:100%;
    background:#2563eb;
    color:white;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    height:50px;
}

.stButton>button:hover{
    background:#1d4ed8;
}
            
.section-title{
    color:#ffffff !important;
    font-size:30px;
    font-weight:700;
    margin-top:35px;
    margin-bottom:30px;
    padding:10px 15px;
    background:rgba(255,255,255,0.08);
    border-radius:10px;
    border-left:5px solid #60a5fa;
}
            
label{
    color:white !important;
    font-weight:600;
}

div[data-testid="stSlider"] label{
    color:white !important;
}

div[data-testid="stNumberInput"] label{
    color:white !important;
}

div[data-testid="stSelectbox"] label{
    color:white !important;
}
            
div[data-testid="stNumberInput"] label p,
div[data-testid="stSelectbox"] label p{
    color: black !important;
    font-weight: 700 !important;
    font-size: 17px !important;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 class='main-title'>🎓 Student Performance Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Predict the student's final grade using Machine Learning.</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<h2 class='section-title'>👤 Personal Details</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=22,
        value=17
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    school = st.selectbox(
        "School",
        ["GP", "MS"]
    )

with col2:

    address = st.selectbox(
        "Address",
        ["Urban", "Rural"]
    )

    Medu = st.slider(
        "Mother's Education",
        0, 4, 2
    )

    Fedu = st.slider(
        "Father's Education",
        0, 4, 2
    )

# Sidebar
st.sidebar.title("📘 About Project")

st.sidebar.info("""
### Student Performance Prediction

**Model Used:** Linear Regression

**Dataset:** UCI Student Performance Dataset

**Developed Using:**
- Python
- Pandas
- Scikit-Learn
- Streamlit
""")

st.markdown(
    "<h2 class='section-title'>📚 Academic Details</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    studytime = st.slider(
        "Study Time",
        1, 4, 2
    )

    traveltime = st.slider(
        "Travel Time",
        1, 4, 1
    )

    failures = st.slider(
        "Previous Failures",
        0, 4, 0
    )

with col2:

    absences = st.number_input(
        "Absences",
        0, 100, 4
    )

    G1 = st.number_input(
        "First Period Grade (G1)",
        0, 20, 10
    )

    G2 = st.number_input(
        "Second Period Grade (G2)",
        0, 20, 10
    )

st.markdown(
    "<h2 class='section-title'>🏠 Family Details</h2>",
    unsafe_allow_html=True
)

famsize = st.selectbox(
    "Family Size",
    ["LE3", "GT3"]
)

Pstatus = st.selectbox(
    "Parents Living Together",
    ["A", "T"]
)

guardian = st.selectbox(
    "Guardian",
    ["Mother", "Father", "Other"]
)

famsup = st.selectbox(
    "Family Educational Support",
    ["No", "Yes"]
)

schoolsup = st.selectbox(
    "School Educational Support",
    ["No", "Yes"]
)

famrel = st.slider(
    "Family Relationship Quality",
    1,
    5,
    3
)

st.markdown(
    "<h2 class='section-title'>🎯 Lifestyle Details</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    freetime = st.slider(
        "Free Time",
        1,5,3
    )

    goout = st.slider(
        "Going Out with Friends",
        1,5,3
    )

    health = st.slider(
        "Health Status",
        1,5,3
    )

    activities = st.selectbox(
        "Extra Activities",
        ["No","Yes"]
    )

    Dalc = st.slider(
    "Workday Alcohol Consumption",
    1, 5, 1
)

    Walc = st.slider(
    "Weekend Alcohol Consumption",
    1, 5, 2
)

with col2:

    internet = st.selectbox(
        "Internet Access",
        ["No","Yes"]
    )

    higher = st.selectbox(
        "Higher Education",
        ["No","Yes"]
    )

    paid = st.selectbox(
        "Extra Paid Classes",
        ["No","Yes"]
    )

    nursery = st.selectbox(
        "Attended Nursery",
        ["No","Yes"]
    )

    romantic = st.selectbox(
        "In a Relationship",
        ["No","Yes"]
    )

st.markdown(
    "<h2 class='section-title'>👨‍👩‍👧 Parents' Occupation</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    Mjob = st.selectbox(
        "Mother's Job",
        ["at_home","health","other","services","teacher"]
    )

with col2:

    Fjob = st.selectbox(
        "Father's Job",
        ["at_home","health","other","services","teacher"]
    )

st.markdown(
    "<h2 class='section-title'>🏫 School Information</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    reason = st.selectbox(
        "Reason for Choosing School",
        ["course","home","other","reputation"]
    )

st.markdown("---")

predict = st.button("🎯 Predict Final Grade")   

if predict:

    # Binary Encoding
    sex_M = 1 if gender == "Male" else 0
    school_MS = 1 if school == "MS" else 0
    address_U = 1 if address == "Urban" else 0

    famsize_LE3 = 1 if famsize == "LE3" else 0
    Pstatus_T = 1 if Pstatus == "T" else 0

    guardian_mother = 1 if guardian == "Mother" else 0
    guardian_other = 1 if guardian == "Other" else 0

    schoolsup_yes = 1 if schoolsup == "Yes" else 0
    famsup_yes = 1 if famsup == "Yes" else 0
    paid_yes = 1 if paid == "Yes" else 0
    activities_yes = 1 if activities == "Yes" else 0
    nursery_yes = 1 if nursery == "Yes" else 0
    higher_yes = 1 if higher == "Yes" else 0
    internet_yes = 1 if internet == "Yes" else 0
    romantic_yes = 1 if romantic == "Yes" else 0

        # Mother's Job
    Mjob_health = 1 if Mjob == "health" else 0
    Mjob_other = 1 if Mjob == "other" else 0
    Mjob_services = 1 if Mjob == "services" else 0
    Mjob_teacher = 1 if Mjob == "teacher" else 0

    # Father's Job
    Fjob_health = 1 if Fjob == "health" else 0
    Fjob_other = 1 if Fjob == "other" else 0
    Fjob_services = 1 if Fjob == "services" else 0
    Fjob_teacher = 1 if Fjob == "teacher" else 0

    # Reason
    reason_home = 1 if reason == "home" else 0
    reason_other = 1 if reason == "other" else 0
    reason_reputation = 1 if reason == "reputation" else 0

    input_data = pd.DataFrame([{
        "age": age,
        "Medu": Medu,
        "Fedu": Fedu,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2,
        "school_MS": school_MS,
        "sex_M": sex_M,
        "address_U": address_U,
        "famsize_LE3": famsize_LE3,
        "Pstatus_T": Pstatus_T,
        "Mjob_health": Mjob_health,
        "Mjob_other": Mjob_other,
        "Mjob_services": Mjob_services,
        "Mjob_teacher": Mjob_teacher,
        "Fjob_health": Fjob_health,
        "Fjob_other": Fjob_other,
        "Fjob_services": Fjob_services,
        "Fjob_teacher": Fjob_teacher,
        "reason_home": reason_home,
        "reason_other": reason_other,
        "reason_reputation": reason_reputation,
        "guardian_mother": guardian_mother,
        "guardian_other": guardian_other,
        "schoolsup_yes": schoolsup_yes,
        "famsup_yes": famsup_yes,
        "paid_yes": paid_yes,
        "activities_yes": activities_yes,
        "nursery_yes": nursery_yes,
        "higher_yes": higher_yes,
        "internet_yes": internet_yes,
        "romantic_yes": romantic_yes
    }])

    # Prediction
    prediction = model.predict(input_data)

    predicted_grade = max(0, min(20, prediction[0]))

    # Display Result
    st.markdown("---")

    st.success(f"🎉 Predicted Final Grade: {predicted_grade:.2f} / 20")

    if predicted_grade >= 16:
        st.balloons()
        st.info("🌟 Excellent Performance!")

    elif predicted_grade >= 12:
        st.info("👍 Good Performance!")

    elif predicted_grade >= 8:
        st.warning("📚 Average Performance. More study can improve the score.")

    else:
        st.error("⚠️ Needs Improvement. Focus on studies and attendance.")

    st.markdown("---")

st.markdown("""
<div style="
    text-align:center;
    padding:18px;
    color:white;
    font-size:18px;
    font-weight:bold;
    background:linear-gradient(90deg,#1e293b,#334155);
    border-left:5px solid #60a5fa;
    border-radius:12px;
">
🚀 Developed by <span style="color:#60a5fa;">Bhakti Bagthariya 🐙</span>
<pre>               Powered by Python | Scikit-Learn | Streamlit</pre>
</div>
""", unsafe_allow_html=True)