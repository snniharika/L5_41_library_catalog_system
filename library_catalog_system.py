"""Library catalog management module."""

import hashlib
import logging
import secrets
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)

catalog = {
    "B01": {"title": "Clean Code", "copies": 3},
    "B02": {"title": "The Pragmatic Programmer", "copies": 1},
    "B03": {"title": "Design Patterns", "copies": 2},
}


def issue_book(book_id, patron, active_issues=None):
    """Issue an available book and record the transaction."""
    if active_issues is None:
        active_issues = []

    if not isinstance(book_id, str) or not book_id.strip():
        raise ValueError("Book ID must be a non-empty string.")
    if not isinstance(patron, str) or not patron.strip():
        raise ValueError("Patron ID must be a non-empty string.")
    if book_id not in catalog or catalog[book_id]["copies"] <= 0:
        return False

    catalog[book_id]["copies"] -= 1
    active_issues.append(f"Issued book {book_id} to patron {patron}")
    return True


def return_book(book_id):
    """Return a book if it exists in the catalog."""
    if book_id not in catalog:
        raise ValueError(f"Unknown book ID: {book_id}")

    catalog[book_id]["copies"] += 1


def check_availability(book_id):
    """Return whether a known book has copies available."""
    if book_id not in catalog:
        return False
    return catalog[book_id]["copies"] > 0


def calculate_fine(days_overdue, daily_rate=2.0):
    """Calculate a fine from validated numeric inputs."""
    if isinstance(days_overdue, bool) or not isinstance(days_overdue, int):
        raise TypeError("Days overdue must be an integer.")
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative.")
    if isinstance(daily_rate, bool) or not isinstance(
        daily_rate, (int, float)
    ):
        raise TypeError("Daily rate must be numeric.")
    if daily_rate < 0:
        raise ValueError("Daily rate cannot be negative.")

    return days_overdue * daily_rate


def generate_patron_hash(patron_id):
    """Create a SHA-256 digest for a patron identifier."""
    if not isinstance(patron_id, str) or not patron_id:
        raise ValueError("Patron ID must be a non-empty string.")

    return hashlib.sha256(patron_id.encode("utf-8")).hexdigest()


def generate_temp_patron_pin():
    """Generate a cryptographically secure four-digit temporary PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_catalog(filename="catalog_export.txt"):
    """Export the catalog to a text file."""
    output_path = Path(filename)
    output_path.write_text(
        f"{catalog}\n",
        encoding="utf-8",
    )
    logger.info("Catalog backup exported to: %s", output_path)


def main():
    """Run the library catalog demonstration."""
    active_issues = []

    issue_book("B01", "P101", active_issues)
    return_book("B02")

    print("Is B01 available:", check_availability("B01"))
    print("Fine accrued:", calculate_fine(4))
    print("Patron Hash:", generate_patron_hash("P101"))
    print("Temp PIN:", generate_temp_patron_pin())
    export_catalog()


if __name__ == "__main__":
    main()
