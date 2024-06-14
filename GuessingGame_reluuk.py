import random
def save_score(score):
    x = open("HighscoreGuessingGame.txt", "w")
    x.write(f"Highscore: {score}")
def play():
    random_num = random.randint(1,100)
    print(f"DEBUG: {random_num}")
    win = False
    score = 0

    while score < 10 and win == False:
        score += 1 # Kurzform für score = score + 1
        geraten_num = input(f"({score})Rate eine ganze Zahl von 1 bis 100:")
        try:
            geraten_num = int(geraten_num)
            if geraten_num < 1 or geraten_num > 100:
                raise ValueError # raise erzwingt eine Exception
        except ValueError:
            print("Nur ganze Zahlen von 1 bis 100 sind gültig!")
            continue # springt zum nächsten Schleifendurchlauf
        if geraten_num == random_num and score == 1:
            print(f"Richtig geraten! Zufallszahl = {random_num}")
            print("Perfekt! Highscore = 1.")
            win = True
        elif geraten_num == random_num:
            print(f"Richtig geraten! Zufallszahl = {random_num}")
            print(f"Score = {score}.")
            win = True
        elif geraten_num > random_num:
            print(f"Gesuchte Zahl ist kleiner.")
            erraten_num = geraten_num
        elif score == 10:
            print(f"Zu viele Versuche! ({score})")
            exit()
        else:
            print(f"Gesuchte Zahl ist größer.")
            erraten_num = geraten_num
    if score == 10:
                print(f"Zu viele Versuche! ({score})")
    return score
while True:
    save_score(play())
    correctUserInput = False
    while not correctUserInput:
        Continue = input("Nochmal spielen? [j/n]")
        #if Continue == "n":
        if "n" == Continue:
            exit()
        elif Continue == "j":
            #break
            correctUserInput = True
        else:
            print("Falsche Eingabe")