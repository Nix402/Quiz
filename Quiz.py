def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Madrid", "B. Berlin", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
            "answer": "A"
        }
    ]

    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYou completed the quiz! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
