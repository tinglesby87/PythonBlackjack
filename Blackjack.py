import random


#  def start_game()
#  Game()
#  def start(self):
# Game = play_game()
# unfinished


def start__game():
    answer = input("Do you want to start a game of Blackjack? Y/n")
    if answer != "n":
        make_deck()
        #  play_game() suits= ["H", "D", "C", "S"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = []


#  self.suits= ["H", "D", "C", "S"]
#  self.values = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"]
#  self.deck = []

#  def make_deck(self):
#  card = (s,v)
#  for s in self.suit:
#  for v in self.val:
#  self.deck.append(v + ', ' + s)
#  return self.deck

#  create variable that is empty list, it will put card encountered into list 52 times


def make_deck():
    deck = []  # can delete this if we are going to self
    suits = ["H", "D", "C", "S"]
    for suit in suits:
        for val in values:
            deck.append([suit, val])
    return deck


def create_hand(deck):
    hand = []
    for card in range(2):
        random_card = random.randint(0, 52)
        hand.append(deck[random_card])
    return hand

deck = make_deck()

hand_player = create_hand(deck)
hand_dealer = create_hand(deck)
print("Player hand: {}".format(hand_player))
print("The dealer shows {}".format(hand_dealer[0]))


'''def make_dealer_hand():
    handDealer.append(card)
    handDealer.append(card)
    return handDealer'''


#hand_dealer = make_dealer_hand()
# handPlayer.append(card)
# handPlayer.append(card)
# handDealer.append(card)
# handDealer.append(card)


def get_player_value(hand):

    d = 0
    for val in hand:
            try:
                val[1] = int(val)
                if val[1] == 1:
                    val[1] = 10
            except ValueError:
                if val[1] == 'A':
                    val[1] = 11
                elif val[1] in 'JQK':
                    val[1] = 10
            d += val[1]
            return val[1]


def player_hit():
    while True:
        choice = input("Do you want to hit? Y/n ")
        if choice != 'n':
            random_card = random.randint(0, 51)
            hand_player.append(deck[random_card])
            print(hand_player)
        else:
            return hand_player

print(player_hit())
print(get_player_value(hand_player))

#def Make_Dealer_Hand(self):
#hand = []
#for card in range(2):
#hand.append(self.Give_Dealer_Card())
#return hand

#if hand.dealer > 21:
    #return "You busted":
#elif 17 < hand.dealer < 20
    #return "Stay"
#else:
    #Give_Dealer_Card()

#Get_Player_Value():

#def Make_Dealer_Hand(self):
    #hand = []
    #for card in range(2):
        #hand.append(self.Give_Dealer_Card())
    #return


"""
        handPlayer < 17:


                # Get_ Dealer_Value():
                # v=0
                # for card in hand:
                #  for val in card[0]:
                #  try:
                #  val = int(val)
                #  if int(val) == 1:
                #  value = 10
                #  except ValueError:
                #  if val == 'a':
                #  val = 11
                #  elif val in 'jqk':
                #  val = 10
                #  v += val
                #  return v

                #  sum player values of hands:
                #  for val in playerHand
                #  sum val+val
                #  for val in playerHand
                #  sum val+val

                #  compare value.handDealer vs. value.handPlayer for round(1,2,3,4)

                #  if hand.player > 21:
                #  return "You busted":
                #  elif 17 < hand.player < 20
                #  return "Stay"
                #  else:
                #  Give_Player_Card(range(0,5)


                #  if hand.dealer > 21:
                #  return "You busted":
                #  elif 17 < hand.dealer < 20:
                #  return "Stay"
                #  else:
                #  Give_Dealer_Card()


                #  ask Player do you want to hit
                #  getplayerinput
                #  Dealer hits automatically
                #  If Dealer busts, print "you Win"
                #  Show_Dealer_Hand
                #  Show_Player_Hand
                #  If Player busts, print "you Lose"

                #  if hand.player > 21:
                #  return "You busted":
                #  elif 17 < hand.player < 20
                #  return "Stay"
                #  else:
                #  Give_Player_Card()

                #  Show_Dealer_Hand
                #  Show_Player_Hand


"""
"""
flat_cards = []
for card_suit in cards:
    for card in card_suit:
        flat_cards.append(card)

print(dict([() for _ in range(52)]))

print(flat_cards)

import random

random.shuffle(flat_cards)
print(flat_cards)


deck = Deck()
deck_creation = deck.make_deck()
hit_one = deck.give_one()
print(deck_creation)
hand_creation = deck.create_hand()
print(hand_creation)
hand_value = deck.get_value(hand_creation)
print(hand_value)


player = Player()
value_player_hand = player.player_hand()
show_player_hand = player.show_player_hand()
print(player.player_hit)


#def Make_Dealer_Hand(self):
#hand = []
#for card in range(2):
#hand.append(self.Give_Dealer_Card())
#return hand

#if hand.dealer > 21:
    #return "You busted":
#elif 17 < hand.dealer < 20
    #return "Stay"
#else:
    #Give_Dealer_Card()

#Get_Player_Value():

#def Make_Dealer_Hand(self):
    #hand = []
    #for card in range(2):
        #hand.append(self.Give_Dealer_Card())
    #return

###if

print(val)
print(suit)


def start(self):
    Game = play_game()
    #unfinished

  def receive_hand(self):
        for card in Deck:
            pop(Deck)

    self.draw()
    self.take_turn()

    self.Hand
    self.add_card()

    self.draw()
    self.add()
    self.randomshuffle()

#Rules

def ask_again:
    print("Would you like to stay or hit again?")

hand = C1 + C2 + '{}/__'
round_1/2/3 = c3/c4/c5


###Functions


def bust_yet(self, hand):
    numbers = []
    if player.hand.val > 21:
        numbers = self.grab_numbers(hand)
		total = sum([num for num in numbers])
		if total > 21:
			return True
		elif total == 21:
			return False
		else:
			return False


def calculate_hand(self, hand):
	    Calculate the score of the hand
        score = self.grab_numbers(hand)
		total = sum([num for num in score])
		return total

self.suits = "chsd"
		self.ranks = '23456789TJQKA'
		self.deck = tuple([''.join(card)
			for card in itertools.product(self.ranks, self.suits)])
		self.hand = random.sample(self.deck, 2)

    def create_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_one())
        return hand

    print([['{}{}'.format(suit, value) for suit in suits] for value in range(1,16)])


"""
