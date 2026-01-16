"""
2단계: 텍스트 출력 함수들
학습 목표: 다양한 방식으로 텍스트 출력하기
"""

import streamlit as st

# ============================================
# 1. 제목과 헤더
# ============================================
st.title("📝 텍스트 출력 함수 배우기")
st.header("1. 제목과 헤더")
st.subheader("이것은 소제목입니다")

st.write("""
Streamlit은 다양한 방식으로 텍스트를 출력할 수 있습니다.\n
각 함수의 용도를 이해하고 적절히 사용하는 것이 중요합니다.
""")

# ============================================
# 2. 일반 텍스트
# ============================================
st.divider()
st.header("2. 일반 텍스트")

st.text("이것은 st.text() 함수입니다.")
st.write("이것은 st.write() 함수입니다. - 가장 많이 사용됩니다!")

# st.write는 마크다운도 지원합니다
st.write("**굵은 글씨**, *기울임*, ~~취소선~~")

# ============================================
# 3. 마크다운
# ============================================
st.divider()
st.header("3. 마크다운")

st.markdown("""
### 마크다운으로 작성한 소제목

마크다운을 사용하면 더 풍부한 서식을 사용할 수 있습니다:
- **굵은 글씨**
- *기울임*
- `코드 강조`
- [링크](https://streamlit.io)

#### 리스트
1. 첫 번째
2. 두 번째
3. 세 번째
""")

# ============================================
# 4. 코드 블록
# ============================================
st.divider()
st.header("4. 코드 블록")

st.code("""
def hello():
    print("Hello, Streamlit!")
    return "안녕하세요"
""", language="python")

# 다른 언어도 가능합니다
st.code("""
SELECT * FROM users
WHERE age > 20
ORDER BY name;
""", language="sql")

# ============================================
# 5. 수식 (LaTeX)
# ============================================
st.divider()
st.header("5. 수식")

st.latex(r"""
E = mc^2
""")

st.latex(r"""
\sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n
""")

# ============================================
# 6. 상태 메시지
# ============================================
st.divider()
st.header("6. 상태 메시지")

st.success("✅ 성공 메시지 - 작업이 성공적으로 완료되었습니다!")
st.info("ℹ️ 정보 메시지 - 유용한 정보를 제공합니다.")
st.warning("⚠️ 경고 메시지 - 주의가 필요합니다.")
st.error("❌ 에러 메시지 - 문제가 발생했습니다.")

# ============================================
# 7. 기타 유용한 함수
# ============================================
st.divider()
st.header("7. 기타 유용한 함수")

st.caption("이것은 작은 설명 텍스트입니다 (캡션)")

# 인용문
st.markdown("> 누구나 코딩을 할 수 있다. - 박태근")

# 인터넷상 이미지
st.caption("인터넷상 이미지 표시")
st.image("data:image/jpeg;base64,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",use_container_width=True)

# 이미지 사이즈를 화면에 맞추고싶다면? 강제로 늘릴 수 있음
st.image("https://placehold.co/300x300")
# st.image("https://placehold.co/300x300", use_container_width=True)

# 로컬 이미지
st.caption("내 컴퓨터의 이미지 표시")
st.image('image/sample1.jpg')

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제: 뉴스 기사 만들기

다음 요소들을 포함한 가상의 뉴스 기사를 만들어보세요:
1. `st.title()`로 기사 제목
2. `st.caption()`으로 작성자와 날짜
3. `st.image()`로 이미지 (URL 사용 가능)
4. `st.markdown()`으로 본문 내용
5. `st.info()`로 관련 정보 박스
6. `st.code()`로 코드나 데이터 예시
""")

# 예시 답안 (접어두기)
with st.expander("💡 예시 답안 보기"):
    st.title("🚀 AI 기술의 새로운 돌파구")
    st.caption("작성자: 홍길동 | 2026-01-15")
    
    st.image("https://placehold.co/600x400", caption="AI 연구소")
    
    st.markdown("""
    최근 연구진이 새로운 AI 알고리즘을 개발했다고 발표했습니다.
    
    이 기술은 기존 방식보다 **50% 더 빠른** 처리 속도를 보여줍니다.
    """)
    
    st.info("이 기술은 2027년 상용화될 예정입니다.")

import streamlit as st

# 1. 기사 제목
st.title("치이카와, 서울 한복판에 등장! 🐹🦊🐰\n'귀여움으로 도심 교통 마비'")

# 2. 작성자와 날짜
st.caption("작성자: 치이뉴스 편집부 | 2026-01-16")

# 3. 이미지 (URL 사용)
st.image(
    "https://images.unsplash.com/photo-1601758260747-9c3bafa286f4?auto=format&fit=crop&w=1200&q=80",
    caption="서울 도심에 갑자기 나타난(?) 치이카와 스타일 코스프레 팬들",
    use_column_width=True
)

# 4. 본문 내용
st.markdown(
"""
서울 도심 한복판에 **치이카와**들이 나타났다는 소식에 시민들이 환호성을 질렀다.  
16일 오전 10시, 종로 일대에는 치이카와, 하치와레, 우사기 코스프레를 한 팬들이  
게릴라 퍼레이드를 펼치며 도심을 ‘귀여움’으로 물들였다.

---

### 🐹 현장을 뒤집어 놓은 치이카와들

목격자 A씨는 이렇게 전했다.

> "출근길에 갑자기 앞에서 `(*´∀｀*)` 이런 얼굴을 한 치이카와가 춤을 추고 있더라구요.  
>  순간적으로 모든 스트레스가 사라졌습니다."

현장에는 다양한 치이카와 관련 소품이 등장했다.

- 치이카와 봉제인형 🧸  
- 하치와레 머리띠 😺  
- 우사기 풍선 🎈  
- 그리고 “**오늘도 열심히 살아볼까… (๑•̀ㅂ•́)و✧**” 라는 문구의 피켓까지

---

### 🦊 SNS를 뒤덮은 귀여움 폭발

퍼레이드 소식은 실시간으로 SNS에 퍼지며  
해시태그 `#치이카와서울상륙`, `#오늘도_귀여워서_버틴다` 가 트렌드 상위권에 올랐다.

한 이용자는 이렇게 남겼다.

> "치이카와들 때문에 버스 놓쳤는데, 화가 안 난다… 이게 바로 힐링… (´･ω･`)🍯"

---

### 🐰 시민 반응은?

대부분의 시민은 긍정적인 반응을 보였지만,  
일부 시민들은 “귀여움 과다 노출로 업무 집중 불가”라며 웃픈(?) 목소리를 내기도 했다.

한 회사원은 이렇게 말했다.

> "사무실에 들어와도 머릿속엔 치이카와 얼굴밖에 안 떠올라요…  
>  보고서 대신 치이카와 낙서만 늘었어요. (╯°□°）╯︵ ┻━┻"

주최 측은 “이번 행사를 시작으로,  
연말까지 **치이카와 힐링 캠페인**을 이어가겠다”고 밝혔다.
"""
)

# 5. 관련 정보 박스
st.info(
"""
### ℹ 치이카와 서울 이벤트 한눈에 보기

- 📍 장소: 서울 종로 일대, 한강공원, 홍대 걷고싶은 거리  
- 🗓 기간: 2026년 1월 16일 ~ 1월 31일  
- 🎪 프로그램:
  - 치이카와 퍼레이드
  - 굿즈 플리마켓
  - 치이카와 드로잉 클래스
  - 성우 라이브 토크 (온라인 스트리밍 포함)
- 🔗 공식 해시태그: `#치이카와서울`, `#치이카와힐링캠페인`
"""
)

# 6. 코드나 데이터 예시
st.code(
"""
# 치이카와 굿즈 인기 순위 (예시 데이터)
chiikawa_goods = [
    {"name": "치이카와 인형", "price": 32000, "emoji": "🐹", "popularity": 98},
    {"name": "하치와레 머리띠", "price": 15000, "emoji": "😺", "popularity": 95},
    {"name": "우사기 키링", "price": 12000, "emoji": "🐰", "popularity": 92},
    {"name": "치이카와 머그컵", "price": 18000, "emoji": "☕", "popularity": 89},
]

# 가장 인기 있는 굿즈 출력
top_item = max(chiikawa_goods, key=lambda x: x["popularity"])

print(f"오늘의 TOP 굿즈는? {top_item['emoji']} {top_item['name']}")
print(f"가격: {top_item['price']}원, 인기 지수: {top_item['popularity']} / 100")

# 출력 예시:
# 오늘의 TOP 굿즈는? 🐹 치이카와 인형
# 가격: 32000원, 인기 지수: 98 / 100
""",
language="python"
)
