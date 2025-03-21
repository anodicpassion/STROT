import fpdf
import os


class Basics:
    def __init__(self):
        self.pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')

    def add_page(self):
        self.pdf.add_page()

    def heading1(self, heading: str = ""):
        self.pdf.set_font("times", style="b", size=16)
        self.pdf.cell(40, 10, heading)

        self.pdf.ln(10)

    def heading2(self, heading: str = ""):
        self.pdf.set_font("times", style="b", size=14)
        self.pdf.cell(40, 10, heading)

        self.pdf.ln(10)

    def heading3(self, heading: str = ""):
        self.pdf.set_font("times", style="b", size=12)
        self.pdf.cell(40, 10, heading)

        self.pdf.ln(10)

    def body(self, body_text: str = ""):
        self.pdf.set_font("times", size=10)

        self.pdf.multi_cell(0, 5, body_text, align="J")
        self.pdf.ln(10)

    def line(self):
        self.pdf.line(10, 20, 200, 20)

    def save(self, file_name: str = "output.pdf"):
        self.pdf.output(file_name)

    def italic(self, text):
        self.pdf.set_font("times", style="I", size=10)
        self.pdf.multi_cell(0, 5, text, align="J")
        self.pdf.ln(10)


if __name__ == "__main__":
    obj = Basics()
    obj.add_page()

    obj.heading1("heading _ 1")
    obj.line()
    # obj.heading1("ganesh")
    # obj.heading1("pratik")
    obj.heading2("heading _ 2")
    obj.heading3("heading _ 3")
    obj.italic("Hello this is italic")
    obj.body(
        "hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer")
    obj.save()

    os.system("open output.pdf")

