import streamlit as st
from PyPDF2 import PdfReader

# 화면 기본 설정 (미니멀하고 깔끔한 레이아웃)
st.set_page_config(page_title="PDF 텍스트 에디터", page_icon="📝", layout="centered")

st.title("📝 심플 PDF 텍스트 에디터")
st.markdown("PDF 문서의 텍스트를 추출하여 자유롭게 수정하고 다시 저장할 수 있습니다. 복잡한 과정 없이 핵심 기능에만 집중했습니다.")

# 1단계: 파일 업로드
st.subheader("1️⃣ PDF 파일 업로드")
uploaded_file = st.file_uploader("여기를 클릭하거나 파일을 드래그 앤 드롭 하세요.", type="pdf")

if uploaded_file is not None:
    # PDF 읽기 준비
    reader = PdfReader(uploaded_file)
    
    st.write("---")
    st.subheader("2️⃣ 텍스트 수정하기")
    st.info("💡 원본 PDF의 복잡한 디자인(레이아웃, 이미지)은 덜어내고, 오직 '텍스트 정보'만 가져옵니다.")
    
    # 전체 페이지 텍스트 추출
    all_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            # 사용자가 페이지 구분을 쉽게 인지할 수 있도록 어포던스(Affordance) 제공
            all_text += f"==== {i+1} 페이지 ====\n{text}\n\n"
            
    # 사용자가 직접 글자를 지우고 쓸 수 있는 커다란 텍스트 박스
    edited_text = st.text_area(
        "아래 상자 안의 글자를 자유롭게 편집하세요:", 
        value=all_text, 
        height=500
    )
    
    st.write("---")
    st.subheader("3️⃣ 수정된 내용 저장하기")
    
    # 3단계: 결과물 다운로드
    st.download_button(
        label="💾 수정된 텍스트 다운로드 (.txt)",
        data=edited_text,
        file_name="edited_document.txt",
        mime="text/plain"
    )
    
    # 현실적인 제약사항 안내
    st.caption("⚠️ **개발자 노트:** 스트림릿 클라우드 서버는 기본적으로 한글 폰트를 지원하지 않아, PDF로 바로 구울 경우 글자가 네모(ㅁ)로 깨지는 현상이 발생합니다. 이를 방지하고 데이터 손실을 막기 위해 텍스트(.txt) 파일로 안전하게 저장됩니다. 다운로드 후 워드나 한글(HWP)에 붙여넣으시면 가장 깔끔합니다.")