import streamlit as st


cq1, cq2, cq3, cq4, cq5 = st.columns(5)
with cq1:
   st.image('화면 캡처 2023-09-08 204412.png')
with cq2:
   st.write('for_everyoung10✅')
with cq3:
   button = st.button('팔로잉🔽')
with cq4:
   button = st.button('메세지보내기')
with cq5:
   button = st.button('◾◾◾')



c1, c2, c3 = st.columns(3)
with c1:
   st.write('게시물222')
with c2:
   st.write('팔로워942.6만')
with c3:
   st.write('팔로우13')

st.write('장원영 WONYOUNG')
st.write('jeongyun1205, itseunmini, jimin1565님 외 6명이 팔로우합니다')

tab1, tab2, tab3 = st.tabs(["▦게시물", "🎬릴스", "🙍‍♀️태그됨"])

with tab1:
   col1, col2, col3 = st.columns(3)

   with col1:
      st.image("화면 캡처 2023-09-08 201440.png")

   with col2:
      st.image("3.heic")

   with col3:
      st.image("2.heic")
   coll1, coll2, coll3 = st.columns(3)

   with coll1:
      st.image("4.heic")

   with coll2:
      st.image("5.jpg")

   with coll3:
      st.image("6.jpg")
with tab2:
   coll1, coll2, coll3,  coll4 = st.columns(4)

   with coll1:
      st.image("11.png")

   with coll2:
      st.image("12.png")

   with coll3:
      st.image("13.png")
   with coll4:
      st.image("14.png")
   cl1, cl2, cl3, cl4 = st.columns(4)

   with cl1:
      st.image("15.png")
   with cl2:
      st.image("16.png")

   with cl3:
      st.image("17.png")
   with cl4:
      st.image("18.png")

with tab3:
   a1, a2, a3 = st.columns(3)

   with a1:
      st.image("tag1.png")

   with a2:
      st.image("tag2.png")

   with a3:
      st.image("tag3.png")
   a11, a12, a13 = st.columns(3)

   with a11:
      st.image("tag4.png")

   with a12:
      st.image("tag5.png")

   with a13:
      st.image("20.png")
font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
