import tkinter as tk
import random


class QuestionView(tk.Frame):
    def __init__(self, parent, question_data, on_answer):
        super().__init__(parent)

        qid, question, answers = question_data.values()
        random.shuffle(answers)
        for i in range(len(answers)):
            if answers[i][2] == True:
                self.correct = answers[i][0]
        self.on_answer = on_answer

        tk.Label(self, text=question, font=("Arial", 16)).pack(pady=10)

        for id, text, is_correct in answers:
            tk.Button(self, text=text, command=lambda i=id: self.answer(qid, i)).pack(
                fill="x", pady=5
            )

    def answer(self, qid, aid):
        self.on_answer(qid, aid, aid == self.correct)
