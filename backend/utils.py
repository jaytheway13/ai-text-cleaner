import docx2txt
import PyPDF2
from io import BytesIO

def extract_text_from_file(file):
    filename = file.filename
    if filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    elif filename.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return "Desteklenmeyen dosya türü."
