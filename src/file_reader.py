from io import BytesIO

from docx import Document
from pypdf import PdfReader

# function to read .txt files 
def read_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8", errors="ignore")

# function to read .pdf files
def read_pdf(uploaded_file):
    pdf_reader = PdfReader(BytesIO(uploaded_file.read()))
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# function to read .docx files
def read_docx(uploaded_file):
    document = Document(BytesIO(uploaded_file.read()))
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return ""
    
    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):
        return read_txt(uploaded_file)
    elif filename.endswith(".pdf"):
        return read_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return read_docx(uploaded_file)
    else:
        raise ValueError(f"Unsupported file type: {filename}")