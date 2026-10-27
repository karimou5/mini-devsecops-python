# Mini-projet DevSecOps Python

Ce mini-projet illustre la mise en œuvre d’un pipeline **CI/CD DevSecOps** complet avec GitHub Actions.

## Étapes du pipeline

```
build ──┬── test ──┬── deploy (main uniquement, environnement staging)
        └── scan ──┘
```

1. **Build** : installation des dépendances (cache pip) et compilation des sources.
2. **Test** : tests unitaires Pytest avec couverture, échec sous 80 %.
3. **Scan** (bloquant), en parallèle des tests :
   - **SAST** avec Bandit (failles dans le code Python) ;
   - **SCA** avec pip-audit (CVE des dépendances) ;
   - **Trivy** en mode filesystem : vulnérabilités HIGH/CRITICAL, secrets et mauvaises configurations.
4. **Deploy** : déploiement simulé en staging, seulement si test et scan passent, et seulement sur un push sur `main` (jamais depuis une pull request).

## Mesures de sécurité du pipeline

- `permissions: contents: read` : le token GitHub a le minimum de droits.
- Actions épinglées par SHA de commit et non par tag (un tag peut être réécrit, comme lors de la compromission de `trivy-action` en 2026).
- Scan Trivy devenu **bloquant** (il était en `continue-on-error`, donc ne bloquait rien).
- Environnement GitHub `staging` : on peut y ajouter une validation manuelle et des secrets dédiés.

## Vulnérabilité trouvée et corrigée

`pip-audit` signalait `pytest==8.0.0` (PYSEC-2026-1845, corrigée en 9.0.3). La dépendance a été montée en `pytest==9.0.3`.

## Exécution locale

```bash
pip install -r requirements.txt
pytest -v --cov=app --cov-fail-under=80
pip install bandit pip-audit
bandit -r . -x ./test_app.py
pip-audit -r requirements.txt
docker run --rm -v "$PWD":/src:ro aquasec/trivy:0.76.1 fs --scanners vuln,secret,misconfig --severity HIGH,CRITICAL --exit-code 1 /src
```
