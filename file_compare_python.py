import PySimpleGUI as sg
import difflib

def compare_files(file_path_a, file_path_b):
    '''
    Opens both files and checks if they are identical
    '''
    with open(file_path_a, 'r') as file_a, open(file_path_b, 'r') as file_b:
        content_a = file_a.read()
        content_b = file_b.read()

        d = difflib.SequenceMatcher(None, content_a, content_b)
        similarity_percentage = d.ratio() * 100
        similarity_percentage = round(similarity_percentage, 4)

        sg.popup("Similarity Percentage: ", similarity_percentage)

# define the layout of the GUI
layout = [
    [sg.Text("Select First File:")],
    [sg.Input('', key="fileA"), sg.FileBrowse(file_types=(("Python or Text Files", "*.py; *.txt"),))],
    [sg.Text("Select Second File: ")],
    [sg.Input('', key="fileB"), sg.FileBrowse(file_types=(("Python or Text Files", "*.py; *.txt"),))],
    [sg.Button("Check"), sg.Button("Exit")]
]

# create the window
window = sg.Window("File Comparison Checker", layout)

while True:
    # display and interact with window
    event, values = window.read()

    # if user closes window or clicks exit
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    # perform check
    if event == "Check":
        python_file_A = values['fileA']
        python_file_B = values['fileB']
        compare_files(python_file_A, python_file_B)


# close window
window.close()