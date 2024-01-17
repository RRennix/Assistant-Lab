import windowsapps
a = input('a:')
def app(a):
    a = a.split(' ')
    if a[0].lower() in ['abrir', 'abra', 'abre']:
        a = a[1]
    else:
        a = a[0]
    try:
        
        windowsapps.open_app(a)
    except:
        return
app(a)