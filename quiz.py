
def tietovisa():
    score = 0
    while True:
        aloitus = input("Haluatko pelata? (y/n)")
        if aloitus == "y":
            jatko = True

        elif aloitus == "n":
            jatko = False
            return False
            
        else:
            print("Valitse y/n")
            continue
    
        while jatko:
            vastaus1 = input('Mikä maa voittaa jalkapallon Euroopan-mestarruden vuonna 2021? \na. Suomi \nb. Italia \nc. Tanska \nd. Kanada \nVastaus: ')
            if vastaus1 == 'b':
                score += 1
                print('Oikein!')
                break
                
            else:
                print('Väärin! Oikea vastaus oli Italia')
                break
                
    

        while jatko:
            vastaus1 = input('Mikä on paras pilvipalvelu? \na. AWS \nb. Azure \nc. Gcloud \nVastaus: ')
            if vastaus1 == 'c':
                score += 1
                print('Oikein!')
                print(f'Sait oikein: {score}')
                jatko = False
            else:
                print('Väärin! Oikea vastaus oli Italia')
                print(f'Sait oikein: {score}')
                jatko = False
        
            

tietovisa()