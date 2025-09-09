import time

number = input("scegli un numero che dovrò indovinare: ")
print("Per favore rispondi a tutte le domande con 'Si' o 'No'")
time.sleep(0.5)
print("Iniziamo!")
time.sleep(0.5)
answer1 = input("Hai almeno un cane? ")
if answer1 != "Si":
    if answer1 != "No":
        print("Risposta non accettabile")
        answer1 = input("Hai almeno un cane? ")

answer2 = input("Sei maggiorenne? ")
if answer2 != "Si":
    if answer2 != "No":
        print("Risposta non accettabile")
        answer2 = input("Sei maggiorenne? ")

answer3 = input("Oggi c'è il sole? ")
if answer3 != "Si":
    if answer3 != "No":
        print("Risposta non accettabile")
        answer3 = input("Oggi c'è il sole? ")

for i in range(0,5):
    time.sleep(0.5)
    print("...")
print("il tuo numero è", number)