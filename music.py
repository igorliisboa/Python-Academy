#Tocar músicas

from pygame import mixer

#Coloque o nome do arquivo aqui
file = "......." '''<----COLOQUE O CAMINHO DA MÚSICA AQUI'''

mixer.init()
mixer.music.load(file)
mixer.music.play()