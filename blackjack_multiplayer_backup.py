'''

BlackJack Game

User Stories:

1) User can play the blackjack game in terminal against the dealer
2) Dealer automatically plays his hand with a fixed algorithm (If it's 16 or below they hit, if it's above 16, they stay)
3) User can play the blackjack game repeatedly
4) User can choose to hit or stay
5) User can see what cards they have been dealt
6) User can only see one dealer card, not the bottom card

Tips:
1) Aces can count as an eleven or a one - but it only counts as a one if your score is over 21
2) Research random.shuffle()
3) You are not allowed to code until you design your program!
4) Research __radd__ - it is a built-in method in Python

Extension:
1) Multiple users can play blackjack game in terminal in a turn-based game
2) Consider using the stack data structure
3) User can bet dollar amounts in the blackjack game


'''


import random



suits = ('c','s','h','d')
ranks = ('2','3','4','5','6','7','8','9','10','j','q','k','a')

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def __repr__(self):
        return self.suit + self.rank

    def __radd__(self,other):
        pass
        
    def value(self):
        try:
            return int(self.rank)
        except:
            if self.rank == 'a':
                return 11
            else:
                return 10                       

# c = Card('c', 'a')
# print c.value()

class Deck:
    def __init__(self):
        self.suits = suits
        self.ranks = ranks
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit, rank)
                self.deck.append(card)
        

    def shuffle(self):
        random.shuffle(self.deck)


    def one(self):
        "get one card"
        self.card = self.deck.pop()
        return self.card
# d = Deck()        
# d.shuffle()
#d.one()

class Player:
    def __init__(self,name):
        self.player = name
        self.hand_list = []

    def __str__(self):
        "optional"
        return self.player

    def __lt__(self,other):
        pass
    
    def get(self,card):
        "adds a card to the users hand"
        self.hand_list.append(card)
        return self.hand_list

    def choose(self):
        "ui, ask user to hit or stand"
        self.choice = str(raw_input("hit or stand?"))
        self.choice = self.choice.lower()
        if self.choice == 'hit':
            print "You want a hit"
            return True
        else:
            print "You want to stand"
            return False

    def hand(self):
        # print "this is the hand" , self.hand_list
        self.total_value = 0
        for card in self.hand_list:
            self.total_value = self.total_value + card.value()
        #print self.total_value
        return self.total_value
        ''' add all the values in hand that are not aces, if total would put you over, make it a 1, else add the 11*evaluate aces one by one'''
    
    def bust(self):
        "did the user bust"
        if self.total_value > 21:
            return True
        else:
            return False

    def won(self):
        "do they have 21"
        if self.total_value == 21:
            return True
        else:
            return False

# p = Player(name = "Anabell")

# p.hand()
# p.choose()
# p.bust()

class Dealer(Player):
    def __init__(self,name):
       Player.__init__(self,name)

    def __str__(self):
        "optional"
        pass

    def choose(self):
        "computer logic to decide to hit or stay"
        #if dealer hand < 16:
        if self.hand() < 16:
            #print "Dealer's will hit"
            return True
        else:
            #print "Dealer will stay"
            return False
     
    
class Game:
    def __init__(self):
        "Game setup, adds players and a dealer"
        # self.Player1 = Player(name = raw_input("Enter your name: "))
        self.dealer1 = Dealer("Dealer")
        self.d = Deck()        
        self.d.shuffle()
        num_players = int(raw_input("Enter number of Players"))
        #for each player, create an instance of class player
        self.playerlist = []
        for x in range(num_players):
            self.playerlist.append(Player(x))
        self.playerlist.append(self.dealer1)
        self.play()
    
    # def print_table(self,player):
    #     "helper method to print out all the players hands"
    
    def results(self, player):        
            if player.bust() == True:
                print "player:", player.player, " BUST!!"
            if player.won() == True:
                print "player:", player.player, ", YOU WON!!"
            elif player.hand() > self.dealer1.hand() or player.won() == True:
                print "player:", player.player, " beat the dealer!"
            elif player.hand() < self.dealer1.hand():
                print "player:", player.player, "The Dealer beat you"
    
    def deal(self):
        "deal to all players"
        for x in range(2):
            self.dealer1.get(self.d.one())
            for player in self.playerlist:
                player.get(self.d.one())
        print "\n CARDS DEALT \n"
        for player in self.playerlist[:-1]:
            print "\n"
            print player.player,  "'s hand:" , player.hand_list , "Total Value: " , player.hand(),"\n"
        print "\nDealer's card: ", self.dealer1.hand_list[0], "\n"
                # ADD DEALER TO THE END OF THE list
    def play(self):
        "top level, manages the game"
        
        print "\n WELCOME TO BLACKJACK \n"
        
        
        self.deal()
        
        for player in self.playerlist:
            print "\nPlayer : ", player.player
            print "Your hand:" , player.hand_list
            print "Your Value:", player.hand(), "\n"
            while player.bust() == False and player.choose() == True:
                player.get(self.d.one())
                print "Your hand:" , player.hand_list
                print "Your Value:", player.hand(), "\n"
                print "Player : ", player.player, "\n"
                if player.bust() == True:
                    print "YOU BUSTED!! ***END OF TURN***\n"
            # else:
            #     while player.bust() == False and player.choose() == True:
            #     player.get(self.d.one())
            #     print "\nDealer's hand:" , self.dealer1.hand_list, "\n"
            #     print "Dealers Value:", self.dealer1.hand()
        
        print "\n ****************SCOREBOARD*********************" 
        for player in self.playerlist:
            self.results(player)

g = Game()



    
