from fpdf import FPDF


class asian_character_worksheet_generator():
    pdf = FPDF()
    pdf.add_font('fireflysung', '', 'fireflysung.ttf', uni=True)
    pdf.set_font("fireflysung", size=30)
    size = 19
    num_x_cell = 14
    num_y_cell = 8
    file = "text"

    def read_file(self):
        f = open(self.file, "r")
        return f.readlines()

    def split(self, word):
        return list(u"{}".format(word.rstrip("\n")))

    def make_page(self, line):
        self.pdf.add_page(orientation='L')
        word_array = self.split(line)

        for c in word_array:
            self.pdf.cell(self.size, self.size, txt=c, border=1, ln=0, align='C')

        self.pdf.ln()

        for _ in range(0, self.num_y_cell):
            for _ in range(0, self.num_x_cell):
                self.pdf.cell(self.size, self.size, border=1, ln=0, align='C')
            self.pdf.ln()


def main():
    new_pdf = asian_character_worksheet_generator()
    lines = new_pdf.read_file()
    for line in lines:
        new_pdf.make_page(line)
    new_pdf.pdf.output("worksheet.pdf")


if __name__ == "__main__":
    main()
