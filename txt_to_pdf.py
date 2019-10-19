#PASAR ARCHIVO ".txt" A PDF
from fpdf import FPDF

#ABRIR FICHERO A CONVERTIR
fichero = open("prueba.txt","r")

#OBJETO "pdf"
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",size=10)
line=1

#LECTURA ".txt"/ESCRITURA ".pdf"
for linea in fichero:
    pdf.cell(200,7,txt=linea,ln=line,align="L")
    if linea[-1]==("\n"):
        linea=linea[:-1]
    line+=1

#CREAR PDF
pdf.output("prueba2.pdf")

#CERRAR FICHERO.
fichero.close()

