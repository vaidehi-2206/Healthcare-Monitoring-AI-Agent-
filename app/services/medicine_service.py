from pathlib import Path
import csv


# Find project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

MEDICINE_FILE = PROJECT_ROOT / "assets" / "medicines.csv"


def load_medicines():
    """Load medicines from medicines.csv."""

    if not MEDICINE_FILE.exists():
        return []

    medicines = []

    with open(
        MEDICINE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            medicines.append(row)

    return medicines


def search_medicines(query: str):
    """Search medicines by name or purpose."""

    medicines = load_medicines()

    query = query.lower().strip()

    results = []

    for medicine in medicines:

        medicine_name = medicine.get(
            "medicine_name", ""
        ).lower()

        purpose = medicine.get(
            "purpose", ""
        ).lower()

        if (
            query in medicine_name
            or query in purpose
        ):
            results.append(medicine)

    return results


def format_medicine_results(results):
    """Convert medicine records into readable text."""

    if not results:
        return "No matching medicine was found in the medicine database."

    output = []

    for medicine in results:

        output.append(
            f"""
Medicine: {medicine.get('medicine_name', 'N/A')}
Purpose: {medicine.get('purpose', 'N/A')}
Strength: {medicine.get('strength', 'N/A')}
Listed dosage: {medicine.get('dosage', 'N/A')}
Listed frequency: {medicine.get('frequency', 'N/A')}
Take after food: {medicine.get('take_after_food', 'N/A')}
"""
        )

    return "\n".join(output)