import PyPDF2


def split_pdf(input_path, output_path):
    # Open the PDF file in binary mode
    with open(input_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Iterate through pages and save each page as a separate PDF file
        for page_number in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()

            pdf_writer.add_page(pdf_reader.pages[page_number])

            output_file = f"{output_path}/{page_number + 1}.pdf"
            with open(output_file, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)


if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your input PDF file
    input_pdf_path = 'path/to/input/file'

    # Replace 'output_folder' with the path to the folder where you want to save the individual PDFs
    output_folder_path = 'path/to/output/directory'

    split_pdf(input_pdf_path, output_folder_path)
