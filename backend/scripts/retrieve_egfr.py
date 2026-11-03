import csv
from pathlib import Path
from typing import Any

import requests

BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "data" / "egfr_activity.csv"
ACTIVITY_LIMIT = 100


def find_egfr_target() -> str:
    """Find the human EGFR protein target in ChEMBL."""
    response = requests.get(
        f"{BASE_URL}/target.json",
        params={
            "pref_name__icontains": "epidermal growth factor receptor",
            "organism": "Homo sapiens",
            "limit": 100,
        },
        timeout=30,
    )
    response.raise_for_status()

    for target in response.json().get("targets", []):
        if target.get("pref_name", "").lower() == (
            "epidermal growth factor receptor"
        ):
            target_id = target.get("target_chembl_id")
            if target_id:
                return target_id

    raise LookupError("ChEMBL did not return the human EGFR protein target.")


def fetch_activities(target_id: str, limit: int = ACTIVITY_LIMIT) -> list[dict[str, Any]]:
    """Retrieve experimental activity records for a ChEMBL target."""
    response = requests.get(
        f"{BASE_URL}/activity.json",
        params={"target_chembl_id": target_id, "limit": limit},
        timeout=30,
    )
    response.raise_for_status()
    activities = response.json().get("activities", [])
    return activities[:limit]


def save_to_csv(activities: list[dict[str, Any]], output_path: Path = OUTPUT_PATH) -> None:
    """Save selected activity fields in a spreadsheet-compatible CSV file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "molecule_chembl_id",
        "standard_type",
        "standard_value",
        "standard_units",
        "assay_chembl_id",
        "document_chembl_id",
    ]
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(
            {field: activity.get(field, "") for field in fieldnames}
            for activity in activities
        )


def main() -> None:
    print("Starting Molecular A(Muse)ing Transcriber data retrieval...\n")
    target_id = find_egfr_target()
    print(f"Target found!\nProtein: Epidermal growth factor receptor\nChEMBL ID: {target_id}")

    activities = fetch_activities(target_id)
    print(f"\nRetrieved {len(activities)} activity records.")
    save_to_csv(activities)
    print(f"Results saved to: {OUTPUT_PATH}")
    print("\nMolecular A(Muse)ing Transcriber data retrieval completed!")


if __name__ == "__main__":
    main()
