# Mini-projet DevSecOps Python

Le ZIP ne contient pas d'énoncé détaillé. Ce corrigé reprend les quatre étapes annoncées : Build, Test, Scan et Deploy.

## Application

La fonction calculate_average renvoie la somme des nombres divisée par leur nombre.
Exemple : calculate_average([10, 20, 30]) renvoie 20.
Une liste vide provoque une ValueError.

## Exécution locale

Dans le dossier du projet :

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
python -m pytest -v
```

Sous Windows PowerShell, activer avec `.venv\Scripts\Activate.ps1`.
Résultats attendus : `Moyenne : 30.0` et deux tests réussis.
Le premier test vérifie une moyenne connue. Le second vérifie le refus d'une liste vide.

## Pipeline GitHub Actions

| Étape | Outil | Rôle |
| --- | --- | --- |
| Préparation | Checkout et setup-python | Récupérer le code et installer Python 3.11 |
| Build | pip | Installer les dépendances |
| Test | pytest | Vérifier le comportement de la fonction |
| Scan | Trivy | Rechercher les vulnérabilités HIGH et CRITICAL des dépendances reconnues |
| Deploy | echo | Simuler un déploiement en staging |

Le workflow se lance sur un push vers main, sur une pull request ou manuellement.
Les étapes s'exécutent dans l'ordre. Un test en échec empêche les étapes suivantes.
Le scan bloque la suite si une vulnérabilité du niveau sélectionné est détectée,
même sans correctif disponible. Une erreur d'exécution du scan bloque également la suite.
Le déploiement est uniquement un message dans les logs et ne s'exécute qu'après un push vers main réussi.
Aucun serveur n'est modifié.

## Lancer sur GitHub

1. Créer un dépôt GitHub vide.
2. Placer le contenu de ce dossier à la racine du dépôt, en conservant .github.
3. Envoyer le code sur main.
4. Ouvrir Actions, puis CI DevSecOps pour consulter les étapes et leurs logs.

Pour un dépôt neuf, remplacer URL_DU_DEPOT par son URL :

```bash
git init
git add .
git commit -m "Ajout du pipeline DevSecOps"
git branch -M main
git remote add origin URL_DU_DEPOT
git push -u origin main
```

## Démontrer le blocage des tests

1. Créer une branche avec `git switch -c demo-test-echec`.
2. Remplacer temporairement le résultat attendu 20 par 99 dans le premier test.
3. Faire un commit, pousser la branche et ouvrir une pull request vers main.
4. Observer l'échec de pytest et les étapes suivantes ignorées.
5. Remettre 20, faire un nouveau commit et pousser la correction.

Sur une pull request, le déploiement est ignoré même si les contrôles réussissent.
Il est simulé après un push vers main qui passe tous les contrôles.

## Corrections apportées

- README complété et bloc de code fermé.
- Action Trivy mise à jour vers la version documentée v0.36.0.
- Suppression de continue-on-error et ajout de exit-code: "1" pour rendre le scan bloquant.
- Analyse explicite des vulnérabilités, sans ignorer celles sans correctif.
- Déploiement simulé limité aux pushs vers main.
- Permissions du workflow limitées à la lecture du dépôt.
- Lancement manuel des contrôles possible.

## Texte pour le compte rendu

Ce projet met en place un pipeline CI/CD avec GitHub Actions.
Il installe les dépendances Python, exécute les tests unitaires avec Pytest
puis analyse les dépendances avec Trivy.
Si les contrôles réussissent après un push sur main, un déploiement en staging est simulé.
Les contrôles de sécurité sont ainsi intégrés au processus de livraison.

## Référence

Documentation officielle : https://github.com/aquasecurity/trivy-action
