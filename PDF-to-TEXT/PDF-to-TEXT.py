import PyPDF2


def convert_pdf_to_text(pdf_file_path, text_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)


convert_pdf_to_text('франция eng.pdf', 'eng france')
