import PySimpleGUI as sg 

# Funkcija, kas izpilda kalk darbības
def darbibas(pampam):
    try:
        result=str(eval(pampam))
        return result
    except:
        return "Kļūda"

# Definēt izkārtojumu
dalas=[
    [sg.Menu([['Faila', ['Iziet']], ['Palīdzība', ['Par']]])],
    [sg.InputText(key='-DISPLAY-', justification='right')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('+')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('*')],
    [sg.Button('0'), sg.Button('C'), sg.Button('='), sg.Button('/')]
]

# veido logs
logs=sg.Window('Kalkulators', dalas, resizable=True)

pampam=''

# galvenais loga cikls

while True:
    notikums, vertiba=logs.read()

    if notikums in (sg.WIN_CLOSED, "Iziet"):
        break
    
    if notikums=='C':
        pampam=''
        logs['-DISPLAY-'].update(pampam)
    elif notikums=="=":
        result=darbibas(pampam)
        logs['-DISPLAY-'].update(pampam)
        pampam=result
    else:
        pampam+=notikums
        logs['-DISPLAY-'].update(pampam)










logs.close()