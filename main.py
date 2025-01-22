from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
#Page is not broke automatically
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv("topics.csv")

r1 = 20



for index, row in df.iterrows():

    pdf.add_page()
# Set the header
    pdf.set_font(family='Times', style="BIU", size=24)
    pdf.set_text_color(48, 213, 200)
    pdf.cell(w=0, h=12, align="L", ln=1, txt=row["Topic"])

#Added break line
    pdf.ln(260)
#Set the footer
    pdf.set_font(family='Times', style="I", size=10)
    pdf.set_text_color(40, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")


    for p1 in range(30, 290, 10):
        pdf.set_draw_color(180, 180, 180)
        pdf.line(x1=10, y1=p1, x2=200, y2=p1)


    for _ in range(row["Pages"]-1):
        pdf.add_page()
        for r1 in range(20, 290, 10):
            pdf.set_draw_color(180, 180, 180)
            pdf.line(x1=10, y1=r1, x2=200, y2=r1)

        pdf.ln(270)

        pdf.set_font(family='Times', style="I", size=10)
        pdf.set_text_color(40, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")




pdf.output("output.pdf")