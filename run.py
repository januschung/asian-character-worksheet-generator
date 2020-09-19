from fpdf import FPDF


class asian_character_worksheet_generator():
    pdf = FPDF()
    # Basic settings
    pdf.add_font('fireflysung', '', 'fireflysung.ttf', uni=True)
    pdf.set_font("fireflysung", size=30)
    size = 19
    num_x_cell = 14
    num_y_cell = 8
    file = "text"  # Seed filename; each line should contain the exact number of characters as defined in num_x_cell

    def read_file(self):
        f = open(self.file, "r")
        return f.readlines()

    def split(self, word):
        # turn string into a list of character and strip off the new line character
        return list(u"{}".format(word.rstrip("\n")))

    def make_page(self, line):
        self.pdf.add_page(orientation='L')
        word_array = self.split(line)
        # Reversing character order; In vertical page layout, the character is aligned
        # from right to left
        for c in word_array[::-1]:
            self.pdf.cell(self.size, self.size, txt=c, border=1, ln=0, align='C')

        self.pdf.ln()

        # To print out empty grid
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
