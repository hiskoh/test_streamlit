import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st


st.title("簡単な電卓アプリ")

# 入力欄
num1 = st.number_input("1つ目の数字を入力", format="%.2f")
num2 = st.number_input("2つ目の数字を入力", format="%.2f")

# 演算子選択
operation = st.selectbox("演算子を選んでください", ["足し算 (+)", "引き算 (-)", "掛け算 (*)", "割り算 (/)"])

# 計算ボタン
if st.button("計算"):
    if operation == "足し算 (+)":
        result = num1 + num2
    elif operation == "引き算 (-)":
        result = num1 - num2
    elif operation == "掛け算 (*)":
        result = num1 * num2
    elif operation == "割り算 (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "エラー: 0で割ることはできません"

    st.subheader(f"結果: {result}")
