import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title="🌎 Global Market Cap TOP10 Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("🌎 글로벌 시가총액 TOP10 주식 대시보드")
st.markdown("### 🚀 Yahoo Finance 실시간 데이터 기반")

# 시가총액 상위 기업 티커
stocks = {
    "NVIDIA": "NVDA",
    "Apple": "AAPL",
    "Alphabet": "GOOGL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "TSMC": "TSM",
    "Saudi Aramco": "2222.SR",
    "Meta": "META",
    "Broadcom": "AVGO",
    "Tesla": "TSLA"
}

@st.cache_data(ttl=3600)
def load_data():
    end = datetime.today()
    start = end - timedelta(days=365)

    data = pd.DataFrame()

    for company, ticker in stocks.items():
        try:
            df = yf.download(
                ticker,
                start=start,
                end=end,
                auto_adjust=True,
                progress=False
            )

            data[company] = df["Close"]

        except:
            pass

    return data

price_data = load_data()

if price_data.empty:
    st.error("데이터를 불러오지 못했습니다.")
    st.stop()

# ---------------------------
# 최근 가격
# ---------------------------

st.subheader("📊 현재 주가 현황")

latest = price_data.iloc[-1]

col1, col2, col3, col4, col5 = st.columns(5)

for i, (name, price) in enumerate(latest.items()):
    cols = [col1, col2, col3, col4, col5]
    cols[i % 5].metric(
        name,
        f"${price:,.2f}"
    )

# ---------------------------
# 정규화
# ---------------------------

normalized = price_data / price_data.iloc[0] * 100

st.subheader("📈 최근 1년 수익률 비교")

fig = px.line(
    normalized,
    x=normalized.index,
    y=normalized.columns,
    template="plotly_dark"
)

fig.update_layout(
    height=650,
    legend_title="기업",
    xaxis_title="날짜",
    yaxis_title="100 기준 수익률"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# 개별 종목
# ---------------------------

st.subheader("🔍 개별 종목 분석")

selected = st.selectbox(
    "기업 선택",
    list(stocks.keys())
)

single = pd.DataFrame({
    "Date": price_data.index,
    "Price": price_data[selected]
})

fig2 = px.area(
    single,
    x="Date",
    y="Price",
    template="plotly_dark",
    title=f"{selected} 최근 1년 주가"
)

fig2.update_layout(height=500)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# 수익률 랭킹
# ---------------------------

st.subheader("🏆 최근 1년 수익률 순위")

returns = (
    (price_data.iloc[-1] / price_data.iloc[0] - 1) * 100
).sort_values(ascending=False)

rank_df = pd.DataFrame({
    "기업": returns.index,
    "수익률(%)": returns.values.round(2)
})

st.dataframe(
    rank_df,
    use_container_width=True,
    hide_index=True
)

# ---------------------------
# 막대그래프
# ---------------------------

fig3 = px.bar(
    rank_df,
    x="기업",
    y="수익률(%)",
    title="최근 1년 수익률",
    text="수익률(%)",
    template="plotly_dark"
)

fig3.update_layout(height=500)

st.plotly_chart(fig3, use_container_width=True)

st.caption("📌 데이터 출처 : Yahoo Finance")
