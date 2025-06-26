# 🎯 Jeu de Devinette de Mot (Word Guess Game)

Un petit jeu de terminal en Python où le joueur doit deviner un mot, **une lettre à la fois**, avec un maximum de **10 tentatives**.

---

## 🕹️ Principe du jeu

- Un mot est choisi **au hasard** dans une liste prédéfinie.
- Il est affiché sous forme de tirets (ex : `_ _ _ _`).
- Le joueur propose une lettre à chaque tour.
- Si la lettre est dans le mot, elle est révélée.
- Sinon, le nombre de tentatives diminue.
- Le jeu se termine quand :
  - Le mot est entièrement deviné ✅
  - Les tentatives tombent à zéro ❌

---

## 🧰 Pré-requis

- Python 3.x

Aucune bibliothèque externe n’est nécessaire.

---

## ▶️ Lancer le jeu

Dans un terminal :

```bash
python3 word_guess.py
