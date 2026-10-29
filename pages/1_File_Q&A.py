import streamlit as st
import anthropic
from pypdf import PdfReader
from io import BytesIO

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="centered",
)

st.title("📚 StudyMate AI")
st.subheader("Your personal PDF study assistant")
st.write(
    "Upload your study notes, ask questions, and get "
    "student-friendly explanations based on your material."
)

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
    )
    st.caption(
        "An API key is needed for AI-generated answers. "
        "Never share or commit your key to GitHub."
    )

uploaded_file = st.file_uploader(
    "Upload your study material",
    type=["pdf", "txt", "md"],
)

document_text = ""

if uploaded_file is not None:
    try:
        if uploaded_file.name.lower().endswith(".pdf"):
            reader = PdfReader(BytesIO(uploaded_file.getvalue()))
            document_text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )
        else:
            document_text = uploaded_file.getvalue().decode(
                "utf-8",
                errors="replace",
            )

        if document_text.strip():
            st.success("Document loaded successfully!")
            st.caption(
                f"File: {uploaded_file.name} · "
                f"Characters extracted: {len(document_text):,}"
            )

            with st.expander("Preview document text"):
                st.text(document_text[:5000])
        else:
            st.warning(
                "No readable text was found. A scanned PDF may "
                "need OCR before its contents can be extracted."
            )

    except Exception as error:
        st.error(f"Could not read this document: {error}")

question = st.text_area(
    "What would you like to learn?",
    placeholder=(
        "Example: Summarize this chapter, explain a concept, "
        "or list the key points."
    ),
    disabled=not document_text.strip(),
)

if st.button(
    "✨ Generate Answer",
    type="primary",
    disabled=not document_text.strip() or not question.strip(),
):
    if not api_key.strip():
        st.warning(
            "To generate an AI answer, enter an Anthropic API key "
            "in the sidebar. You can still preview extracted text "
            "without a key."
        )
    else:
        try:
            with st.spinner("Preparing your answer..."):
                client = anthropic.Anthropic(
                    api_key=api_key.strip()
                )

                response = client.messages.create(
                    model="claude-haiku-4-5",
                    max_tokens=800,
                    system=(
                        "You are StudyMate AI, a helpful study assistant. "
                        "Answer using the supplied study material. "
                        "Explain ideas clearly for a student. Use "
                        "headings or bullet points when useful. If the "
                        "material does not contain the answer, say so "
                        "instead of inventing information."
                    ),
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                "Study material:\n\n"
                                f"{document_text[:40000]}\n\n"
                                f"Question: {question}"
                            ),
                        }
                    ],
                )

            answer = "\n".join(
                block.text
                for block in response.content
                if block.type == "text"
            )

            st.subheader("📖 Your Answer")
            st.markdown(answer)

        except Exception as error:
            st.error(
                "We couldn't generate an answer. Check that your "
                "API key is valid, your account has API access, "
                "and your connection is working."
            )
            st.caption(f"Technical details: {error}")

st.divider()
st.caption(
    "StudyMate AI · Built with Python, Streamlit, and pypdf"
)