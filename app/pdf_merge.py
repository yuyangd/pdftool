from PyPDF2 import PdfFileWriter, PdfFileReader
import pdf_common
import os

class Merge:
    def merge(self, files, path):
        output = PdfFileWriter()
        for filename in files:
            if self.checkfile(filename, path):
                self.append_pdf(PdfFileReader(file(path+filename,"rb")),output)
        try:
            output.write(file(path+"/combined.pdf","wb"))
        except:
            print "Failed to merge"

    def append_pdf(self, input, output):
        try:
            [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]
        except:
            print "append pdf failed"

    def checkfile(self, file, path):
        if os.path.exists(path+file):
            return True
        else:
            return False
