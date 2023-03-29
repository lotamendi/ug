# from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
styles = getSampleStyleSheet()
PAGE_HEIGHT = defaultPageSize[1]; PAGE_WIDTH = defaultPageSize[0]; 

# c = canvas.Canvas("sdfdsf.pdf")
# c.setTitle('este es el titulo')
# c.drawString(100,100,"Hola mundo")
# c.showPage()
# c.save()
Title = "Hola mundo"
pageinfo = "ejemplo"
def pagina(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch, "Primera pagina / %s"%pageinfo)
    canvas.restoreState()

def go():
    doc = SimpleDocTemplate("phello.pdf")
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    for i in range(10):
        bogustext = ("Este es el parrafo numero %s. "%i)*20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
    doc.build(Story, onFirstPage=pagina)

# go()