#from cStringIO import StringIO
import io
import sys
sys.path.append("C:/Users/nico/Desktop/Off-Top/off-top-python/pdfminer/__pycache__")
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')

    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


pdfFile= "sc.pdf"
minedText = convert(pdfFile)
print(minedText)

textFname= pdfFile + ".txt"
textF= open(textFname, "w")
textF.write(minedText)

