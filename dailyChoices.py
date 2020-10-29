#keuzes


vraag1 = "1. wat doe je als de wekker afgaat, zet je de wekker UIT of blijf je SLAPEN?\nA. blijven slapen\nB. uit doen "
vraag2 = "2.Ga je ontbijten of gelijk achter de comuter zitten?\nA. ontbijten\nB. computer"
vraag3 = "3.Ga je eerst huiswerk maken of gamen?\nA. huiswerk\nB. gamen"
vraag4 = "4.Welke game ga je spelen?\nA. Call of Duty black ops\nB. Ark survival"
vraag5 = "5.Welke anime ga je kijken?\nA.My hero academia\nB. The promised neverland"

#-------------------------------------------------------------------------------
print("wat doe je als de wekker afgaat, zet je de wekker UIT of blijf je SLAPEN? ")

#-------------------------------------------------------------------------------
print(vraag1)

keuze = input()

if keuze == "A" or keuze == "a":
    print(" je slaapt gewoon door als de wekker gaat (ik slaap elke dag minimaal door 14 wekkers heen).")
    
elif keuze == "B" or keuze == "b":
    print("Je doet de wekker uit")

else:
    print("Je kan alleen maar kiezen uit a of b")

#-------------------------------------------------------------------------------
print("")

print(vraag2)

keuze2 = input()

if keuze2 == "A" or keuze2 == "a":
    print("Je neemt eerst onbijt voordat je achter de computer gaat.")

elif keuze2 == "B" or keuze2 == "b":
    print("je gaat gelijk uit je bed op je computer")

else:
    print("je kan alleen maar kiezen tussen a of b.")
#-------------------------------------------------------------------------------
print("")

print(vraag3)

keuze3 = input()

if keuze3 == "A" or keuze3 == "a":
    print("je gaat eerst je huiswerk maken")

elif keuze3 == "B" or keuze3 == "b":
    print("Gamen vindt je toch even wat belangrijker dus je doet dat eerst.")

else:
    print("Je kan alleen maar kiezen tussen a of b")
#-------------------------------------------------------------------------------
print("")

print(vraag4)

keuze4 = input()

if keuze4 == "A" or keuze4 == "a":
    print("Je start gelijk de game Call of duty op")

elif keuze4 == "B" or keuze4 == "b":
    print("Je start de game Ark survival op")

else:
    print("Je kan alleen maar kiezen uit a of b")

#-------------------------------------------------------------------------------
print("")

print(vraag5)

keuze5 = input()

if keuze5 == "A" or keuze5 == "a":
    print("Je gaat kijken naar My hero academia(aanrader!!!!!!)")

elif keuze5 == "B" or keuze5 == "b":
    print("Je gaat The promised nevrland kijekn(ooook zeker een aanrader)")

else:
    print("Je kan alleen maar kiezen tussen a of b")
#-------------------------------------------------------------------------------
