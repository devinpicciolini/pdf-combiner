import PyPDF2
import os

# Define the directory containing the PDF files
pdf_dir = '/Users/devin/develop/pdf-combiner/data'

# Check if the directory exists
if not os.path.exists(pdf_dir):
    print(f"Directory {pdf_dir} does not exist.")
    exit(1)

# Get a list of all PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# Sort the PDF files by name
pdf_files.sort()

# Create a PDF merger object
pdf_merger = PyPDF2.PdfMerger()

# Loop through all the PDF files and append them to the merger
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    pdf_merger.append(pdf_path)

# Define the full path for the output file, including the filename
output_path = '/Users/devin/develop/pdf-combiner/combined.pdf'

# Write the combined PDF to a new file
with open(output_path, 'wb') as output_pdf:
    pdf_merger.write(output_pdf)

print(f"Combined PDF saved as {output_path}")
