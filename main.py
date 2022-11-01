import requests
import sys

lista = []
wordlist = open('wordlist','r')
for word in wordlist:
    lista.append(word.replace('\n',''))

def ciclo():
    global url
    request = requests.get(url)
    for word in lista:
            if request.ok:
                text = request.text
                word=word.replace('\n','')
                if word in text:
                    print('FIND: ',word)
                    print('IN  : ',url)
                    print('')

pages = open('pages','r')

def pages_find():
    global url
    cp2_url = url
    prova = True
    request = requests.get(url)
    text = request.text
    if 'Parent Directory' in text:
                    if prova:
                        text = text.split()
                        for line in text:
                            if '.html' in line or '.js' in line or ('href="' in line and '/' in line and 'Name' not in line and 'Size' not in line and 'Description' not in line and '"/"' not in line and '.png' not in line):
                                file = line[6:line.rindex('"')]
                                if file[-1] == '/':
                                    url = url+'/'+file[0:-1]
                                    pages_find()
                                    url = cp2_url
                                else:
                                    url = url+'/'+file
                                    ciclo()
                                    url = cp2_url
                                prova = False
    else:
        if word in text:
            print('FIND: ',word)
            print('IN  : ',url)
            print('')



try:
    url = sys.argv[1]
    request = requests.get(url)
    cp_url=url

    ciclo()
    for page in pages:
        url = cp_url
        page = page.split()
        page = page[0]
        url = url + str(page)

        print('-----------------------------------\n')
        request = requests.get(url)
        prova = True
        for word in lista:
            if request.ok:
                text = request.text
                word=word.replace('\n','')
                if 'Parent Directory' in text:
                    if prova:    
                        text = text.split()
                        for line in text:
                            cp2_url = url
                            if '.html' in line or '.js' in line or ('href="' in line and '/' in line and 'Name' not in line and 'Size' not in line and 'Description' not in line and '"/"' not in line and '.png' not in line):
                                file = line[6:line.rindex('"')]
                                if file[-1] == '/':
                                    url = url+'/'+file[0:-1]
                                    pages_find()
                                    url = cp2_url
                                else:
                                    url = url+'/'+file
                                    ciclo()
                                    url = cp2_url
                                prova = False

                else:
                    if word in text:
                        print('FIND: ',word)
                        print('IN  : ',url)
                        print('')



except:
    print("Don't connect, sorry!")
