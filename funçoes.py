# 1.We need to import this modules for the code can understand what do with the variables that we will pass in the main.py
import os
import windowsapps
# 2.Then, to search something, there are two ways: on YouTube or DuckDuckGo, we will use a function to do it
def search(a):
    a = a.split(' ')
    if a[0].lower() == 'pesquisar':
        if 'youtube' in a:
            a = ' '.join(a[int(a.index('youtube'))+1:])
            os.startfile('https://www.youtube.com/results?search_query='+a)
        else:
            a = ' '.join(a[int(a.index('pesquisar'))+1:])
            os.startfile('https://www.google.com/search?q='+a)
    else:
        return
# 3.Other thing that we can do it's open something, that will use a database that we made with searchapp.py
def open(a):
    a = a.split(' ')
    if a[0].lower() in ['abrir', 'abra', 'abre']:
        a = a[1]
    else:
        a = a[0]
    try:
        print(a)
        windowsapps.open_app(a)
    except:
        return