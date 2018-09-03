#Ask for various questions
class Ask():
    def __init__(self,user_option="h",cash="1000",coin="100",answer="yes"):
        self.user_option=user_option
        self.cash=cash
        self.coin=coin
        self.answer=answer
    def ask_player(self):
        while True:
            try:
                self.user_option = str(input("Do you want to Hit or Stand"))
                break
            except:
                print("Invalid option. Please try again")
            
    
    def ask_cash(self):
        while True:
            try:
                self.cash = int(input("Enter the amount of you want to invest"))
                break
            except:
                print("Enter a valid integer in Dollar")
            
    def ask_coin(self):
        while True:
            try:
                self.coin = int(input("Enter the coins you want to invest"))
                break
            except:
                print("Enter a valid integer amount")
                 
ask = Ask()

#Bet determines lose or win
class Bet():
    def __init__(self,cash,coin):
        self.cash=cash
        self.coin=coin
    def bet_lose(self):
        bet.cash-=bet.coin
        print(f"The available cash is {self.cash} and withdrawn coin is {self.coin}")
    def bet_win(self):
        bet.cash+=bet.coin
        print(f"The availabe balance is {self.cash} and gain coin is {self.coin}")

suits = ("Diamond","Spade","Club","Heart")
cards = {"Ace":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"King":10,"Queen":10,"Jack":10}

#Append to the new deck
new_deck = []
for suit in suits:
    for card in cards:
        new_deck.append(card)

#shuffle the new deck
def reshuffle():
    import random
    random.shuffle(new_deck)

#Adding each card for player and dealer while select hit.
class Score():
    def __init__(self,player_score=0,dealer_score=0):
        self.player_score=player_score
        self.dealer_score=dealer_score
    def player_hit(self):
        if new_deck[0].lower()=="ace" and self.player_score<11:
            card_score=11
            self.player_score+=card_score
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            print("The Player card score is {}".format(card_score))
        elif new_deck[0].lower()=="ace" and self.player_score>=11:
            card_score=1
            self.player_score+=card_score
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            print("The Player card score is {}".format(card_score))
        else:
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            card_score = cards.get(poped_num)
            self.player_score+=card_score
            print("The Player card score is {}".format(card_score))
    def dealer_hit(self):
        if new_deck[0].lower()=="ace" and self.dealer_score<11:
            card_score=11
            self.dealer_score+=card_score
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            print("The Dealer card score is {}".format(card_score))
        elif new_deck[0].lower()=="ace" and self.dealer_score>=11:
            card_score=1
            self.dealer_score+=card_score
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            print("The Dealer card score is {}".format(card_score))
        else:
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            card_score = cards.get(poped_num)
            self.dealer_score+=card_score
            print("The Dealer card score is {}".format(card_score))
    def dealer_hit_hidden(self):
        if new_deck[0].lower()=="ace" and self.dealer_score<11:
            card_score=11
            self.dealer_score+=card_score
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            print("The Dealer card score is <hidden>")
        elif new_deck[0].lower()=="ace" and self.dealer_score>=11:
            card_score=1
            self.dealer_score+=card_score
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            print("The Dealer card score is <hidden>")
        else:
            poped_num = new_deck.pop(0)
            new_deck.append(poped_num)
            card_score = cards.get(poped_num)
            self.dealer_score+=card_score
            print("The Dealer card score is <hidden>")

#First Deal Class
score = Score()
class Deal():
    def __init__(self):
        pass
    def first_move(self):
        score.player_hit()
        score.player_hit()
        print("Total Player score is {}".format(score.player_score))
        print("=====================================================")
        score.dealer_hit_hidden()
        score.dealer_hit()
        

#Start the Dealers turn
class Turn():
    def __init__(self):
        pass
    def dealers_turn(self):
        while True:
            if score.dealer_score < 17:
                score.dealer_hit()
                print("The Dealer total score is {}".format(score.dealer_score))
            else:
                print("The Dealer total score is {}".format(score.dealer_score))
                break
    def players_turn(self):
        while True:
            if score.player_score < 21:
                ask.ask_player()
                if ask.user_option.lower()=="h":
                    score.player_hit()
                    print("The total player score is {}".format(score.player_score))
                elif ask.user_option.lower()=="s":
                    turn.dealers_turn()
                    break
            elif score.player_score==21:
                turn.dealers_turn()
                break
            elif score.player_score>21:
                turn.dealers_turn()
                break

class Play():
    def __init__(self):
        pass
    def play_now(self):
        if score.player_score == score.dealer_score:
            print("=======PUSH=======")
            
        elif score.player_score==21:
            print("Player won the match. Congradulation")
            bet.bet_win()
            
        elif score.player_score<21 and score.player_score>score.dealer_score:
            print("Player won the match. Congradulations")
            bet.bet_win()
            
        elif score.player_score>21:
            print("Sorry, You lose the match")
            bet.bet_lose()
            
        elif score.dealer_score>21 and score.player_score<21:
            print("You won the match. Congradulation")
            bet.bet_win()
            
        else:
            print("You lose the match")
            bet.bet_lose()
            
#Black Jack game strating here
print("Welcome to Black Jack game")
            
ask = Ask()
ask.ask_cash()
ask.ask_coin()
bet = Bet(ask.cash,ask.coin)
reshuffle()
score = Score()
deal = Deal()
deal.first_move()
turn = Turn()
turn.players_turn()
play = Play()
play.play_now()

while True:
    input_value = str(input("Do you want to play again? Yes/No"))
    if input_value.lower()=="yes":
        ask.ask_coin()
        if ask.coin < bet.cash:
            reshuffle()
            score = Score()
            deal = Deal()
            deal.first_move()
            turn = Turn()
            turn.players_turn()
            play = Play()
            play.play_now()
        else:
            print("The invested coin in greater than available cash")
            
    elif input_value.lower()=="no":
        break
