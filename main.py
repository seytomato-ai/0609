import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 탐험관 ✨",
    page_icon="🚀",
    layout="wide"
)

# ------------------------------
# 스타일
# ------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom, #f8f9ff, #eef4ff);
}

.title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    background: linear-gradient(90deg,#ff6ec4,#7873f5,#42e695);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle {
    text-align:center;
    font-size:22px;
    color:#555;
}

.job-card {
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom:15px;
}

.big-font {
    font-size:24px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# MBTI 데이터
# ------------------------------
mbti_jobs = {
    "INTJ": {
        "emoji":"🧠",
        "jobs":["데이터 과학자", "AI 연구원", "전략 컨설턴트", "대학교수", "건축가"],
        "desc":"논리적이고 미래를 계획하는 능력이 뛰어납니다."
    },
    "INTP": {
        "emoji":"🔬",
        "jobs":["과학자", "프로그래머", "수학자", "연구원", "발명가"],
        "desc":"호기심이 많고 문제 해결을 즐깁니다."
    },
    "ENTJ": {
        "emoji":"👑",
        "jobs":["CEO", "변호사", "경영 컨설턴트", "프로젝트 매니저", "정치인"],
        "desc":"리더십과 추진력이 뛰어납니다."
    },
    "ENTP": {
        "emoji":"💡",
        "jobs":["창업가", "마케팅 전문가", "광고기획자", "PD", "기획자"],
        "desc":"새로운 아이디어를 만드는 것을 좋아합니다."
    },
    "INFJ": {
        "emoji":"🌟",
        "jobs":["상담교사", "심리상담사", "작가", "사회복지사", "교육연구원"],
        "desc":"타인의 성장과 의미 있는 일을 중요하게 생각합니다."
    },
    "INFP": {
        "emoji":"🎨",
        "jobs":["작가", "디자이너", "일러스트레이터", "상담사", "음악가"],
        "desc":"창의성과 공감 능력이 뛰어납니다."
    },
    "ENFJ": {
        "emoji":"🤝",
        "jobs":["교사", "교육컨설턴트", "HR 전문가", "강사", "상담사"],
        "desc":"사람을 이끌고 성장시키는 능력이 있습니다."
    },
    "ENFP": {
        "emoji":"🎉",
        "jobs":["유튜버", "광고기획자", "방송작가", "기자", "크리에이터"],
        "desc":"열정적이고 창의적인 아이디어가 많습니다."
    },
    "ISTJ": {
        "emoji":"📋",
        "jobs":["공무원", "회계사", "경찰관", "품질관리자", "은행원"],
        "desc":"책임감과 신뢰성이 강합니다."
    },
    "ISFJ": {
        "emoji":"💖",
        "jobs":["간호사", "초등교사", "사회복지사", "행정직", "보건교사"],
        "desc":"배려심이 깊고 성실합니다."
    },
    "ESTJ": {
        "emoji":"🏆",
        "jobs":["군인", "행정가", "경영자", "공무원", "프로젝트 관리자"],
        "desc":"체계적이고 조직 운영 능력이 뛰어납니다."
    },
    "ESFJ": {
        "emoji":"😊",
        "jobs":["교사", "간호사", "승무원", "서비스 매니저", "상담사"],
        "desc":"사람들과 협력하는 것을 좋아합니다."
    },
    "ISTP": {
        "emoji":"🔧",
        "jobs":["엔지니어", "정비사", "파일럿", "소방관", "드론전문가"],
        "desc":"실용적이고 문제 해결 능력이 뛰어납니다."
    },
    "ISFP": {
        "emoji":"🌈",
        "jobs":["사진작가", "디자이너", "플로리스트", "음악가", "패션디자이너"],
        "desc":"예술적 감각이 풍부합니다."
    },
    "ESTP": {
        "emoji":"⚡",
        "jobs":["영업전문가", "기업가", "스포츠선수", "경찰관", "방송인"],
        "desc":"도전과 활동을 즐깁니다."
    },
    "ESFP": {
        "emoji":"🎤",
        "jobs":["배우", "가수", "방송인", "이벤트기획자", "유튜버"],
        "desc":"에너지가 넘치고 사람들과 어울리는 것을 좋아합니다."
    }
}

# ------------------------------
# 화면
# ------------------------------
st.markdown("<div class='title'>🚀 MBTI 진로 탐험관 🚀</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>✨ 나의 MBTI로 알아보는 미래 직업 추천 ✨</div>",
    unsafe_allow_html=True
)

st.balloons()

st.write("")
st.write("### 🎯 MBTI를 선택해보세요!")

selected_mbti = st.selectbox(
    "👇 MBTI 선택",
    list(mbti_jobs.keys())
)

info = mbti_jobs[selected_mbti]

st.markdown("---")

col1, col2 = st.columns([1,2])

with col1:
    st.markdown(
        f"""
        <div style='text-align:center'>
        <h1>{info['emoji']}</h1>
        <h2>{selected_mbti}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.success(f"✨ {info['desc']}")

st.markdown("## 🌟 추천 직업 TOP 5")

for job in info["jobs"]:
    st.markdown(
        f"""
        <div class='job-card'>
        <span class='big-font'>💼 {job}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown("""
### 📚 참고사항
💡 MBTI는 진로 탐색의 참고 자료일 뿐입니다.

🌱 자신의 흥미, 적성, 가치관을 함께 고려하여 진로를 선택해 보세요!

🚀 미래의 꿈을 향해 도전하세요!
""")

st.snow()
