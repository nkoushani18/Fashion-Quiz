def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if 1 <= user_answer <= len(options):
                break
            else:
                print("Please select a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if options[user_answer - 1] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}\n")
        return False

# Main function to run the quiz
def run_quiz():
    questions = [
        {
            "question": "Which fashion designer is known for the 'Little Black Dress'?",
            "options": ["Coco Chanel", "Donatella Versace", "Alexander McQueen", "Giorgio Armani"],
            "correct_answer": "Coco Chanel"
        },
        {
            "question": "Which city is often referred to as the fashion capital of the world?",
            "options": ["Paris", "New York", "Milan", "London"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which brand is famous for its red-soled shoes?",
            "options": ["Manolo Blahnik", "Christian Louboutin", "Jimmy Choo", "Gucci"],
            "correct_answer": "Christian Louboutin"
        },
        {
            "question": "Which fashion house is known for the 'double C' logo?",
            "options": ["Chanel", "Cartier", "Calvin Klein", "Chloé"],
            "correct_answer": "Chanel"
        },
        {
            "question": "Which fashion designer is associated with the punk fashion movement?",
            "options": ["Vivienne Westwood", "Ralph Lauren", "Tom Ford", "Karl Lagerfeld"],
            "correct_answer": "Vivienne Westwood"
        },
        {
            "question": "Which company is known for its iconic trench coat?",
            "options": ["Burberry", "Prada", "Louis Vuitton", "Hermès"],
            "correct_answer": "Burberry"
        },
        {
            "question": "Which fashion brand has a logo featuring a Medusa head?",
            "options": ["Versace", "Dolce & Gabbana", "Fendi", "Givenchy"],
            "correct_answer": "Versace"
        },
        {
            "question": "Which fashion brand introduced the 'New Look' in 1947?",
            "options": ["Dior", "Balenciaga", "Yves Saint Laurent", "Valentino"],
            "correct_answer": "Dior"
        },
        {
            "question": "Which fashion designer is known for the wrap dress?",
            "options": ["Diane von Fürstenberg", "Stella McCartney", "Victoria Beckham", "Donna Karan"],
            "correct_answer": "Diane von Fürstenberg"
        },
        {
            "question": "Which fashion brand is known for its iconic monogram canvas bags?",
            "options": ["Louis Vuitton", "Gucci", "Chanel", "Hermès"],
            "correct_answer": "Louis Vuitton"
        }
    ]
    
    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1

    print(f"Quiz Complete! Your final score is: {score} out of {len(questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
