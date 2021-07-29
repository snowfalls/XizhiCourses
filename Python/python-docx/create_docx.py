from docx import Document

document = Document()
paragraph = document.add_paragraph('lorem ipsum door sit amet.')
prior_paragraph = paragraph.insert_paragraph_before('Lorem ipsum')

document.save(r"D:\test.docx")