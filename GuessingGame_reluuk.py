import random
x = open("HighscoreGuessingGame.txt", "w")
def save_score(score, playername):
    with open("HighscoreGuessingGame.txt", "a") as x:
        x.write(f"player: {playername}\nscore: {score}\n")
        x.close()
def play():
    random_num = random.randint(1,100)
    print(f"DEBUG: {random_num}")
    win = False
    score = 0

    while score < 10 and win == False:
        score += 1 # Kurzform für score = score + 1
        geraten_num = input(f"({score})Guess a number from 1 to 100:")
        try:
            geraten_num = int(geraten_num)
            if geraten_num < 1 or geraten_num > 100:
                raise ValueError # raise erzwingt eine Exception
        except ValueError:
            print("Only whole numbers from 1 to 100 are valid!")
            continue # springt zum nächsten Schleifendurchlauf
        if geraten_num == random_num and score == 1:
            print(f"You guessed on the first try! wanted number = {random_num}")
            print("Highscore = 1.")
            win = True
        elif geraten_num == random_num:
            print(f"You guessed right! wanted number = {random_num}")
            print(f"Score = {score}.")
            win = True
        elif geraten_num > random_num:
            print(f"The wanted number is smaller.")
            erraten_num = geraten_num
        elif score == 10:
            print(f"Too many attempts ({score})")
            exit()
        else:
            print(f"The wanted number is bigger.")
            erraten_num = geraten_num
    if score == 10:
                print(f"Zu viele Versuche! ({score})")
    return score
while True:
    playername = input("input your playername: "
    save_score(play(),playername))
    correctUserInput = False
    while not correctUserInput:
        Continue = input("play again? [y/n]")
        #if Continue == "n":
        if "n" == Continue:
            exit()
        elif Continue == "y":
            #break
            correctUserInput = True
        else:
            print("wrong input")