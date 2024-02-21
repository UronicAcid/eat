import streamlit as st
import random

# 定义食堂和概率
shitang = ['家园一楼', '家园二楼', '家园三楼', '燕南', '学一', '出去吃']
probabilities = [0.99 / 5, 0.99 / 5, 0.99 / 5, 0.99 / 5, 0.99 / 5, 0.01]

# 创建一个按钮，当点击时执行选择
if st.button('决定今天吃什么'):
    chosen = random.choices(shitang, probabilities)[0]
    if chosen == '出去吃':
        st.write('恭喜你🎉！今天出去吃！')
    else:
        st.write('今天要去的食堂是：', chosen)
    st.write('用餐愉快！')

