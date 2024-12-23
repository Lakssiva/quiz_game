print('''                                
\_____  \  __ __|__|_______    _________    _____   ____  
 /  / \  \|  |  \  \___   /   / ___\__  \  /     \_/ __ \ 
/   \_/.  \  |  /  |/    /   / /_/  > __ \|  Y Y  \  ___/ 
\_____\ \_/____/|__/_____ \  \___  (____  /__|_|  /\___  >
       \__>              \/ /_____/     \/      \/     \/ ''')
questions = [
    {
        "question": "What is the capital of France?",
        "choice": ["A. Paris", "B. Berlin", "C. Madrid", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choice": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choice": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "choice": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    }
]
def run_quiz(questions):
  score=0
  for question in questions:
    print(question["question"])
    for option in question["choice"]:
      print(option)
    answer=input("Enter ur answer('A','B','C','D'):")
    if answer==question["answer"]:
      print("Correct!\n")
      score+=1
    else:
      print("Wrong!  The correct answer is",question["answer"],"\n")

  print(f"Your score is {score} out of {len(questions)}")
