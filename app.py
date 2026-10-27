def calculate_average(numbers):
    """Retourne la moyenne d'une liste de nombres"""
    if not numbers:
        raise ValueError("La liste ne peut pas être vide.")
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(f"Moyenne : {calculate_average(data)}")
