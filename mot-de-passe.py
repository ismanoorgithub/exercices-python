mdp = input("Veuillez entrer un mot de passe (min 8 caractères): ")

reponse = "votre mot de passe est trop court."

if len(mdp) == 0:
    print(reponse.upper())
elif len(mdp) <8:
    print(reponse.capitalize())
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée")
