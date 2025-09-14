def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter the answers (A, B, C, D) :")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)    
    
#--------------------------
def check_answer(answer, guess):
    if guess == answer:
        print("Your answer is correct")
        return 1
    else:
        print("Your answer is wrong.")
        return 0
    
#--------------------------
def display_score(correct_guesses, guesses):
    print("---------------------")
    print("Rsults")
    print("---------------------")
    
    print("Answers : ", end = " ")
    for i in questions:
        print(questions.get(i), end = " ")
        print()
        
    print("Guesses : ", end = " ")
    for i in guesses:
        print(i , end = " ")
        print() 
        
    score = int((correct_guesses/len(questions))* 100) 
    print("Your score is : "+str(score) + "%")
#--------------------------
def play_again():
    response = input("Do you want to play again? (yes or no) : ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
#--------------------------

questions = {
    "What is the capital of India? :" : "A",
    "Who created python? :" : "B",
    "What is the largest planet in our solar system? :" : "C",
    "Who is the terrorist country in the world? :" : "D"
}
#--------------------------

options = [["A. Delhi", "B. Mumbai", "C. Chennai", "D. Patna"],
           ["A. Albert Einstien", "B. Guido Van Rossum", "C.Jhonny Depp", "D. Tom Cruise"],
           ["A. Earth", "B. Uranus", "C. Jupiter", "D. Saturn"],
           ["A. Bangladesh", "B. Pakistan", "C. Palestine", "D. All of the above" ]]

new_game()

while play_again():
    new_game()
    print("Byeeee!")