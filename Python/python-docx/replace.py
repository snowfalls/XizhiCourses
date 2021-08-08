from docx import Document
import re

doc = Document(r"D:\论文.docx")
restr = '[A-Z]+'

for p in doc.paragraphs:
    matchRet = re.findall(restr, p.text)
    print(matchRet) 
    for r in matchRet:
        print(r)
        lower = r.lower()
        p.text = p.text.replace(r, lower)

doc.save(r'D:\论文_修正.docx')