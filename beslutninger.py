#Oppgave 3: Beslutninger

#Variabelen settes til å hete brus. Variabelen ber bruker om å
#svare ja eller nei på et spørsmål. Hvis brukeren svarer ja
#printes det "Her har du en brus!". Hvis bruker taster nei printes
#det "Den er grei." Hvis bruker taster ingenting eller noe annet
#enn ja eller nei, printes det "Det forsod jeg ikke helt."
brus=input("Kunne du tenkt deg en brus? Svar ja/nei:")
if brus == "ja":
    print("Her har du en brus!")
elif brus == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")
