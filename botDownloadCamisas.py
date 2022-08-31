from importlib.resources import path
import requests
from bs4 import BeautifulSoup
import os
import unidecode
from tqdm import tqdm




with open("blocoDeNotas.txt", "r") as bloco :
    # bloco de notas com o formato certo na mesma pasta 
   linksCamisas = bloco.readlines()
   for camisa in linksCamisas:
    camisa = camisa.rstrip('\n')
    urlPrincipal = camisa
    
    r = requests.get(urlPrincipal)
    soup = BeautifulSoup(r.content, 'html.parser')
    imgs = soup.find_all('div')

   
    
    for img in imgs:
        
            idCamiseta = img.attrs.get('data-id')
            
            if idCamiseta is not None:
                nomeCamisa = r"Camisas" + idCamiseta[idCamiseta.rfind('/'):]
                
                image = "https://royal-sports.x.yupoo.com" + "/" + idCamiseta + "?uid=1"

    for nome in soup.find_all('title'):
        nomeCamisaCerto = nome.get_text()
        removendoLetras = unidecode.unidecode(nomeCamisaCerto)
        removendoLetras = removendoLetras.replace('You Pai Tu Pian Guan Jia', '')
        removendoLetras = removendoLetras.replace('/', '-')
        removendoLetras = removendoLetras.replace('|', '')
        removendoLetras = removendoLetras.replace('.', '')

        path = removendoLetras

        if not os.path.exists(path):
            os.mkdir(path)
           


        r02 = requests.get(image)
        soup02 = BeautifulSoup(r02.content, 'html.parser')
        imgs02 = soup.find_all('img')

        def get_photos(url):
                    
                with requests.Session() as c:
                    c.get(url)
                    c.headers.update({'referer': url})
                    res = c.get(camisaCerta)
                    if res.status_code == 200:
                        return res.content

        for img in tqdm(imgs02):
                    camisaD = img.attrs.get('data-origin-src')

                    if camisaD is not None:
                        nomeCamisa = r"Camisas" + camisaD[camisaD.rfind('/'):]
                        novoNome = nomeCamisa.replace('Camisas', path)
                        
                        testemaluco = novoNome.replace('   ', '')
                        # print(testemaluco)
                        camisaCerta = 'http:' + camisaD
                            
                        with open(testemaluco, 'wb') as f:
                             f.write(get_photos(camisaCerta))
                            
                            
        print("Download Camisa " + removendoLetras + " finalizada !")

    # # bloco.close()

PASTA_ATUAL = 'D:\oGabriel\Gabe.art\LOJAS\SONECANCIA\CAMISAS BAIXADAS'
totalFiles = 0
totalDir = 0
for base, dirs, files in os.walk(PASTA_ATUAL):
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1
        
print("Total de" ,totalDir ,"Times criados, " + "com total de",totalFiles -6,"Camisas !")

