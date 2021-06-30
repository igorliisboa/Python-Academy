#Baixar vídeos do Youtube

from pytube import YouTube

YouTube("COLOQUE O LINK AQUI").streams.first().download()