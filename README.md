# 🎮 Conway's Game of Life

Une implémentation interactive du Jeu de la Vie de Conway - disponible en version **Web** et **Python**.

![Resolution](https://img.shields.io/badge/Resolution-1500x1000-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌐 Jouer en ligne (Recommandé)

**👉 [Lancer le jeu maintenant](https://tomvieilledent.github.io/life-game/)**

Aucune installation requise ! Fonctionne directement dans votre navigateur.

## 📋 Description

Le Jeu de la Vie est un automate cellulaire conçu par le mathématicien John Conway. Cette version propose une grille de **1500x1000 pixels** (300x200 cellules) avec une interface interactive.

### Règles du jeu
- Une cellule **vivante** avec 2 ou 3 voisins vivants survit
- Une cellule **morte** avec exactement 3 voisins vivants devient vivante
- Dans tous les autres cas, la cellule meurt ou reste morte

## � Héberger sur GitHub

### 1. Pousser le code sur GitHub

```bash
cd life-game
git add .
git commit -m "Add Game of Life - Web and Python versions"
git push origin main
```

### 2. Activer GitHub Pages

1. Va sur ton repository : `https://github.com/tomvieilledent/life-game`
2. Clique sur **Settings** (⚙️)
3. Dans le menu de gauche, clique sur **Pages**
4. Sous **Source**, sélectionne :
   - Branch: **main**
   - Folder: **/ (root)**
5. Clique sur **Save**
6. Attends 1-2 minutes ⏱️

### 3. Accéder au jeu

Ton jeu sera accessible à : **`https://tomvieilledent.github.io/life-game/`**

Partage ce lien - tout le monde pourra jouer sans rien installer ! 🎉

## 🚀 Version Python (locale)

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation depuis GitHub

```bash
# Cloner le repository
git clone https://github.com/tomvieilledent/life-game.git
cd life-game

# Option 1 : Installation avec environnement virtuel (recommandé)
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt

# Option 2 : Installation système sur Ubuntu/Debian
sudo apt update
sudo apt install python3-pygame

# Option 3 : Installation pip globale (si autorisé)
pip install -r requirements.txt
```

## 🎯 Utilisation

### Version Web

Ouvre simplement `index.html` dans ton navigateur ou va sur la version hébergée.

**Contrôles Web :**
| Action | Description |
|--------|-------------|
| **Clic gauche** | Activer/désactiver une cellule (maintenir pour dessiner) |
| **Bouton Pause** ou **ESPACE** | Mettre en pause / Reprendre |
| **Bouton Random** ou **R** | Générer une grille aléatoire |
| **Bouton Clear** ou **C** | Effacer toute la grille |
| **Slower / Faster** | Ajuster la vitesse (1-60 FPS) |

### Version Python

Lance depuis le terminal :

```bash
python3 game_of_life.py
```

**Contrôles Python :**

| Touche/Action | Description |
|---------------|-------------|
| **ESPACE** | Mettre en pause / Reprendre |
| **R** | Générer une grille aléatoire |
| **C** | Effacer toute la grille |
| **Clic gauche** | Activer/désactiver une cellule |
| **ESC** | Quitter |

## 🛠️ Configuration

Vous pouvez modifier les paramètres dans `game_of_life.py` :

```python
WIDTH = 1500        # Largeur en pixels
HEIGHT = 1000       # Hauteur en pixels
CELL_SIZE = 5       # Taille de chaque cellule
FPS = 10           # Images par seconde (vitesse du jeu)
```

## 📚 Structure du projet

```
life-game/
├── index.html         # 🌐 Version Web (HTML/JavaScript/Canvas)
├── game_of_life.py    # 🐍 Version Python (Pygame)
├── requirements.txt   # Dépendances Python
├── setup.sh          # Script d'installation
├── .gitignore        # Fichiers à ignorer
└── README.md         # Documentation
```

## 💡 Pourquoi deux versions ?

- **Version Web** (`index.html`) : Fonctionne partout, pas d'installation, hébergeable sur GitHub Pages
- **Version Python** (`game_of_life.py`) : Pour les développeurs Python, plus facile à modifier/étendre

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou un pull request.

## ⚙️ Technologies

- **Frontend** : HTML5 Canvas, JavaScript ES6, CSS3
- **Backend** : Python 3, Pygame
- **Hébergement** : GitHub Pages

## 📄 Licence

Ce projet est sous licence MIT.

## 👨‍💻 Auteur

Tom Vieilledent - [GitHub](https://github.com/tomvieilledent)