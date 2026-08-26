import streamlit as st
import time

# 1. 페이지 기본 설정 및 디자인 테마
st.set_page_config(
    page_title="✨ MBTI Dream Career ✨",
    page_icon="🔮",
    layout="wide"
)

# 2. 커스텀 CSS (화려한 배경, 3D 카드, 애니메이션 효과)
st.markdown("""
    <style>
    /* 전체 배경 그라데이션 및 글꼴 */
    .stApp {
        background: linear-gradient(135deg, #FF9A9E 0%, #FECFEF 50%, #A1C4FD 100%);
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 메인 타이틀 스타일 */
    .main-title {
        text-align: center;
        font-size: 3rem !important;
        font-weight: 800;
        color: #2D3748;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.1);
        padding: 1rem 0;
    }
    
    /* MBTI 정보 카드 */
    .mbti-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.5);
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* 직업 추천 카드 (3D 호버 효과) */
    .job-card {
        background: white;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-top: 5px solid #FF6B6B;
        height: 100%;
    }
    .job-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    }
    
    /* 강점 태그 스타일 */
    .tag {
        display: inline-block;
        background: #E2E8F0;
        color: #4A5568;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: bold;
        margin: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI별 진로 데이터베이스
mbti_data = {
    "ISTJ": {
        "title": "🔍 신중하고 철저한 체계주의자",
        "desc": "책임감이 강하고 현실적이며, 조직적이고 체계적으로 일을 처리하는 능력이 뛰어나요!",
        "strengths": ["#신뢰성", "#원칙주의", "#정교함", "#집중력"],
        "jobs": [
            {"name": "💼 회계사 / 세무사", "desc": "숫자와 데이터를 정확하게 다루고 규정을 준수해요.", "tip": "정확성과 분석력이 강점인 당신에게 딱!"},
            {"name": "💻 소프트웨어 검증 엔지니어", "desc": "시스템의 오류를 찾아내고 안정성을 높여요.", "tip": "꼼꼼함으로 완벽한 프로그램을 만들어요."},
            {"name": "🏛️ 공무원 / 행정가", "desc": "사회 규범을 지키며 안정적으로 조직을 운영해요.", "tip": "투철한 책임감으로 빛을 발해요."}
        ]
    },
    "ENFP": {
        "title": "🦄 열정적인 재능부자 에너자이저",
        "desc": "상상력이 풍부하고 창의적이며, 새로운 가능성을 찾고 사람들에게 영감을 줘요!",
        "strengths": ["#창의력", "#친화력", "#열정", "#아이디어자판기"],
        "jobs": [
            {"name": "🎨 크리에이티브 디렉터", "desc": "새롭고 혁신적인 브랜드와 콘텐츠 콘셉트를 기획해요.", "tip": "영감이 넘치는 당신의 아이디어를 펼쳐보세요!"},
            {"name": "🎙️ 이벤트 기획자 / MC", "desc": "사람들과 소통하며 즐거운 무대와 행사를 만들어가요.", "tip": "인싸력 폭발! 어디서나 분위기 메이커!"},
            {"name": "🚀 스타트업 창업가", "desc": "세상에 없던 새로운 서비스와 가치를 만들어내요.", "tip": "도전 정신으로 세상을 바꾸는 주역!"}
        ]
    },
    "INTJ": {
        "title": "🧠 용의주도한 전략가",
        "desc": "독창적인 사고와 강한 직관력으로 거대한 목표를 설계하고 실행해나갑니다!",
        "strengths": ["#통찰력", "#전략적사고", "#독립성", "#문제해결"],
        "jobs": [
            {"name": "📊 데이터 사이언티스트", "desc": "복잡한 데이터 속에서 미래의 패턴과 인사이트를 도출해요.", "tip": "논리적 사고의 끝판왕!"},
            {"name": "🪐 우주항공 공학자", "desc": "최첨단 기술과 이론을 바탕으로 미래를 설계해요.", "tip": "원대한 거시적 비전을 현실로!"},
            {"name": "👔 경영 컨설턴트", "desc": "기업의 문제점을 진단하고 장기적인 성장의 길을 제시해요.", "tip": "명석한 분석으로 최고의 전략 수립!"}
        ]
    },
    "ESFJ": {
        "title": "🤝 친절한 겉바속촉 힐러",
        "desc": "타인에게 관심이 많고 친절하며, 집단의 화합과 협력을 이끌어내는 능력이 탁월해요!",
        "strengths": ["#공감능력", "#협동심", "#친화력", "#봉사정신"],
        "jobs": [
            {"name": "👩‍🏫 교사 / 교육 컨설턴트", "desc": "학생들의 성장을 돕고 용기를 북돋아주는 가이드가 되어줘요.", "tip": "따뜻한 마음으로 인재를 양성해요!"},
            {"name": "🏥 의료 보건 전문가", "desc": "환자의 마음까지 따뜻하게 돌보는 의료 서비스를 제공해요.", "tip": "세상을 더 따뜻하게 만드는 유능한 인재!"},
            {"name": "✈️ 항공 승무원", "desc": "고객의 세심한 부분까지 케어하며 최고의 경험을 선물해요.", "tip": "뛰어난 센스와 친절함의 대명사!"}
        ]
    }
    # 필요시 다른 MBTI 유성을 동일한 포맷으로 추가 가능합니다!
}

# 4. 헤더 영역 (화려한 이모지 폭탄)
st.markdown("<h1 class='main-title'>🌈✨ MBTI 드림 캐치! ✨🌈</h1>", unsafe_unsafe_html=True)
st.markdown("<h3 style='text-align: center; color: #4A5568;'>🔮 나만의 성격 유형에 딱 맞는 찰떡 직업을 찾아봐요! 🚀</h3>", unsafe_allow_html=True)
st.write("")

# 5. MBTI 선택 사이드바 / 드롭다운
selected_mbti = st.selectbox(
    "👉 **당신의 MBTI 성격 유형을 선택해 주세요!**",
    options=["ENFP", "ISTJ", "INTJ", "ESFJ"], # 전체 목록 확장을 위해 기본 옵션 구성
    index=0
)

st.divider()

# 6. 메인 결과 출력
if selected_mbti in mbti_data:
    info = mbti_data[selected_mbti]
    
    # 로딩 애니메이션 연출
    with st.spinner("🔮 수정구슬이 당신의 미래를 분석하고 있습니다... ✨"):
        time.sleep(0.4)
    
    # 🎉 폭죽 효과
    st.balloons()
    
    # MBTI 프로필 카드
    st.markdown(f"""
        <div class="mbti-card">
            <h2 style="color: #2B6CB0; margin-bottom: 5px;">[{selected_mbti}] {info['title']}</h2>
            <p style="font-size: 1.1rem; color: #4A5568; margin-bottom: 15px;">{info['desc']}</p>
            <div>
                {' '.join([f'<span class="tag">{tag}</span>' for tag in info['strengths']])}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🌟 **추천 진로 & 직업 TOP 3**")
    
    # 3개 컬럼 레이아웃으로 직업 카드 배치
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    for idx, job in enumerate(info['jobs']):
        with cols[idx]:
            st.markdown(f"""
                <div class="job-card">
                    <h3 style="color: #2D3748; font-size: 1.3rem;">{job['name']}</h3>
                    <p style="color: #718096; font-size: 0.95rem; min-height: 50px;">{job['desc']}</p>
                    <hr style="border: 0; border-top: 1px solid #EDF2F7; margin: 10px 0;">
                    <p style="color: #DD6B20; font-weight: bold; font-size: 0.85rem;">💡 추천 이유: {job['tip']}</p>
                </div>
            """, unsafe_allow_html=True)

st.write("")
st.divider()

# 7. 교육용 인터랙티브 코너 (선택 항목에 대한 피드백)
st.markdown("### 💌 **미래의 나에게 보내는 한 줄 응원**")
user_goal = st.text_input("🎓 꿈을 향한 나의 다짐을 적어보세요! (예: 멋진 디자이너가 될 거야!)")

if user_goal:
    st.success(f"💖 **멋져요!** '{user_goal}'라는 꿈을 응원합니다! 👏🎉✨")
    st.snow()
