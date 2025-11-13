from urllib import request
from urllib.error import URLError
lpo =["coño", "bobo", "culiao", "pinche", "estupido", "estupida","disparos"]

def verificar_web(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return ('¡La url ' + url + ' no existe!')
    else:
        aux = f.read()  
        contenido = aux.split()
        palabras_encontradas = []
        cantidad_po = 0
        for l in lpo:
            for c in contenido:
                if l == c.decode():
                    cantidad_po += 1
                    palabras_encontradas.append(l)
        return palabras_encontradas

url = 'https://www.abc.com.py/'
print ("\n---------------------------------------\n")
print("\nInforme de sitio:")
print(verificar_web(url))
