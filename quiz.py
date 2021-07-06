
def tietovisa():
    
    while True:
        aloitus = input("Haluatko pelata? (y/n)")
        # If you play more than one round the game returns the overall score of all the rounds that you have played. I have replaced the score variable. It returns the score of the current round if you place it within the first while loop.
        if aloitus[0].lower() == "y":
            #If you write aloitus[0].lower(), you can eliminate some possible mistakes. Even if the player writes an uppercase letter or writes eg. yes or no, your game will still run.
            jatko = True

        elif aloitus[0].lower() == "n":
            jatko = False
            return False
            
        else:
            print("Valitse y/n")
            continue
        
        score = 0
        while jatko:
            #You can simply write vastaus. As you do not have vastaus2 as a variable, you can just erase the number.
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
                jatko = False
            else:
                print('Väärin! Oikea vastaus oli Italia')              
                jatko = False
        
        # You dont need to write this line twice. You can do the print after both while loops are over.
        print(f'Sait oikein: {score}')
        
# Some general ideas:
#Nicely written code, it was easy to read and follow :)
# You can break down the game into more functions. Eg. the first while loop can be one function which returns a boolean. Then you can push this boolean into another function which executes the gameplay itself.
#Let me share my logic... we used it to reduce the number of the lines in the code :P
# If you save the questions and the answers into a dictionary for example, you dont need to write all the rounds separately. You can use a for loop to iterate through the dictionary. Then you dont need to write the same while loop over and over again plus you can add new questions and answers easily.

tietovisa()