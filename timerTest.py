import threading


def foo():
    print("hola Diego")
def looper():    
    # i as interval in seconds    
    threading.Timer(1, looper).start()    
    # put your action here
    foo()

#to start 
looper()