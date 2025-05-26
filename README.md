 # Creative Publishing Hub

A simple Python-SQL project modeling the relationship between Writers, Journals, and the creative Pieces they publish.

# Entities

- Writer: Creates many pieces.
- Journal: Publishes many pieces.
- Piece: Belongs to both a writer and a journal.

# Structure

- `Author` → `Writer`
- `Article` → `Piece`
- `Magazine` → `Journal`

# Setup

-bash
PYTHONPATH=. python scripts/setup_db.py
PYTHONPATH=. python lib/db/seed.py# creative-hub
