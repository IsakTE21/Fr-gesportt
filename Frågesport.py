name = input("Hej och välkommen till denna frågesport, vad heter du? ")


instructions = input("Här kommer instruktionerna (tryck på enter för att fortsätta)")

instructions = input("Korrekt svar ger dig 1 poäng")

instructions = input("Du har totalt tre chanser på dig att svara rätt på en fråga")

instructions = input(" Om du svarar fel alla 3 gånger får du inget poäng")

instructions = input("VIKTIGT- skriv svaret och inte bokstaven på frågorna med svarsalternativ.")


print("Lycka till", name,)

score = 0

print("Startpoäng: ", score,".")

print("Fråga 1:")

tries = 0

while True:
    answer1 = input("Vilken är Sveriges största ö?\nA. Värmdö\nB. Orust\nC. Gotland\nD. Öland\n Svar: ").capitalize()

    tries += 1
    
    if answer1 == "Gotland":
        score +=1
        break
        
    else:
        print("Fel svar, var vänlig försök igen")

    if tries == 3:
        print("Du klarade tyvärr inte av denna fråga och får därmed inga poäng")
        break

print("Bra jobbat", name, ", du har nu", score, "poäng!")


    

print("Fråga 2:")

tries = 0

while True:
    
    answer2 = input("Vilken är Sveriges huvudstad\nA. Örebro\nB. Stockholm\nC. Uppsala\nD.Göteborg\nSvar: ").capitalize()
   
    tries +=1
    
    if answer2 == "Stockholm":
        score +=1 
        break

    else: 
        print("Fel svar, var vänlig och försök igen")
    
    if tries == 3:
        print("Du klarade tyvärr inte av denna fråga och får därmed inga poäng")
        break
    
print("Rätt svar, bra jobbat!")
print("Din totala poäng är nu", score," poäng.")
  

while True:
    
    answer3 = input("Hur många landskap finns det i Sverige?\nA. 15\nB. 25\nC. 35\nD.20\nSvar: ").capitalize()
   
    tries +=1
    
    if answer3 == "25":
        score +=1 
        break

    else: 
        print("Fel svar, var vänlig och försök igen")
    
    if tries == 3:
        print("Du klarade tyvärr inte av denna fråga och får därmed inga poäng")
        break



while True:
    
    answer4 = input("Hur många städer finns det i Sverige?\nA. 1979\nB. 582\nC. 167\nD.1670\nSvar: ").capitalize()
   
    tries +=1
    
    if answer4 == "1979":
        score +=1 
        break

    else: 
        print("Fel svar, var vänlig och försök igen")
    
    if tries == 3:
        print("Du klarade tyvärr inte av denna fråga och får därmed inga poäng")
        break



print("Gratulerar, du slutförde frågesporten med", score,"poäng")

print("Tack för att du spelade.")
