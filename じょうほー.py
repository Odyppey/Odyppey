import pandas as pd
import numpy as np


import streamlit as st
st.title('初めてのstreamlit')
st.write('これから作品を作っていきます。')
import streamlit as st
st.title('初めてのstreamlit')
st.write('これから作品を作っていきます。')
st.title('平均体重だみん')
text = st.text_input('あなたの名前を教えて！')
st.write('あなたの名前は、' +text+ 'です')
condition = st.slider('あなたの今の調子は？',0,100,50)
st.write('コンディション：',condition)
option = st.selectbox('好きな数字を教えてください',list(['１番','２番','３番','４番']))
st.write('あなたが選択したのは、'+ option + 'です')
import time
st.sidebar.write('プログレスバーの表示')

latest_iteration = st.empty() 
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i +1)
  time.sleep(0.01)
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
   right_column.write('ここは右カラムです')
from PIL import Image
img = Image.open('94644.jpg')
st.image(img,caption='生活場面',use_column_width=True)


