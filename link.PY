#Encurtador de links

import pyshorteners as ps

url = "........" '''<----COLOQUE A URL AQUI'''
u = ps.Shortener().tinyurl.short(url)

print(u)