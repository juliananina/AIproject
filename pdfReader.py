# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:45:05 2024

@author: Harjot
"""


import pdfplumber

def extract_text_from_pdf(pdf_path, txt_output_path):
    # Open the PDF file using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Create or open the output text file in write mode
        with open(txt_output_path, 'w', encoding='utf-8') as output_file:
            # Iterate through all the pages in the PDF
            for page_num, page in enumerate(pdf.pages):
                # Extract text from each page
                text = page.extract_text()
                if text:
                    output_file.write(f"Page {page_num + 1}:\n")
                    output_file.write(text)
                    output_file.write("\n\n")  # Add extra newline between pages
                else:
                    output_file.write(f"Page {page_num + 1}: No text found\n")
                    output_file.write("\n\n")
                
    print(f"Text extraction complete. The output is saved to: {txt_output_path}")


# Specify the input PDF path and output text file path


# Run the function to extract text and save it to a text file
for number in range(1, 71):
    pdf_path = str(number) + ".pdf"  # Replace with your PDF file path
    txt_output_path = "outputfiles/"+ str(number)+".txt"  # Replace with your desired output file path
    extract_text_from_pdf(pdf_path, txt_output_path)

