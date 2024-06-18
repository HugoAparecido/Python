oi=0
while True:
    try:
        print("Hello World")
        if(oi==5):
            break
        oi=5
    except EOFError:
        break
