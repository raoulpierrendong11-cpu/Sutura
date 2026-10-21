import hashlib
import secrets
import string
def score(mdp):
    points = 0
    if len(mdp) >= 12:
        points += 2
    elif len(mdp) >= 8:
        points += 1
    if any(c.islower() for c in mdp):
        points += 1
    if any(c.isupper() for c in mdp):
        points += 1
    if any(c.isdigit() for c in mdp):
        points += 1
    if any(c in string.punctuation for c in mdp):
        points += 1
    return points


def hash_mdp(mdp):
    return hashlib.sha256(mdp.encode()).hexdigest()


def est_compromis(mdp, fichier="rockyou.txt"):
    try:
        with open(fichier, "r", encoding="latin-1") as f:
            for ligne in f:
                if ligne.strip() == mdp:
                    return True
    except FileNotFoundError:
        print("Fichier de mots de passe introuvable.")
    return False


def generer(longueur=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(longueur))


def main():
    print("1. Analyser  2. Générer")
    choix = input("Choix : ")
    if choix == "1":
        mdp = input("Mot de passe : ")
        print("Score :", score(mdp), "/ 6")
        print("SHA-256 :", hash_mdp(mdp))
        print("Compromis :", "OUI" if est_compromis(mdp) else "non trouvé")
    elif choix == "2":
        print("Proposition :", generer())


if __name__ == "__main__":
    main()
                