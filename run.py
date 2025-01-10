from fpdf import FPDF
from fpdf.enums import XPos, YPos


class asian_character_worksheet_generator():
    pdf = FPDF()
    # Basic settings
    pdf.add_font('noto-serif-cjk', '', 'NotoSerifCJK-Regular.ttc')
    pdf.set_font("noto-serif-cjk", size=30)
    size = 19
    num_x_cell = 14
    num_y_cell = 8
    file = "text"  # Seed filename; each line should contain the exact number of characters as defined in num_x_cell

    def read_file(self):
        with open(self.file, "r") as f:
            return f.readlines()

    def split(self, word):
        # turn string into a list of character and strip off the new line character
        return list(u"{}".format(word.rstrip("\n")))
    
    def add_cell(self, text=""):
        self.pdf.cell(self.size, self.size, text=text, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')

    def make_page(self, line):
        self.pdf.add_page(orientation='L')
        word_array = self.split(line)
        # Reversing character order; In vertical page layout, the character is aligned
        # from right to left
        for c in word_array[::-1]:
            self.add_cell(c)
        self.pdf.ln()

        # To print out empty grid
        for _ in range(0, self.num_y_cell):
            for _ in range(0, self.num_x_cell):
                self.add_cell()
            self.pdf.ln()


    def save_pdf(self, output_file):
        self.pdf.output(output_file)


def main():
    new_pdf = asian_character_worksheet_generator()
    lines = new_pdf.read_file()
    for line in lines:
        new_pdf.make_page(line)
    new_pdf.save_pdf("worksheet.pdf")


if __name__ == "__main__":
    main()
