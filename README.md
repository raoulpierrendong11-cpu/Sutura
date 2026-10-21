# Password Tool

Outil en Python pour évaluer la force d'un mot de passe, calculer son empreinte SHA-256, vérifier s'il figure dans une liste de mots de passe connus et en générer un fort.

## Fonctionnalités
- Score de force de 0 à 6 (longueur, minuscules, majuscules, chiffres, symboles)
- Empreinte SHA-256
- Vérification dans une liste de mots de passe compromis (`rockyou.txt`)
- Générateur sécurisé (module `secrets`)

## Installation
1. Installer Python 3
2. Cloner le dépôt
3. Placer un fichier `rockyou.txt` à côté de `main.py`

## Utilisation
```
py main.py
```
Choix 1 : analyser un mot de passe. Choix 2 : en générer un.

## Exemple
```
Mot de passe : azerty123
Score : 3 / 6
Compromis : OUI
```

## Limites et améliorations
- Liste de mots de passe locale uniquement
- Pas d'interface graphique
- Ajouter des tests (pytest) et une API de fuites

## Auteur
[Roo Ndong] 
## Lieu
Dakar , Sénégal
