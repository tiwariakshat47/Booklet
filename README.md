# Booklet

## Overview

A structured learning path for building and deploying a book recommender system using the Book-Crossing dataset.

---

## The Three Core Approaches

| Approach | Description | Best For |
|---|---|---|
| **Collaborative Filtering** | "Users like you also liked…" — learns from user-item interaction patterns | Classic starting point, no item metadata needed |
| **Content-Based Filtering** | "Because you liked X…" — uses book features like genre, author, description | When you have rich item metadata |
| **Hybrid** | Combines both approaches | What most real-world systems use |

> 💡 **Start with collaborative filtering** — it teaches core ideas with minimal data wrangling.

---

## Dataset

Use the **Book-Crossing dataset** (public, free):

- ~270k users, ~1M ratings, ~270k books
- Has user ratings (explicit feedback) + book metadata
- Download: http://www2.informatik.uni-freiburg.de/~cziegler/BX/

---

## Algorithm Progression

| Step | Algorithm | Library | Why |
|---|---|---|---|
| 1st | **Matrix Factorization (SVD)** | `surprise` | Clean API, great for learning latent factor models |
| 2nd | **ALS (Alternating Least Squares)** | `implicit` | Better for sparse/implicit data, industry-standard |
| 3rd | **Neural CF or LightFM** | `lightfm` | Bridges into deep learning + hybrid models |


## Build Plan
### Phase 1 — Data & Baseline (Day 1–2)

Load Book-Crossing data with pandas
Explore: rating distribution, sparsity, popular books
Build a simple popularity baseline ("most rated books")

Phase 2 — Collaborative Filtering (Day 3–5)

Build a user-item ratings matrix
Train SVD with the surprise library
Evaluate with RMSE and train/test split
Generate top-N recommendations for a user

Phase 3 — Improve & Understand (Day 6–7)

Tune hyperparameters: n_factors, regularization, learning rate
Try user-based vs item-based KNN for comparison
Understand and address the cold-start problem


Phase 4 — Deploy (Day 8–10)

Wrap your model in a FastAPI endpoint
Build a minimal UI with Streamlit
Deploy for free on Hugging Face Spaces or Railway
