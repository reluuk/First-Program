def save_score(score, playername, attempts):
    score_highscore = ""
    if score == 1:
        score_highscore = "Highscore:"
    else:
        score_highscore = "Score:"
    with open("HighscoreGuessingGame.txt", "a") as x:
        x.write(f"Player: {playername}\n{score_highscore} {score}/{attempts}\n")
        x.close()
def play(versuche):
    random_num = random.randint(1,100)
    print(f"DEBUG: {random_num}")
    win = False
    score = 0
    while score < versuche and win == False:
        score += 1 # Kurzform für score = score + 1
        geraten_num = input(f"({score})Guess a number from 1 to 100 (max. {versuche} attempts):")
        try:
            geraten_num = int(geraten_num)
            if geraten_num < 1 or geraten_num > 100:
                raise ValueError # raise erzwingt eine Exception
        except ValueError:
            print("Only whole numbers from 1 to 100 are valid!")
            continue # springt zum nächsten Schleifendurchlauf
        if geraten_num == random_num and score == 1:
            print(f"You guessed on the first try! Wanted number was {random_num}.")
            print("Highscore = 1.")
            win = True
        elif geraten_num == random_num:
            print(f"You guessed right! Wanted number was {random_num}.")
            print(f"Score = {score}.")
            win = True
        elif geraten_num > random_num:
            print(f"The wanted number is smaller.")
        else:
            print(f"The wanted number is bigger.")
    if score == versuche:
        print(f"Too many attempts! ({score})")
    return score
import random
x = open("HighscoreGuessingGame.txt", "w")
while True:
    playername = input("Input your playername: ")
    versuche = input("Number of attempts: ")
    try:
        versuche = int(versuche)
        if versuche < 0:
            raise ValueError  # raise erzwingt eine Exception
    except ValueError:
        print("Wrong Input!")
        continue  # springt zum nächsten Schleifendurchlauf
    save_score(play(versuche), playername, versuche)
    correctUserInput = False
    while not correctUserInput:
        Continue = input("play again? [y/n]")
        if "n" == Continue:
            exit()
        elif Continue == "y":
            correctUserInput = True
        else:
            print("wrong input")