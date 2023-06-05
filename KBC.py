questions = ["Q1. What is the capital on India?", "Q2. Who is PM of India?", "Q3. Shape of Window?"]
options = [["A. Delhi", "B. Mumbai", "C. Kolkata","D. Syria"],["A. Modi","B.Rahul","C.Mamta"],["A.Square","B. Rect","C. Circle"]]
answers = ["A","A","B"]


print("Welcome to KBC, Every Correct Answer Gives you 1k, \n And wrong answer will give you 0")

name=input("Please Enter Your Name: ")

sum = 0
rewards = 0
def awards(sum):
    sum = sum + 1000
    return sum

rewards = 0

def show_options(i):
    j =0
    while j < len(options[i]):
        print(options[i][j])
        j = j + 1


def show_questions(i):
    print(questions[i])

i = 0

for i in range(len(questions)):
    show_questions(i)
    show_options(i)
    abc = input("Please enter your choice: ")
    if abc == answers[i]:
        rewards = awards(rewards)
        print(f"you have won {rewards}")
        i = i+1
    else:
        print("you loose")
        break
print(rewards)
     
    


# for i in questions:
#     print(i)
#     k=0
#     j = 0
# # abc = NULL
#     print(len(options[k]))
#     while j is range(len(options[k])):
#         print(options[k][j])
#         j=j +1
#     abc = input("Please enter your choice: ")
#     if abc == answers[i]:
#         rewards = awards()
#         print(f"you have won {rewards}")
#         k = k+1
#     else:
#         print("you loose")
#     print(rewards)
#     break



