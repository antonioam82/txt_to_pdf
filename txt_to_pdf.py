#PASAR ARCHIVO ".txt" A PDF
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",size=10)
line=1

fichero = open("prueba.txt","r")

for linea in fichero:
    if linea[-1]==("\n"):
        linea=linea[:-1]
    pdf.cell(200,7,txt=linea,ln=line,align="L")
    line+=1

pdf.output("prueba5.pdf")
fichero.close()
