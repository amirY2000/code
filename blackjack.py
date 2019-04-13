import random
import copy
def creatdeck():
    cards = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","T♠","J♠","Q♠","K♠","A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","T♥","J♥","Q♥","K♥","A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","T♣","J♣","Q♣","K♣","A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","T♦","J♦","Q♦","K♦"]
    random.shuffle(cards)
    return cards
def dealer_hand():
    deck = creatdeck()
    a = random.randint(0,51)
    hand = []
    hand.append(deck[a])
    deck.remove(deck[a])
    while calc_hand_total(hand) < 21:
        a = random.randint(0,51)
        hand.append(deck[a])
    if calc_hand_total(hand) > 21:
        hand.remove(deck[a])
    return hand
def getValue(card):
    nums = ["2","3","4","5","6",'7','8','9']
    a = card[0]
    if a in nums:
        return int(a)
    elif a == "A":
        return 11
    else:
        return 10

def calc_hand_total(hand):
    mylist = []
    sum = 0
    for i in hand:
        b = getValue(i)
        mylist.append(b)
    for j in mylist:
        sum += j 
    return sum

def show_all_hand(hand):
    string = ""
    for i in hand:
        string += (i+" ")
    return string 

def show_with_hole(hand):
    liist = hand
    string = "XX"
    liist[0] = string
    b = show_all_hand(liist)
    return b
def display_board(board):
    for j in board:
        for c in j:
            print(c,end = " ")
        print()
    print("  --------------------")
    print(" your answer should be yes or no")
    return  "  ====================="
def main():
    dealer = dealer_hand()
    Dealer = copy.deepcopy(dealer)
    hidden = show_with_hole(dealer)
    deck = creatdeck()
    a = random.randint(0,51)
    board = [["  dealer  ","|",hidden,"|","         "],["                                    "],["                                    "],["                                    "],["                                    "],["  player  ","|","      ","|","         "]]
    print(display_board(board))
    play = input("Are you ready to play ? ")
    if play == "no":
        print("see you later !")
    elif play == "yes":
        player_hand = []
        player_hand.append(deck[a])
        board = [["  dealer  ","|",show_with_hole(dealer),"|","         "],["                                    "],["                                    "],["                                    "],["                                    "],["  player  ","|",show_all_hand(player_hand),"|","         "]]
        print(display_board(board))
        con = input("Do you want to continiue ? ")
        while con == "yes" and calc_hand_total(player_hand) <= 21:
            v = random.randint(0,51)
            player_hand.append(deck[v])
            if calc_hand_total(player_hand) > 21:
                break
            board = [["  dealer  ","|",show_with_hole(dealer),"|","         "],["                                    "],["                                    "],["                                    "],["                                    "],["  player  ","|",show_all_hand(player_hand),"|","         "]]
            print(display_board(board))
            con = input("Do you want to continiue ? ")
        board = [["  dealer  ","|",show_all_hand(Dealer),"|","         "],["                                    "],["                                    "],["                                    "],["                                    "],["  player  ","|",show_all_hand(player_hand),"|","         "]]
        print(display_board(board))
        if con == "yes":
            if calc_hand_total(player_hand) == 21 and len(player_hand) == 2:
                print("congratulation you are Black Jack!")
            elif calc_hand_total(player_hand) == 21 and calc_hand_total(dealer) != 21:
                print("hey you won! you are 21 :)")
            elif calc_hand_total(player_hand) == 21 and calc_hand_total(dealer) == 21:
                print("wow both 21 :O, Draw!")
            elif calc_hand_total(player_hand) > 21:
                print("Game over! your hand is greater than 21 :(")
            elif calc_hand_total(player_hand) < 21:
                if calc_hand_total(player_hand) > calc_hand_total(Dealer):
                    print("hey you won :)")
                elif calc_hand_total(player_hand) < calc_hand_total(Dealer):
                    print("Dealer won!")
                else:
                    print("Draw :|")
        elif con == "no":
            if calc_hand_total(player_hand) == 21 and len(player_hand) == 2:
                print("congratulation you are Black Jack!")
            if calc_hand_total(player_hand) == 21 and calc_hand_total(dealer) != 21:
                print("hey you won! you are 21 :)")
            elif calc_hand_total(player_hand) > 21:
                print("Game over! your hand is greater than 21 :(")
            elif calc_hand_total(player_hand) < 21:
                if calc_hand_total(player_hand) > calc_hand_total(Dealer):
                    print("hey you won :)")
                elif calc_hand_total(player_hand) < calc_hand_total(Dealer):
                    print("Dealer won!")
                else:
                    print("Draw :|")
if __name__ == "__main__":
    main()