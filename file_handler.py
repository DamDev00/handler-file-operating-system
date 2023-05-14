import time
from tkinter import *
import os
import random
import string as dg
#import pkg_resources.py2_warn


if __name__ == '__main__':
    class File:
        def __init__(self):
            pass
        def crea_percorso(self):
            desk = os.getcwd()
            size = desk.find('Desktop')
            n_desk = 7
            desk = os.getcwd()[:size + n_desk]
            desk = desk.replace('\\', '/')
            return desk
        def crea_cartella(self):
            opzione = -1
            while opzione != 0:
                print('scegli il percorso del file\n')
                print('1) desktop')
                print('2) inserisci una cartella dove inserirlo')
                opzione = int(input('>: '))
                if(opzione == 1):
                    desk = self.crea_percorso()
                    cartella = str(input('inserisci il nome della cartella: '))
                    time.sleep(3)
                    nuova_cartella = desk + '/' + cartella
                    if(os.path.exists(nuova_cartella)):
                        print('cartella nel desktop esistente')
                    else: 
                        os.makedirs(nuova_cartella)
                    opzione = 0
                elif(opzione == 2):
                    cartella_esistente = str(input('inserisci il nome della cartella esistente: '))
                    percorso = self.crea_percorso() + '/' + cartella_esistente
                    cartella_da_inserire = str(input('inserisci la cartella da inserire: '))
                    if(os.path.exists(percorso + '/' + cartella_da_inserire)):
                        print(f'cartella esistente nel percorso {percorso}')
                    else:
                        os.makedirs(percorso + '/' + cartella_da_inserire)
        def crea_file(self):
            print('1) aggiungi il file nel desktop')
            print('2) aggiungi il file in una cartella')
            opzione = int(input('>: '))
            if(opzione == 1):
                nome_file = str(input('inserisci il nome del file: '))
                estensione = '.txt'
                percorso = self.crea_percorso()
                if(os.path.exists(percorso + '/' + nome_file + estensione)):
                    print('file esistente')
                else:
                    f = open(percorso + '/' + nome_file + estensione, 'x')
                opzione = 0
            elif(opzione == 2):
                percorso = self.crea_percorso()
                risposta = True
                while risposta:
                    cartella = str(input('inserisci il nome della cartella: '))
                    percorso+='/'
                    percorso+=cartella
                    r = str(input('concatenare la cartella? (si/no) >: '))
                    if(r in ('s', 'si')):
                        None
                    elif(r in ('n', 'no')):
                        risposta = False
                nome_file = str(input('inserisci il nome del file: '))
                estensione = '.txt'
                if(os.path.exists(percorso + '/' + nome_file + estensione)):
                    print('file esistente')
                else:
                    f = open(percorso + '/' + nome_file + estensione, 'x')
        def rimuovi_file(self):
            opzione = -1
            print('1) file presente nel desktop')
            print('2) file presente in una cartella')
            opzione = int(input('>: '))
            if(opzione == 2):
                percorso = self.crea_percorso()
                risposta = True
                while risposta:
                    cartella = str(input('inserisci il nome della cartella: '))
                    percorso+='/'
                    percorso+=cartella
                    r = str(input('concatenare la cartella? (si/no) >: '))
                    if(r in ('s', 'si')):
                        None
                    elif(r in ('n', 'no')):
                        risposta = False
                nome_file = str(input('inserisci il nome del file: '))
                estensione = str(input('estensione del file: '))
                if(os.path.exists(percorso + '/' + nome_file + '.' + estensione)):
                    os.remove(percorso + '/' + nome_file + '.' + estensione)
                else:
                    print('file non esistente')
            elif(opzione == 1):
                percorso = self.crea_percorso()
                nome_file = str(input('inserisci il nome del file: '))
                estensione = str(input('estensione del file: '))
                if(os.path.exists(percorso + '/' + nome_file + '.' + estensione)):
                    os.remove(percorso + '/' + nome_file + '.' + estensione)
                else:
                    print('file non esistente')
            opzione = 0
        def opzioni_file(self):
            opzione = -1
            print('1) file presente nel desktop')
            print('2) file presente in una cartella')
            opzione = int(input('>: '))
            if(opzione == 2):
                percorso = self.crea_percorso()
                risposta = True
                while risposta:
                    cartella = str(input('inserisci il nome della cartella: '))
                    percorso+='/'
                    percorso+=cartella
                    r = str(input('concatenare la cartella? (si/no) >: '))
                    if(r in ('s', 'si')):
                        None
                    elif(r in ('n', 'no')):
                        risposta = False
                        nome_file = str(input('inserisci il nome del file: '))
                        estensione = str(input('estensione del file: '))
                if(os.path.exists(percorso + '/' + nome_file + '.' + estensione)):
                    print('r -> leggi il file')
                    print('w -> scrivi nel file')
                    c = str(input('>: '))
                    if(c == 'r'):
                        f = open(percorso + '/' + nome_file + '.' + estensione, 'r')
                        print(f.read())
                        f.close()
                    elif(c == 'w'):
                        f = open(percorso + '/' + nome_file + '.' + estensione, 'w')
                        stringa = str(input('inserisci il contenuto del file (termine al click invio): '))
                        f.write(stringa)
                        f.close()
                else:
                    print('file non esistente')
            elif(opzione == 1):
                percorso = self.crea_percorso()
                nome_file = str(input('inserisci il nome del file: '))
                estensione = str(input('estensione del file: '))
                if(os.path.exists(percorso + '/' + nome_file + '.' + estensione)):
                    print('r -> leggi il file')
                    print('w -> scrivi nel file')
                    c = str(input('>: '))
                    if(c == 'r'):
                        f = open(percorso + '/' + nome_file + '.' + estensione, 'r')
                        print(f.read())
                        f.close()
                    elif(c == 'w'):
                        f = open(percorso + '/' + nome_file + '.' + estensione, 'w')
                        f.write()
                        f.close()
                else:
                    print('file non esistente')
            opzione = 0
        def rimuovi_cartella(self):
            percorso = self.crea_percorso()
            print('1) rimuovere cartella nel desktop')
            print('2) rimuovere cartella dentro un\'altra cartella')
            stato = True
            opzione = int(input('>: '))
            if(opzione == 1):
                nome_cartella = str(input('inserisci il nome della cartella: '))
                if(os.path.exists(percorso + '/' + nome_cartella)):
                    os.removedirs(percorso + '/' + nome_cartella)
                else:
                    print('file non esistente')
            elif(opzione == 2):
                stato = True
                while stato:
                    cartella = str(input('inserisci il nome della cartella: '))
                    percorso+='/'
                    percorso+=cartella
                    c = str(input('vuoi concatenare la cartella?(si/no)'))
                    if(c in ('s', 'si')):
                        None
                    elif(c in ('n', 'no')):
                        stato = False
                        if(os.path.exists(percorso)):
                            os.removedirs(percorso)
                        else:
                            print('cartella non esistente')

            
f = File()
opzione = -1
while opzione != 0:
    print('1) crea cartella')
    print('2) crea file')
    print('3) rimuovi file')
    print('4) opzioni file')
    print('5) rimuovi cartella')
    opzione = int(input('>: '))
    if(opzione == 1):
        f.crea_cartella()
    elif(opzione == 2):
        f.crea_file()
    elif(opzione == 3):
        f.rimuovi_file()
    elif(opzione == 4):
        f.opzioni_file()
    elif(opzione == 5):
        f.rimuovi_cartella()
    else:
        None
            

        """
def Crea_cartella():
    f = File()
    f.crea_cartella()


root.geometry('300x300')
root.config(bg='white')
titolo = Label(
    fg='black',
    font=('Times New Roman', 15),
    text='Gestisci i tuoi file',
    width=13,
    bg='white',
    pady=5
)
button1 = Button(
    text='Crea cartella',
    fg='black',
    font=('Times New Roman', 8),
    command=lambda: Crea_cartella()
)
inp = Entry(
    fg='black',
    font=('Times New Roman', 10),

)

titolo.grid(row=0, column=2)
inp.grid(row=2, column=2)
button1.grid(row=3, column=1)

root.mainloop()
            """