def guess_v2(min_v, max_v):
    """GA game where the user invents a number. The computer then tries to guess that number.
    The user should answer questions. If user tries to cheat, computer will display a cheat message."""
    print('Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach')

    while True:
        guess = int((max_v - min_v) / 2) + min_v
        print('Zgaduję:' + str(guess))
        user_answer = input('Wprowadź odpowiedź "too small", "too big", "you win": ')
        user_answer = user_answer.lower()
        if user_answer == "you win":
            return "You win!"

        if user_answer == "too big":
            max_v = guess
            if max_v - min_v <= 1:
                print('Nie oszukuj!')
                min_v = 0
                max_v = 1000
            continue
        if user_answer == "too small":
            min_v = guess
            continue
        else:
            print('Podana odpowiedź jest błędna!')
            continue

    return guess


new = guess_v2(0, 1000)
print(new)
