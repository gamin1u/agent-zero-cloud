# 🤖 Agent Zero - Cloud Deployment

Interface vocale AI avec déploiement cloud gratuit sur Render.

## 🚀 Déploiement rapide sur Render (GRATUIT)

### Prérequis
- Compte GitHub
- Compte Render
- Clé API Groq gratuite ([console.groq.com](https://console.groq.com))

### Étapes de déploiement

1. **Créez un dépôt GitHub** avec ce code

2. **Connectez GitHub à Render**
   - Allez sur [render.com](https://render.com)
   - Cliquez sur "New +" → "Web Service"
   - Sélectionnez votre dépôt

3. **Configurez le service**
   - Render détectera automatiquement le `render.yaml`
   - Ajoutez la variable d'environnement : `API_KEY_GROQ=votre_clé_ici`

4. **Déployez**
   - Cliquez sur "Create Web Service"
   - Attendez 5-10 minutes

5. **Accédez à l'URL** fournie par Render

### 📱 Utilisation

- Ouvrez l'URL sur votre téléphone
- Cliquez sur le bouton 🎤 microphone
- Parlez en français !

### ⚠️ Limitations du plan gratuit

- Délai de démarrage : ~30 secondes après inactivité
- Arrêt automatique après 15 minutes sans utilisation
- Pas de persistance des données
- RAM : 512 MB

### 📖 Documentation complète

Voir `/root/render-free-deployment.md` pour le guide détaillé.

---

**Développé avec ❤️ pour un accès 24/7**
