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

def kysymys1():
    while aloitus == True:
        vastaus1 = input('Mikä maa voittaa jalkapallon Euroopan-mestarruden vuonna 2021? \na. Suomi \nb. Italia \nc. Tanska \nd. Kanada \nVastaus: ')
        if vastaus1 == 'b':
            Score += 1
            print('Oikein!')
        else:
            print('Väärin! Oikea vastaus oli Italia')
    else:
        break

def kysymys2():
    while aloitus == True:
        vastaus1 = input('Mikä on paras pilvipalvelu? \na. AWS \nb. Azure \nc. Gcloud \nVastaus: ')
        if vastaus1 == 'c':
            Score += 1
            print('Oikein!')
        else:
            print('Väärin! Oikea vastaus oli Italia')
    else:
        break

def tulos():
    print(f'Sait oikein: {score}')

alku()
kysymys1()
kysymys2()
tulos()        

