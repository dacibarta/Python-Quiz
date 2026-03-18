import sqlite3
import os
from tkinter import messagebox

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(ROOT, "backend", "db.sqlite3")


def get_connection():
    return sqlite3.connect(DB_FILE)


def get_questions():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, text FROM quiz_question")
        questions = cur.fetchall()

        result = []

        for qid, text in questions:
            cur.execute(
                """
                SELECT id, text, is_correct 
                FROM quiz_answer 
                WHERE question_id = ?
            """,
                (qid,),
            )
            answers = cur.fetchall()

            result.append({"id": qid, "text": text, "answers": answers})

        conn.close()
        return result
    except Exception as e:
        messagebox.showinfo("Hiba", f"Hiba történt a kérdések lekérésekor.\n{e}")
        return []
