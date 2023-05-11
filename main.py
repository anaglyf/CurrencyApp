import streamlit as st
import pandas as pd

currency_scale = [1, 100, 1000]
st.set_page_config(layout="wide")

df = pd.read_csv("currencies.csv")

st.title("""
"Easy" Currency Exchange Calculator!
""")
st.caption("Developed by Kotik Tech Solutions")

col1, col2 = st.columns(2)

with col1:
    currency_mult = st.selectbox("Rate per:", options=currency_scale, index=0)
    your_currency = st.selectbox("Choose Your Currency", df['currency'])
    desired_currency = st.selectbox("Choose Desired Currency", df['currency'], index=1)


with col2:
    money = st.text_input(f"Enter the amount of {your_currency} you want to convert")
    buy_price = st.text_input("Enter the buy price:", 0)
    sell_price = st.text_input("Enter the sell price:", 0)
    button = st.button("Submit")
    if buy_price and sell_price:
        exchange_rate = (float(sell_price) + float(buy_price)) / 2
        if button:
            final_amount = (float(money) * float(exchange_rate))
            st.subheader(f'You will receive {final_amount} {desired_currency}')

