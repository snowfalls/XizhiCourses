# coding:utf-8
from docx import Document
from docx.oxml.ns import qn

document = Document() 
document.styles['Normal'].font.name = u'宋体'
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

paragraph = document.add_paragraph("中国再创辉煌")
prior_paragraph = paragraph.insert_paragraph_before("东京奥运会加油")

document.save(r"D:\test.docx")