# 1.We need to import this modules for the code can understand what do with the variables that we will pass in the main.py
import os
import yaml
# 2.Then, to search something, there are two ways: on YouTube or DuckDuckGo, we will use a function to do it
def search(a):
    # 2.1.First, if the user pass an order to search on YouTube, we will check it, because "pesquisar" is in "pesquisar no youtube"
    if 'pesquisar no youtube' in a:
        conteudo = a[20:]
        os.startfile('https://www.youtube.com/results?search_query='+conteudo)
        print('Pesquisando por '+conteudo)
    # 2.2.If the last interaction doesn't occur, it will lead to this, when it will search everything that it's after "pesquisar"
    elif 'pesquisar' in a:
        a = a[9:]
        os.startfile('https://duckduckgo.com/?q='+a)
        print('Pesquisando por '+a)
# 3.Other thing that we can do it's open something, that will use a database that we made with searchapp.py
def open(a):
    data = yaml.safe_load(open('path.yml','r',encoding='utf-8').read())
    for Aplicativo in data['Aplicativos']:
        b = Aplicativo['Nome']
        c = Aplicativo['Caminho']
        if b in a:
            os.startfile(c)
            print('Executando '+b)