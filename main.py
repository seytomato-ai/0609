import streamlit as st
import random

st.set_page_config(
    page_title="🍿 OTT 취향 분석기",
    page_icon="🎬",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.block-container{
    padding-top:2rem;
}

.big-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:#E50914;
}

.sub-title{
    text-align:center;
    color:#BBBBBB;
    font-size:20px;
    margin-bottom:30px;
}

.drama-card{
    background:#1C1F26;
    border-radius:20px;
    padding:25px;
    margin-bottom:20px;
    border-left:8px solid #E50914;
    box-shadow:0px 0px 15px rgba(229,9,20,0.2);
}

.drama-title{
    font-size:28px;
    color:white;
    font-weight:bold;
}

.drama-story{
    color:#d6d6d6;
    line-height:1.8;
}

.analysis{
    background:#141821;
    padding:20px;
    border-radius:15px;
    color:white;
    font-size:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# 제목
# ==========================

st.markdown(
    "<div class='big-title'>🍿 OTT DRAMA PICKER 🎬</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>✨ 당신의 취향을 분석해서 드라마를 추천해드립니다 ✨</div>",
    unsafe_allow_html=True
)

# ==========================
# 데이터
# ==========================

dramas = {

"💘 로맨스":[
{
"title":"폭싹 속았수다",
"story":"제주를 배경으로 꿈과 사랑, 가족의 이야기를 담은 따뜻한 성장 드라마",
"reason":"감성적인 이야기와 아름다운 여운"
},
{
"title":"선재 업고 튀어",
"story":"과거로 돌아가 사랑하는 사람의 운명을 바꾸려는 타임슬립 로맨스",
"reason":"설렘과 웃음이 공존"
}
],

"😱 스릴러":[
{
"title":"악연",
"story":"서로 얽힌 인물들이 예기치 못한 사건에 휘말리며 벌어지는 범죄 스릴러",
"reason":"긴장감 있는 전개"
},
{
"title":"트리거",
"story":"연쇄 사건의 진실을 추적하는 과정에서 밝혀지는 충격적인 비밀",
"reason":"몰입도 최고"
}
],

"⚔️ 액션":[
{
"title":"무빙",
"story":"초능력을 가진 부모와 아이들이 거대한 위협에 맞서는 이야기",
"reason":"액션과 감동을 모두 갖춤"
},
{
"title":"카지노",
"story":"카지노 제국을 일군 한 남자의 성공과 몰락",
"reason":"강렬한 캐릭터"
}
],

"😂 코미디":[
{
"title":"닥터 차정숙",
"story":"평범한 가정주부가 다시 의사에 도전하며 벌어지는 이야기",
"reason":"유쾌하면서도 감동적"
}
],

"🧟 판타지":[
{
"title":"경성크리처",
"story":"1945년 경성을 배경으로 괴생명체와 맞서는 사람들의 이야기",
"reason":"독특한 세계관"
}
],

"🔍 추리":[
{
"title":"시그널",
"story":"과거와 현재를 연결하는 무전기로 미제 사건을 해결하는 이야기",
"reason":"명작 수사물"
}
]
}

# ==========================
# 취향 선택
# ==========================

selected = st.multiselect(
    "🎭 좋아하는 취향을 모두 선택하세요",
    list(dramas.keys())
)

if selected:

    st.markdown("---")

    personality = " + ".join(selected)

    st.markdown(f"""
    <div class='analysis'>
    🤖 <b>취향 분석 결과</b><br><br>
    당신은 <span style="color:#E50914;"><b>{personality}</b></span>
    취향을 가진 시청자입니다! 🍿✨
    감정 몰입도가 높고 작품의 분위기를 중요하게 생각하는 편입니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎬 추천 작품")

    recommendations = []

    for genre in selected:
        recommendations.extend(dramas[genre])

    for drama in recommendations:

        st.markdown(f"""
        <div class='drama-card'>
            <div class='drama-title'>
            🎬 {drama['title']}
            </div>
            <br>
            <div class='drama-story'>
            📖 <b>줄거리</b><br>
            {drama['story']}
            <br><br>
            ⭐ <b>추천 이유</b><br>
            {drama['reason']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("🎲 오늘의 운명 드라마 뽑기"):

        pick = random.choice(recommendations)

        st.balloons()

        st.success(
            f"🎉 오늘의 운명 드라마는 '{pick['title']}' 입니다!"
        )

else:

    st.info("👆 먼저 취향을 선택해 주세요!")
