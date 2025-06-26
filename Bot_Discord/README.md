# 🤖 MemeBot — Mon premier bot Discord en Python

Bienvenue sur le dépôt de **MemeBot**, un bot Discord développé en Python grâce au tutoriel de [Codedex](https://www.codedex.io/projects/build-a-discord-bot-with-python) 💻✨

Ce bot est capable de répondre à des commandes simples (comme \`!ping\`) et constitue une excellente base pour développer un assistant Discord plus complet.

---

## 🚀 Fonctionnalités

- 🔔 Répond à des commandes dans le chat (\`!ping\`)
- 🧠 Utilise la librairie \`discord.py\` et un système de commandes avec \`commands.Bot\`
- 🔐 Chargement sécurisé du token via un fichier \`.env\`

---

## 🧰 Technologies utilisées

- Python 3.8+
- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🛠️ Installation

1. **Clone le dépôt** :
   \`\`\`bash
   git clone https://github.com/tmlgde/personnal_project.git
   cd discord-bot
   \`\`\`

2. **Crée un environnement virtuel (optionnel mais recommandé)** :
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`

3. **Installe les dépendances** :
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Crée un fichier \`.env\` avec ton token Discord** :
   \`\`\`env
   DISCORD_TOKEN=ton_token_discord_ici
   \`\`\`

---

## ▶️ Lancement du bot

\`\`\`bash
python bot.py
\`\`\`

Tu devrais voir quelque chose comme :

\`\`\`
Bot connecté en tant que MemeBot#1234
\`\`\`

---

## 🔐 Sécurité

⚠️ **Ne jamais publier ton token Discord sur GitHub !**
Utilise toujours un fichier \`.env\` (déjà ignoré via \`.gitignore\`).

---

## 💡 Améliorations futures

- Ajouter une commande \`!meme\` pour envoyer des memes
- Gérer les événements comme les nouveaux arrivants
- Ajouter une base de données pour gérer les stats

---

## 🧑‍💻 Auteur

[@tmlgde](https://github.com/tmlgde)

---

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
EOF
