import zipfile
import xml.etree.ElementTree as ET
import os
import sys

def read_docx(path):
    try:
        document_text = []
        with zipfile.ZipFile(path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.XML(xml_content)
            
            # The word namespace
            WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
            PARA = WORD_NAMESPACE + 'p'
            TEXT = WORD_NAMESPACE + 't'
            
            for paragraph in tree.iter(PARA):
                texts = [node.text for node in paragraph.iter(TEXT) if node.text]
                if texts:
                    document_text.append(''.join(texts))
        return '\n'.join(document_text)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    path = "C:\\Users\\GRACY SAHAYAM\\Desktop\\BAS.docx"
    text = read_docx(path)
    with open("e:\\final\\bas_content.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extraction complete. Output len:", len(text))
