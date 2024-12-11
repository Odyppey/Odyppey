import streamlit as st
import pandas as pd
import numpy as np

st.title("自転車の消費カロリー計算アプリ")

weight = st.number_input('自分の体重を入力 (kg)', min_value=20.0, max_value=200.0, value=60.0)

activity_type = st.radio(
    "強度を選択",
    ["下り","ゆるぽた",  "強度高めな平坦", "上り坂",  "レース","4分44秒で上る地附山","二回足をつく地附山"])

activity_time = st.number_input('運動時間を入力 (分)', min_value=1, max_value=300, value=60)
if activity_type == "4分44秒で上る地附山":
    activity_time = 4.73
    st.write("運動時間は4分44秒に固定されています。")
if activity_type == "二回足をつく地附山":
    activity_time = 10.66
    st.write("運動時間は「気が遠くなるほど遅かった」に固定されています。")    

if st.button("消費カロリーを計算する"):
    if activity_type == "4分44秒で上る地附山": activity_time = 4.73
    if activity_type == "二回足をつく地附山": activity_time = 10.66
    met_values = {
        "二回足をつく地附山": 1.0 ,
        "下り": 3.1 ,     
        "ゆるぽた": 4.0,    
        "強度高めな平坦": 8.0,    
        "上り坂": 12.0,    
        "レース": 15.5,
        "4分44秒で上る地附山": 16.0
           }
    
    


    met = met_values[activity_type]
    calories = met * weight * (activity_time / 60)
    messages = {
        "二回足をつく地附山": "だから平均体重だみん",
        "下り": "下ってる",
        "ゆるぽた": "ゆるゆる",
        "強度高めな平坦": "ちょき",
        "上り坂": "これはおくすそばな",
        "レース": "れーす",
        "4分44秒で上る地附山": "じづじづ",
   }

    st.write(f"選択した運動: **{activity_type}**")
    st.write(f"運動時間: **{activity_time}分**")
    st.write(f"体重: **{weight}kg**")
    st.write(f"消費カロリー: **{calories:.0f} kcal**")
    st.write(f"ひとこと: {messages[activity_type]}")
    if activity_type == "4分44秒で上る地附山": st.image("103161.jpg")
    if activity_type == "レース": st.image("103147.jpg")
    if activity_type == "上り坂": st.image("103164.jpg")
    if activity_type == "下り": st.image("103165.jpg")
    if activity_type == "ゆるぽた": st.image("103167.jpg")
    if activity_type == "強度高めな平坦": st.image("103166.jpg")
    if activity_type == "二回足をつく地附山":st.image("103169.jpg")