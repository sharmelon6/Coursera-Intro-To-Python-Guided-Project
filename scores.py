def check(score):
    if score < 50:
        print ("Product Fail")
    else:
        print ("Product Pass")


# get the user's score
score = int(input("Enter your score: "))

# compare the user's score to the scoring system and give feedback
while score >= 0:
    check(score)
    score = int(input("Enter your score: "))