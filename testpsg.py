import PySimpleGUI as sg 
import pandas as pd 
import os 


###select the folder, if none, display a system message and close, if yes, display a system message to show the path , click ok to close the program ###
# dir_path = sg.popup_get_folder('select folder')
# if not dir_path:
#     sg.popup('Cancel', 'No folder selected')
#     raise SystemExit('Cancelling: no folder selected')
# else: 
#     sg. popup('The folder you chose was', dir_path)


###select the csv file, if none, display a system message and close, if yes, display a system message to show the path , click ok to close the program ###
# fname = sg.popup_get_file('Choose csv file', multiple_files=False, file_types=(('csv','*.csv'),),)
# if not fname:
#     sg.popup('Cancel', 'no filename here')
#     raise SystemExit('Cancel: no file name is given')
# else:
#     sg.popup('The filename was ', fname)

###select the date, if none, display a system message and close, if yes, display a system message to show the path , click ok to close the program ###
# date = sg.popup_get_date()
# if not date:
#     sg.popup('Cancel', 'No date picked')
#     raise SystemExit('Cancelling: no date selected')
# else:
#     sg.popup('The date you picked is: ', date)

###input some text, if none, display a system message and close, if yes, display a system message to show the path , click ok to close the program ###
# text = sg.popup_get_text("Please enter a text: ")
# if not text:
#     sg.popup("Cancel", 'No text was entered')
#     raise SystemExit("Cancelling: no text was putting down")
# else:
#     sg.popup("You have entered: ", text)

###status notification###
# sg.popup_notify('Great')

#backend, data source locating the current python execute file
exefile_path = os.path.realpath(__file__)
#backend, data source locating the data file folder, 'pybkp'
pybkp_path = os.path.realpath(f"{os.path.dirname(exefile_path)}/pybkp")

print(pybkp_path)

#theme
sg.theme('Dark Blue')

#layout structure
layout = [
[sg.Input(key='input'), sg.FileBrowse('data')],
[sg.Button('Submit'), sg.Button('Reset')],
[sg.Button('Exit')],
[sg.Output(key='Output')]
]

window = sg.Window('Window Title', layout)

#event loops
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        # change the 'output' element to be the value of 'data'
        window['Output'].update(pd.read_csv(values['data']))


window.close()
