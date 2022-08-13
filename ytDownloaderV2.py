from contextlib import nullcontext
import PySimpleGUI as sg
from pytube import YouTube


layout = [[sg.Text("Insert your link here")],
          [sg.Input('-', key='-INPUT-', do_not_clear=False)],
          [sg.Text(size=(40,3), key='-OUTPUT-')],
          [sg.Button('Video'), sg.Button('Audio'), sg.Button('Exit')]]

window = sg.Window('PyTube Downloader', layout)

while True:
    event, values = window.read()
    
    if event == 'Exit':
        window.close()
        break

    else:
        yt = YouTube(values['-INPUT-'])

        if  event == 'Audio':
            window['-OUTPUT-'].update( "Downloaded: "+ "\n" + yt.title + "\nEnjoy your audio!")
            stream = yt.streams.get_audio_only()

        elif event == 'Video':
            window['-OUTPUT-'].update( "Downloaded: "+ "\n" + yt.title + "\n Enjoy your video!")
            stream = yt.streams.get_highest_resolution()
        
        stream.download('')

            
        
