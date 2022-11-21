from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import psycopg

origins = [
    "http://localhost:3000",
    os.environ.get("CORS_HOST", None),
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CategoryOut(BaseModel):
    id: int
    title: str
    canon: bool


class ClueOut(BaseModel):
    id: int
    question: str
    answer: str
    value: int
    invalid_count: int
    canon: bool
    category: CategoryOut


def row_to_clue(row):
    return {
        "id": row[3],
        "question": row[4],
        "answer": row[5],
        "value": row[6],
        "invalid_count": row[7],
        "canon": row[8],
        "category": {
            "id": row[0],
            "title": row[1],
            "canon": row[2],
        },
    }


@app.get(
    "/api/random-clue",
    response_model=ClueOut,
)
def get_random_clue():
    with psycopg.connect() as conn:
        with conn.cursor() as cur:

            cur.execute(
            """
                SELECT cats.id, cats.title, cats.canon,
                       clues.id, clues.question, clues.answer,
                       clues.value, clues.invalid_count,
                       clues.canon
                FROM categories AS cats
                INNER JOIN clues ON (cats.id = clues.category_id)
                ORDER BY RANDOM()
                LIMIT 1
            """,
            )

            row = cur.fetchone()
            return row_to_clue(row)
