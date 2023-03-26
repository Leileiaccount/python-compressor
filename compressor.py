import PySimpleGUI as sg
import zip_creator

text_1 = sg.Text("Select files to compress")
input_1 = sg.Input()
browser_btn_1 = sg.FileBrowse("Choose a file", key="files")
text_2 = sg.Text("Select a directory folder")
input_2 = sg.Input()
browser_btn_2 = sg.FolderBrowse("Choose a folder", key="folder")
compress_button = sg.Button("Compress")
text_3 = sg.Text("", key="complete_message")

layout = [[text_1, input_1, browser_btn_1], [text_2, input_2, browser_btn_2], [compress_button]]

window = sg.Window("File Compressor", layout=layout)

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    des_path = values["folder"]
    zip_creator.zip_creator(filepaths, des_path)
    window["complete_message"].update(values="Completed!!")

window.close()