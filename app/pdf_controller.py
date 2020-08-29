import time
from . import pdf_common
from pyfiglet import Figlet


class PDFController(object):
    def main(self):
        f = Figlet(font='slant')
        msg = f.renderText("Smart PDF")
        Welcome = 'Welcome to Smart PDF Terminal, type "help" for commands.'
        prompt = pdf_common.PDFPrompt()
        prompt.cmdloop(msg+Welcome)

        
