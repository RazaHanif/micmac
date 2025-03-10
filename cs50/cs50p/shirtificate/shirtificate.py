from fpdf import FPDF
from PIL import Image


def main():
    # Get name from user
    name = input("Name: ").strip().capitalize()

    # Create PDF page and add CS50 Header (not using class header way)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(
        w=190, h=50, txt="CS50 Shirtificate",
        new_x="CENTER", new_y="TOP", align="C"
    )

    # Add shirt png to picture
    with Image.open("shirtificate.png") as im:
        pdf.image(im, x="C", y=50)

    # change text to smaller size and change color to white, add user name
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(
        w=50, h=250, txt=name,
        align="X", new_y="LAST",
    )

    # save file in correct format
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
