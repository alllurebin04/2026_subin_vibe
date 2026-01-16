"""
1단계: Streamlit 소개 및 첫 번째 앱
학습 목표: Streamlit의 기본 구조 이해하기
"""

import streamlit as st

# 브라우저창 텝을 보면 아이콘과 페이지 타이틀이 바뀌어있는것을 볼 수 있다.
st.set_page_config(
    page_title="스트림릿과의 만남",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

# 제목 표시
st.title(":hamster: 이수빈 :hamster:")

# 간단한 텍스트 출력
st.write("안녕하세요! Streamlit에 오신 것을 환영합니다.")

# 구분선
st.divider()

# 자기소개 섹션
st.header("자기소개")
st.write("이름: 수빈")
st.write("직업: 무직")
st.write("관심사: 재밌는 활동")

# 구분선
st.divider()

# 간단한 인터랙션
st.subheader("버튼을 눌러보세요!")
if st.button("인사하기"):
    st.balloons()  # 풍선 애니메이션
    st.success("반갑습니다! :hamster:")
    import streamlit as st
import random
import time

import streamlit as st

import streamlit as st

st.set_page_config(page_title="햄스터 팝콘", layout="wide")

st.title("🐹 햄스터 팝콘 머신")
st.write("버튼을 눌러 햄스터를 튀겨보세요!")

# 전체 영역에 relative position을 주기 위한 컨테이너
container = st.container()
with container:
    root_html = """
    <div id="popcorn-root" style="
        position: relative;
        height: 400px;
        width: 100%;
        overflow: hidden;
        background: radial-gradient(circle at top, #fff7e6 0, #ffe0b3 40%, #ffd1a3 100%);
        border-radius: 12px;
        border: 1px solid #f0c68a;
    ">
    </div>
    """
    st.markdown(root_html, unsafe_allow_html=True)

def make_popcorn_script(num=25):
    # ⚠️ JS 안에서만 쓰는 변수/문법이고, 파이썬은 num 말고는 건드리지 않게 구성
    js_code = f"""
    <script>
    const root = window.parent.document.querySelector('#popcorn-root');
    if (root) {{
        for (let i = 0; i < {num}; i++) {{
            const span = document.createElement('span');
            span.textContent = '🐹';

            const size = 24 + Math.random() * 48;       // 24 ~ 72px
            const x = Math.random() * 90;               // 왼쪽에서 0~90%
            const y = 20 + Math.random() * 60;          // 위에서 20~80%
            const rot = (Math.random() - 0.5) * 80;     // -40 ~ 40deg
            const up = 10 + Math.random() * 40;         // 튀어오를 높이

            // 템플릿 리터럴 안 쓰고, 그냥 문자열 이어 붙이기
            span.style.position = "absolute";
            span.style.transition = "all 0.3s ease-out";
            span.style.transformOrigin = "center";
            span.style.pointerEvents = "none";
            span.style.fontSize = size + "px";
            span.style.left = x + "%";
            span.style.top = y + "%";
            span.style.transform = "translateY(0px) rotate(" + rot + "deg)";
            span.style.opacity = 0;

            root.appendChild(span);

            // 약간의 딜레이를 두고 튀게
            setTimeout(() => {{
                span.style.opacity = 1;
                span.style.transform = "translateY(-" + up + "px) rotate(" + rot + "deg)";
            }}, 50 + i * 20);

            // 다시 내려가면서 사라지게
            setTimeout(() => {{
                span.style.opacity = 0;
                span.style.transform = "translateY(" + (up / 2) + "px) rotate(" + rot + "deg)";
            }}, 400 + i * 20);

            // 완전히 제거
            setTimeout(() => {{
                if (span && span.parentNode) {{
                    span.parentNode.removeChild(span);
                }}
            }} , 900 + i * 20);
        }}
    }}
    </script>
    """
    return js_code


# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")
st.markdown("""
1. 제목을 자신의 이름으로 변경해보세요
2. 자기소개 내용을 본인의 정보로 바꿔보세요
3. 새로운 버튼을 추가하고, 클릭 시 다른 메시지가 나오도록 해보세요
4. `st.warning()` 또는 `st.error()` 함수를 사용해보세요
""")
