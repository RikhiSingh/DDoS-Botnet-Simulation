'''
This script imports the 'run_gui()' function from the 'gui.py' module located in the 'GUI' folder.

If executed directly (i.e., not imported as a module), it runs the GUI by calling the 'run_gui()' function.

The GUI provides controls for starting and stopping the client and server processes in the botnet, as well 
as displaying information about the purpose of each file.

The 'run_gui()' function initializes the Tkinter window and sets up the layout with buttons and a status label.
'''

from GUI.gui import run_gui

if __name__ == "__main__":
    run_gui()
