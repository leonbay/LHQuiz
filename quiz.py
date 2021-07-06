score = 0
def alku():
    while True:
        aloitus = input("Haluatko pelata? (y/n)")
        if aloitus == "y":
            return True
            break
        elif aloitus == "n":
            return False
            break
        else:
            print("Valitse y/n")
            continue

alku()
        

        
def tulos():
    print(f'Sait oikein: {score}')