from fastapi import FastAPI

app = FastAPI(
    title="KrishiPrajna API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "KrishiPrajna Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
