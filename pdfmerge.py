import PyPDF2
import sys

def pdfMerge(pdf_list):
    merge = PyPDF2.PdfFileMerger() #creates a merger object
    for pdf in pdf_list:
        print(pdf)
        merge.append(pdf) #merge object acts lile a list
    merge.write("combinedPDF")

def main():
    inputs = sys.argv[1:] #this allows any number of terminal arguments and puts into list
    pdfMerge(inputs)

if __name__ == "__main__":
    main()