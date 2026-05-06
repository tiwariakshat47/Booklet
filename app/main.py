from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import json

app = FastAPI(title="Booklet API")

# Load model and lookup files on startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("book_titles.json") as f:
    book_titles = json.load(f)

with open("reliable_books.json") as f:
    reliable_books = json.load(f)

with open("users.json") as f:
    users = json.load(f)


# --- Routes ---

@app.get("/")
def root():
    return {"message": "Booklet API is running"}


@app.get("/users")
def get_users():
    """Return a sample of users for the UI dropdown."""
    return {"users": users[:50]}  # cap at 50 for the UI


@app.get("/recommend/{user_id}")
def recommend(user_id: str, n: int = 10):
    """Return top-N book recommendations for a user."""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    # Get books this user has already rated - not available at serving time
    # so we predict on all reliable books and let the model score them
    predictions = [model.predict(user_id, book_id) for book_id in reliable_books]
    predictions.sort(key=lambda x: x.est, reverse=True)

    results = []
    for pred in predictions[:n]:
        results.append({
            "book_id": pred.iid,
            "title": book_titles.get(pred.iid, "Unknown"),
            "predicted_rating": round(pred.est, 2)
        })

    return {"user_id": user_id, "recommendations": results}