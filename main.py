import streamlit as st

st.set_page_config(
    page_title='공동교육과정',
    page_icon='🤬'
)

menu = st.sidebar.selectbox('MENU', ['로그인', '자기소개', '선택과목 조사', '기타'])

if menu == '자기소개':
    st.title('자기소개')
    st.video('https://www.youtube.com/watch?v=Dx4PlwPWzt8')

elif menu == '선택과목 조사':
    st.header('함지고등학교 선택과목 조사')
    st.subheader('국어 선택')
    국어 = st.radio('', ['화법과작문', '언어와매체'])

    st.subheader('수학 선택')
    수학 = st.radio('', ['미적분', '확률과통계'])

    st.subheader('국영수 선택과목 [택2]')
    국영수 = st.multiselect('', ['심화수학', '심화국어', '심화영어', '과학중점'])
    if len(국영수) < 2:
        st.write(':red[2가지 국영수 과목을 선택해주세요.]')
    elif len(국영수) > 2:
        st.write(':red[2가지 국영수 과목을 선택해주세요.]')

    st.subheader('탐구 선택 [택3]')
    탐구 = st.multiselect('', ['물리학II', '화학II', '지구과학II', '생명과학II'])
    if len(탐구) < 3:
        st.write(':red[3가지 탐구 과목을 선택해주세요.]')
    elif len(탐구) > 3:
        st.write(':red[3가지 탐구 과목을 선택해주세요.]')


    제출 = st.button('제출')
    if 제출:
        text = ''
        for value in 국영수:
            text += value + ' '
        for value in 탐구:
            text += value + " "
        st.write(':red[선택한 과목은] ', text + ':red[이 맞습니까?]')

elif menu == '기타':
    st.title('기타')
    st.image('그림.png')

elif menu == '로그인':
    st.title('로그인')
    id = st.text_input('아이디', placeholder='아이디를 입력하세요')
    pw = st.text_input('비밀번호 🔑', type='password', placeholder='비밀번호를 입력하세요')
    login = st.button('로그인')
    if login:
        if id == '1029' and pw == '1290':
            st.write(':blue[로그인 성공]')
            st.balloons()
        else:
            st.write(':red[로그인 실패]')


#짜장면 = st.checkbox('짜장면')
#탕수육 = st.checkbox('탕수육')
#짬뽕 = st.checkbox('짬뽕')
#메뉴 = ''
#if 짜장면:
#   메뉴 = 메뉴 + '짜장면 '
#if 탕수육:
#    메뉴 = 메뉴 + '탕수육 '
#if 짬뽕:
#    메뉴 = 메뉴 + '짬뽕 '
#st.write(메뉴+'을 선택하셨습니다.')
#성별 = st.radio('당신의 성별은?', ['남자', '여자'])
#st.write('당신의 성별은 '+성별+'입니다.')   
#email = st.selectbox(
#    'E-mail을 선택하세요',
#    ['gmail.com', 'naver.com','hanmail.com']
#)
#food = st.multiselect(
#    '당신이 좋아하는 음식은?',
#    ['피자', '햄버거', '삶은계란', '파스타']
#)
#st.write(food)


# st.write('장영우')
# st.subheader('this is subheader')
# st.header('this is header')
# st.title('this is title')
# st.caption('this is caption')
# st.code('x = 10 + 20')
# btn = st.button('클릭')
# if btn:
#     st.write('버튼 클릭!')
# text = '이 버튼을 클릭하면 파일을 다운 받을 수 있습니다.'
# download_btn = st.download_button('다운로드', text)
# link_btn = st.link_button('네이버', 'https://www.naver.com')
# link_btn = st.link_button('구글', 'https://www.google.com')
# link_btn = st.link_button('함지고', 'http://www.hamji.dge.hs.kr')

# checkbox = st.checkbox('동의')
# if checkbox:
#     st.write('동의하셨습니다.')

