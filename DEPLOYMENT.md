# Guide de déploiement - Yves Programmeur Quiz App

Ce guide vous explique comment déployer l'application Quiz App sur Vercel (frontend) et Render (backend).

## Déploiement du frontend sur Vercel

### Prérequis
- Un compte Vercel (inscription gratuite sur [vercel.com](https://vercel.com))
- Node.js et npm installés sur votre machine

### Étapes de déploiement

1. **Installez l'outil CLI de Vercel** :
   ```bash
   npm install -g vercel
   ```

2. **Préparez le build de production** :
   ```bash
   cd frontend
   npm run build
   ```

3. **Déployez sur Vercel** :
   ```bash
   vercel login
   vercel
   ```

4. **Suivez les instructions dans le terminal** :
   - Confirmez le répertoire du projet
   - Configurez le nom du projet (par exemple, "yves-programmeur-quiz")
   - Choisissez votre compte personnel ou d'équipe
   - Confirmez les paramètres

5. **Configurez les variables d'environnement** :
   - Allez dans les paramètres de votre projet sur le tableau de bord Vercel
   - Ajoutez la variable d'environnement `REACT_APP_API_URL` avec l'URL de votre API backend

## Déploiement du backend sur Render

### Prérequis
- Un compte Render (inscription gratuite sur [render.com](https://render.com))
- Git installé sur votre machine

### Étapes de déploiement

1. **Créez un nouveau service Web sur Render** :
   - Connectez-vous à votre compte Render
   - Cliquez sur "New" puis "Web Service"
   - Connectez votre dépôt GitHub ou téléchargez le code

2. **Configurez le service** :
   - Nom : yves-programmeur-quiz-api
   - Environment : Python 3
   - Build Command : `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command : `gunicorn quiz_project.wsgi`
   - Répertoire : `/backend` (si vous déployez tout le dépôt)

3. **Ajoutez les variables d'environnement** :
   - `SECRET_KEY` : une chaîne aléatoire (par exemple, générez-en une avec `openssl rand -base64 32`)
   - `DEBUG` : False
   - `CORS_ALLOWED_ORIGINS` : l'URL de votre frontend Vercel (par exemple, `https://yves-programmeur-quiz.vercel.app`)

4. **Créez le service** et attendez que le déploiement soit terminé

5. **Testez votre API** en accédant à l'URL fournie par Render

## Connexion du frontend au backend

Une fois que votre backend est déployé, mettez à jour l'URL de l'API dans votre frontend :

1. Allez dans les paramètres de votre projet Vercel
2. Ajoutez une variable d'environnement :
   - Nom : `REACT_APP_API_URL`
   - Valeur : l'URL de votre API backend (par exemple, `https://yves-programmeur-quiz-api.onrender.com/api`)
3. Redéployez votre application

## Création d'un superutilisateur pour l'administration

Pour créer un superutilisateur sur Render, vous pouvez utiliser la console shell :

1. Allez dans votre service Web sur Render
2. Cliquez sur "Shell" dans le menu de gauche
3. Exécutez la commande suivante :
   ```bash
   python manage.py createsuperuser
   ```
4. Suivez les instructions pour créer un superutilisateur

## Dépannage

### Problèmes courants avec le frontend
- **Erreur CORS** : Assurez-vous que l'URL de votre frontend est bien ajoutée dans `CORS_ALLOWED_ORIGINS` dans les paramètres du backend
- **Erreur 404** : Vérifiez que les routes sont correctement configurées dans le fichier `vercel.json`

### Problèmes courants avec le backend
- **Erreur de connexion à la base de données** : Vérifiez les paramètres de connexion à la base de données
- **Erreur de déploiement** : Consultez les logs de déploiement sur Render pour identifier le problème

## Ressources utiles
- [Documentation Vercel](https://vercel.com/docs)
- [Documentation Render](https://render.com/docs)
- [Documentation Django](https://docs.djangoproject.com/)
