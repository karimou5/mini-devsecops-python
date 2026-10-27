# Démo : clé d'accès codée en dur (fausse clé), Trivy doit la détecter
AWS_ACCESS_KEY_ID = "AKIA4HJQ7ZPLR2MXW6TB"


def calculate_average(numbers):
    """Retourne la moyenne d'une liste de nombres"""
    if not numbers:
        raise ValueError("La liste ne peut pas être vide.")
    return sum(numbers) / len(numbers)

if __name__ == "__main__":  # pragma: no cover
    data = [10, 20, 30, 40, 50]
    print(f"Moyenne : {calculate_average(data)}")
