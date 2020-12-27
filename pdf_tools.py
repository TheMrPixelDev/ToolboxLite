from tkinter import filedialog, Tk
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from dialog import Dialog

pdf_tools = ["PDF-Merging", "PDF-Encrypting", "<-- Back"]

def pdf_mergin():

    dest_file_name = str(input("Enter name for destination file: "))
    print("Select the files you want to merge using the filedialog...")
    root = Tk()
    input_files = filedialog.askopenfilenames(parent=root, title="Chose the PDFs")
    pdf_writer = PdfFileWriter()

    for file in root.tk.splitlist(input_files):
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    print("PDFs have been merged...")
    with open(dest_file_name,'wb') as out:
        pdf_writer.write(out)
        print("PDF file has been created...")

def pdf_encryption():

    filename = filedialog.askopenfile().name
    
    if filename.endswith('.pdf'):
        filename = filename[:-4]
    else:
        print("The file you chose is not a PDF")
        pdf_encryption()

    pdf_reader = PdfFileReader(filename+".pdf")
    pdf_writer = PdfFileWriter()
    password = str(input("Enter a password for your PDF: "))

    for page in range(pdf_reader.getNumPages()):    
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password,use_128bit=True)
    print("Your file is being encrypted, please wait...")

    with open(filename+".encrypted.pdf", 'wb') as out:
        pdf_writer.write(out)
    
    print(f"File has successfully been encryted and stored as: {filename+'.encrypted.pdf'}")


def pdf_functions_dialog():
    
    from main import mainDialog

    os.system('cls')

    pdf_f_dialog = Dialog("Which PDF related tool do you want to use?")
    pdf_f_dialog.setOptions(("PDF-Merging",pdf_mergin),("PDF-Encrypting",pdf_encryption),("<-- Back", mainDialog))
    pdf_f_dialog.show()

    

    