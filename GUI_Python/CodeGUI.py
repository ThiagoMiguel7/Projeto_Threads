from cProfile import label
from cgitb import text
from turtle import width
from webbrowser import BackgroundBrowser
import pyaudio  
import wave    
import os      
import threading 

from tkinter import * 
import tkinter as tk

app = Tk()

def bateria():

    class WavePlayerLoop(threading.Thread):     

        def __init__(self, filepath, loop=True):      
            super(WavePlayerLoop, self).__init__()    
            self.filepath = os.path.abspath(filepath)   
            self.loop = loop                          

        def run(self):                                 
            CHUNK = 2048  #Tamanho do arquivo de som
            wf = wave.open(self.filepath, 'rb') #Abrir o arquivo
            player = pyaudio.PyAudio() # Lendo o arquivo
            stream = player.open(
                format=player.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True
            )                             
            data = wf.readframes(CHUNK)     
            while self.loop:               
                stream.write(data)          
                data = wf.readframes(CHUNK)
                if data == b'':             
                     wf.rewind()            
                    #self.stop()            
            stream.close()                 
            player.terminate()              

        def play(self):                     
            self.start()                   

        def stop(self):                    
            self.loop = False

    def principal():
        tocar = WavePlayerLoop("DumpsCar.wav")  
        tocar.play()                            
        print('BATERIA')                       

    if __name__ == "__main__":                  
        principal()


def guitarra():

    class WavePlayerLoop(threading.Thread):

        def __init__(self, filepath, loop=True):
            super(WavePlayerLoop, self).__init__()
            self.filepath = os.path.abspath(filepath)
            self.loop = loop

        def run(self):
            CHUNK = 2048
            wf = wave.open(self.filepath, 'rb')
            player = pyaudio.PyAudio()
            stream = player.open(
                format=player.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True
            )
            data = wf.readframes(CHUNK)
            while self.loop:
                stream.write(data)
                data = wf.readframes(CHUNK)
                if data == b'':
                     wf.rewind()
                    #self.stop()
            stream.close()
            player.terminate()

        def play(self):
            self.start()

        def stop(self):
            self.loop = False

    def principal():
        tocar = WavePlayerLoop("GuitarCar.wav")
        tocar.play()
        print('GUITARRA')

    if __name__ == "__main__":
        principal()


def piano():

    class WavePlayerLoop(threading.Thread):

        def __init__(self, filepath, loop=True):
            super(WavePlayerLoop, self).__init__()
            self.filepath = os.path.abspath(filepath)
            self.loop = loop

        def run(self):
            CHUNK = 2048
            wf = wave.open(self.filepath, 'rb')
            player = pyaudio.PyAudio()
            stream = player.open(
                format=player.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True
            )
            data = wf.readframes(CHUNK)
            while self.loop:
                stream.write(data)
                data = wf.readframes(CHUNK)
                if data == b'':
                     wf.rewind()
                    #self.stop()
            stream.close()
            player.terminate()

        def play(self):
            self.start()

        def stop(self):
            self.loop = False

    def principal():
        tocar = WavePlayerLoop("PianoCar.wav")
        tocar.play()
        print('PIANO')

    if __name__ == "__main__":
        principal()


app.title("MCQUEEN BAND")
app.geometry("500x300")
app.configure(background="dark red")



Bateria = Button(app, command=bateria, width=20, height=2,
                 text="BATERIA", relief="flat", fg="White", bg="#121211")
Bateria.grid(row=5, column=0, padx=180, pady=25)

Guitarra = Button(app, command=guitarra, width=20, height=2,
                  text="GUITARRA", relief="flat", fg="White", bg="#121211")
Guitarra.grid(row=10, column=0, padx=180, pady=25)

Piano = Button(app, command=piano, width=20, height=2,
               text="PIANO", relief="flat", fg="White", bg="#121211")
Piano.grid(row=15, column=0, padx=180, pady=25)

app.mainloop()
