import streamlit as st
from catboost import CatBoostRegressor
import pandas as pd

from predict import load_model
from confirm_button_hack import cache_on_button_press


# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# 비밀번호 설정
root_password = 'thumbup'


def main():
    st.title("Book Rating Prediction Model")
    
    # 모델 불러오기
    model = load_model()

    # 입력값 받기(ID, ISBN)
    ID_input = st.text_input("유저 ID를 입력해주세요")
    ISBN_input = st.text_input("책 ISBN을 입력해주세요")

    if ID_input and ISBN_input:
        # 예측값 출력
        st.write("Predicting...")
        y_hat = model.predict([int(ID_input), ISBN_input])

        st.write(f'Prediction Rating!: {y_hat}')


# 비밀번호 입력
@cache_on_button_press('Authenticate')
def authenticate(password) ->bool:
    print(type(password))
    return password == root_password

password = st.text_input('password', type="password")

if authenticate(password):
    st.success('You are authenticated!')
    main()
else:
    st.error('The password is invalid.')

# 입력데이터 리스트 보여주기
submit_df = pd.read_csv('sample_submission.csv')
st.dataframe(submit_df)