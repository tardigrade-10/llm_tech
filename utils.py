from PyPDF2 import PdfReader

def pdf_to_txt(pdf_file):

    # creating a pdf reader object
    reader = PdfReader(pdf_file)
    
    # printing number of pages in pdf file
    pages = len(reader.pages)
    
    # getting a specific page from the pdf file
    text_filename = pdf_file[:-4] + "_text.txt"

    with open(text_filename, "w") as f:
        for i in range(pages):
            page = reader.pages[i]
    
            # extracting text from page
            text = page.extract_text()
            f.write(text)