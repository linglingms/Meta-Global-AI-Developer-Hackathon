# Molecular A(Muse)ing Transcriber

Foundation for a Python + React scientific research application.

## Requirements

- Python 3.12+
- Node.js LTS
- Git

## Backend setup

From the repository root, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
```

Retrieve the first 100 EGFR activity records from ChEMBL:

```powershell
python backend\scripts\retrieve_egfr.py
```

Start the API:

```powershell
python -m uvicorn backend.app.main:app --reload
```

The API is available at <http://127.0.0.1:8000>, with interactive
documentation at <http://127.0.0.1:8000/docs>.

## Frontend setup

In a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

The React application is available at <http://localhost:5173>.

Generated datasets are written to `data/` and are intentionally ignored by
Git. See [`.gitignore`](.gitignore) for the complete list of local files.
