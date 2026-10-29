# 📚 StudyMate AI

### Your Personal AI-Powered Study Assistant

StudyMate AI is a document-based learning application designed to help students work with their study materials. Upload a PDF, text file, or Markdown document, extract its contents, and ask questions to get clear, student-friendly explanations powered by an AI language model.

## ✨ Features

- **PDF text extraction:** Extract readable text from PDF study materials using `pypdf`.
- **Multiple file formats:** Upload PDF, TXT, and Markdown files.
- **Document Q&A:** Ask questions about uploaded study materials.
- **AI-powered explanations:** Generate answers using Anthropic's Claude API.
- **Text preview:** Review extracted document content without an API key.
- **Error handling:** Display helpful messages when documents contain no extractable text or something goes wrong.

## 🛠️ Built With

- Python
- Streamlit
- pypdf
- Anthropic API

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or a compatible version
- An Anthropic API key to generate AI answers

### Installation

Clone the repository:

```bash
git clone https://github.com/Adhyayan-12/llm-examples.git
cd llm-examples
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run StudyMate AI:

```bash
python -m streamlit run "pages/1_File_Q&A.py"
```

For an isolated environment, create and activate a Python virtual environment before installing dependencies.

## 🔐 API Configuration

Document extraction and text preview work without an API key. AI-generated answers require a valid Anthropic API key, entered in the application's sidebar.

**Security note:** Never publish API keys, passwords, or other secrets in your repository.

## ⚠️ Limitations

- Scanned PDFs may require OCR to extract text from images.
- AI-generated answers require a valid API key and access to the configured Anthropic model.
- Long documents are truncated before being sent to the AI model.

## 👨‍💻 Developer

**Adhyayan Singh**  
B.Tech Computer Science Student | Aspiring Software Developer

- **GitHub Profile:** [@Adhyayan-12](https://github.com/Adhyayan-12)
- **Project Repository:** [StudyMate AI — PDF Study Assistant](https://github.com/Adhyayan-12/llm-examples)

## 📄 Acknowledgments & Open-Source Attribution

StudyMate AI is a customized learning and development project built using Python and Streamlit, with the [Streamlit LLM Examples](https://github.com/streamlit/llm-examples) repository as its starting point.

My contributions include adapting the File Q&A application into a study-focused interface, implementing PDF text extraction using `pypdf`, supporting PDF, TXT, and Markdown uploads, adding document text previews, and integrating Anthropic's API for AI-powered question answering.

This project is maintained for learning, experimentation, and portfolio development. The original project's authors are acknowledged, and the applicable license and attribution notices are retained in accordance with its licensing requirements.