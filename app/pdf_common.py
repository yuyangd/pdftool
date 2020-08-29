import os.path
import sys
import app
from . import pdf_jpg2pdf
from . import pdf_merge
from cmd import Cmd

class PDFPrompt(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = 'Smart PDF> '


    def cmdloop(self, intro=None):
        Cmd.cmdloop(self, intro)

    def do_quit(self, args):
        '''Quit the app'''
        sys.exit(0)

    def do_convert(self, filename):
        """
        [Syntax]
        convert <filename>    # convert /tmp/sample.jpg
        """
        if filename:
            jpg = pdf_jpg2pdf.JpgPrompt()
            jpg.convert(filename)
        else:
            print("Please specify filename, type 'help' for more info")

    def do_merge(self, args):
        """
        [Syntax]
        merge <path> <filename1> <filename2>
        merge /tmp/ page1.pdf page2.pdf page3.pdf
        """
        if args:
            args = args.split()
            head = args.pop(0)
            if '/' in head:
                path = head
            else:
                print("Please specify the absolute path of the files")
                return false
            mg = pdf_merge.Merge()
            mg.merge(args, path)
        else:
            print("Please specify path and filenames, type 'help' for more info")
