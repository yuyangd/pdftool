import PIL
import PIL.Image
import app
import os


class JpgPrompt:
    """This class is to convert jpg to pdf"""
    def convert(self, filename):
        try:
            im = PIL.Image.open(filename)
            outfilename = self.get_basename(filename)+'.pdf'
            outfile = os.path.dirname(filename)+'/'+outfilename
            im.save(outfile, format='PDF', resoultion = 100.0)
            print "File converted"
        except:
            print "Failed to convert the file"

    def get_basename(self, filename):
        name = os.path.basename(filename)
        return os.path.splitext(name)[0]

