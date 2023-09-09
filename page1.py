import streamlit as st
st.title('새 탭 만들기!')

image_path = 'jang.gif'
#이미지를 화면에 출력
st.image(image_path)

#라디오버튼
mbti = st.radio(
    '누구일까요?',
    ('장원영','김채원','조유리')
)
if mbti == '장원영':
    st.write('정답입니다!')
elif mbti == '김채원':
    st.write('틀렸습니다.다시생각해 보세요')
elif mbti == '조유리':
    st.write('틀렸습니다.다시생각해 보세요')
