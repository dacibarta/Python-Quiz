import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from ui.question_view import QuestionView
import db
import random
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATS_DIR = os.path.join(ROOT, "statistics")


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kvíz App")

        self.container = tk.Frame(self)
        self.container.pack(padx=20, pady=20)

        self.score = 0

        self.show_welcome_screen()

    def show_welcome_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        tk.Label(self.container, text="Üdvözöllek a Kvízben!", font=("Arial", 20)).pack(
            pady=20
        )

        tk.Button(
            self.container,
            text="Kvíz indítása",
            font=("Arial", 14),
            command=self.start_quiz,
        ).pack(pady=10)

    def start_quiz(self):
        self.questions = db.get_questions()

        if not self.questions:
            self.show_welcome_screen()
        else:
            random.shuffle(self.questions)

            self.score = 0
            self.index = 0
            self.load_question()

    def load_question(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        if self.index >= len(self.questions):
            tk.Label(self.container, text="Kvíz vége!", font=("Arial", 20)).pack(
                pady=20
            )
            tk.Label(self.container, text=f"Elért pontok: {self.score}").pack()
            tk.Label(
                self.container,
                text=f"Elért százalék: {self.score/len(self.questions)*100}%",
            ).pack()

            ttk.Separator(self.container, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)

            tk.Button(
                self.container,
                text="Új játék",
                font=("Arial", 14),
                command=self.start_quiz,
            ).pack(pady=10)

            return

        q = self.questions[self.index]
        view = QuestionView(self.container, q, self.on_answer)
        view.pack()

    def on_answer(self, qid, aid, was_correct):
        self.log_question_result(qid, was_correct)
        self.log_answer_choice(qid, aid)

        self.index += 1
        self.load_question()

    def log_question_result(self, question_id, was_correct):

        path = os.path.join(STATS_DIR, "stats_questions.csv")
        try:
            if not os.path.exists(path):
                with open(path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(
                        ["question_id", "total_attempts", "correct_attempts"]
                    )
        except Exception as e:
            messagebox.showinfo(
                "Hiba", f"Nem sikerült létrehozni a stats_questions.csv fájlt.\n{e}"
            )

        rows = {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    rows[int(r["question_id"])] = {
                        "total": int(r["total_attempts"]),
                        "correct": int(r["correct_attempts"]),
                    }
        except Exception as e:
            messagebox.showinfo(
                "Hiba", f"Nem sikerült beolvasni a stats_questions.csv fájlt.\n{e}"
            )

        if question_id not in rows:
            rows[question_id] = {"total": 0, "correct": 0}

        rows[question_id]["total"] += 1
        if was_correct:
            rows[question_id]["correct"] += 1
            self.score += 1

        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["question_id", "total_attempts", "correct_attempts"])
                for qid, data in rows.items():
                    writer.writerow([qid, data["total"], data["correct"]])
        except Exception as e:
            messagebox.showinfo(
                "Hiba", f"Nem sikerült írni a stats_questions.csv fájlba.\n{e}"
            )

    def log_answer_choice(self, question_id, answer_id):

        path = os.path.join(STATS_DIR, "stats_answers.csv")

        try:
            if not os.path.exists(path):
                with open(path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["question_id", "answer_id", "count"])
        except Exception as e:
            messagebox.showinfo(
                "Hiba", f"Nem sikerült létrehozni a stats_answers.csv fájlt.\n{e}"
            )

        rows = {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    key = (int(r["question_id"]), int(r["answer_id"]))
                    rows[key] = int(r["count"])
        except Exception as e:
            messagebox.showinfo(
                "Hiba", f"Nem sikerült beolvasni a stats_answers.csv fájlt.\n{e}"
            )

        key = (question_id, answer_id)
        rows[key] = rows.get(key, 0) + 1

        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["question_id", "answer_id", "count"])
                for (qid, aid), count in rows.items():
                    writer.writerow([qid, aid, count])
        except Exception as e:
            messagebox.showinfo(
                "Hiba", f"Nem sikerült írni a stats_answers.csv fájlba.\n{e}"
            )
