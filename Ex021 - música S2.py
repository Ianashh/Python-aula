import pygame as pg
pg.mixer.init()
pg.init()
pg.mixer.music.load('ex021py.mp3')
pg.mixer.music.play()
pg.mixer.music.set_volume(2)
x = input('Digite algo para encerrar a música: ')
print(x.upper())
print(x.__len__())
print(x.find('som'))

print('fim')
