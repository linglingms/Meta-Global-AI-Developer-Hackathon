from fastapi import FastAPI

app = FastAPI(
    title="Molecular A(Muse)ing Transcriber API",
    description="AI-powered drug discovery research platform",
    version="0.1.0",
)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to Molecular A(Muse)ing Transcriber!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy", "application": "Molecular A(Muse)ing Transcriber"}
