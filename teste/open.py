import windowsapps
while True:
    name = input('Nome:')
    try:
        windowsapps.open_app(name)
    #Will search for the application APPLICATION NAME and open it.
    except:
        print("Can't find")