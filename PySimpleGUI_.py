import PySimpleGUI as sg

#exibe todos os temas
# sg.theme_previewer()

#define o tema
sg.theme('Python')

LAYOUT = [
  [sg.Text('Hello World!')],
  [sg.Text('Digite seu nome:'), sg.Input('', key='input', size=(15,0))],
  [sg.Button('CLIQUE')]
]

WINDOW = sg.Window('Título', LAYOUT)

while True:
  events, values = WINDOW.read()
  
  if events == 'CLIQUE':
    sg.popup(f"Bem vindo! {values['input'].title()}")
  
  if events == sg.WINDOW_CLOSED:
    break
  
WINDOW.close()
