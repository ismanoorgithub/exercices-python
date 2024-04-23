moyenne = float(input("Veuillez entrer votre moyennne: "))

if 12 <= moyenne <14:
    print("Vous avez obtenu la mention Assez Bien.")
elif 14 <= moyenne <16:
    print("Vous avez obtenu la mention Bien.")
elif 16 <= moyenne <18:
    print("Vous avez obtenu la mention Très Bien.")
elif moyenne >= 18:
    print("Bravo! Vous avez obtenu les félicitations du jury.")
else:
    print("Vous n'avez obtenu aucune mention.")