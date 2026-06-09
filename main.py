import streamlit as st

st.set_page_config(
    page_title="OTT Drama Picker",
    page_icon="🎬",
    layout="wide"
)

# ------------------------
# CSS
# ------------------------

st.markdown("""
<style>

.main {
    background-color:#0e1117;
}

.title {
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#ff4b4b;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:30px;
}

.card{
    background:#1a1d24;
    border-radius:20px;
    padding:15px;
    text-align:center;
    transition:0.3s;
    margin-bottom:20px;
}

.card:hover{
    transform:scale(1.05);
}

.poster{
    border-radius:15px;
    width:100%;
}

.name{
    color:white;
    font-size:24px;
    font-weight:bold;
}

.desc{
    color:#cfcfcf;
}

</style>
""", unsafe_allow_html=True)

# ------------------------
# 데이터
# ------------------------

dramas = {

"💘 로맨스":[

{
"name":"폭싹 속았수다",
"img":"https://images.unsplash.com/photo-1517602302552-471fe67acf66",
"desc":"제주를 배경으로 한 감성 로맨스"
},

{
"name":"선재 업고 튀어",
"img":"https://images.unsplash.com/photo-1489599849927-2ee91cede3ba",
"desc":"타임슬립 청춘 로맨스"
},

{
"name":"멋진 신세계",
"img":"https://images.unsplash.com/photo-1440404653325-ab127d49abc1",
"desc":"미래 사회 속 인간과 사랑 이야기"
}

],

"😱 스릴러":[

{
"name":"악연",
"img":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
"desc":"얽히고설킨 운명의 스릴러"
},

{
"name":"트리거",
"img":"https://images.unsplash.com/photo-1516035069371-29a1b244cc32",
"desc":"총기 사건을 둘러싼 긴장감"
}

],

"🧟 판타지":[

{
"name":"중증외상센터",
"img":"https://images.unsplash.com/photo-1505751172876-fa1923c5c528",
"desc":"영웅 같은 의사의 활약"
},

{
"name":"경성크리처",
"img":"https://images.unsplash.com/photo-1500534623283-312aade485b7",
"desc":"괴생명체와 맞서는 이야기"
}

],

"⚔️ 액션":[

{
"name":"무빙",
"img":"https://images.unsplash.com/photo-1518998053901-5348d3961a04",
"desc":"초능력 액션 드라마"
},

{
"name":"카지노",
"img":"https://images.unsplash.com/photo-1511512578047-dfb367046420",
"desc":"거대한 카지노 제국 이야기"
}

]
}

# ------------------------
# 화면
# ------------------------

st.markdown(
"<div class='title'>🍿 OTT DRAMA PICKER 🎬</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>✨ 오늘의 취향에 맞는 드라마를 찾아보세요 ✨</div>",
unsafe_allow_html=True
)

genre = st.selectbox(
"🎭 어떤 분위기를 원하시나요?",
list(dramas.keys())
)

st.markdown("---")

cols = st.columns(3)

for idx, drama in enumerate(dramas[genre]):

    with cols[idx % 3]:

        st.markdown(f"""
        <div class='card'>
            <img class='poster' src='{drama["img"]}'>
            <div class='name'>🎬 {drama["name"]}</div>
            <div class='desc'>{drama["desc"]}</div>
            <br>
            ⭐ 추천도 : 9.8
        </div>
        """,
        unsafe_allow_html=True)
