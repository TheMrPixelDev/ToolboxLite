import sys
import os
import youtube_dl
import pdf_tools
import excel_tools
from dialog import Dialog

def mainDialog():

    os.system('cls')

    print("""\n  ______            ____               __    _ __     
 /_  __/___  ____  / / /_  ____  _  __/ /   (_) /____ 
  / / / __ \/ __ \/ / __ \/ __ \| |/_/ /   / / __/ _ \\
 / / / /_/ / /_/ / / /_/ / /_/ />  </ /___/ / /_/  __/
/_/  \____/\____/_/_.___/\____/_/|_/_____/_/\__/\___/ 
""")

    main_dialog = Dialog("Welcome to ToolboxLite! Down below are listed some tools which might be helpful:")
    main_dialog.setOptions(("PDF-Tools",pdf_tools.pdf_functions_dialog),("Excel-Tools",excel_tools.excel_functionctions_dialog),("Youtube-dl",youtube_dl.youtube_dl_dialog),("Exit program",sys.exit))
    main_dialog.show()

if __name__ == "__main__":
    mainDialog()