# kerolos Amgad

import random
from art import logo

def deal_card():
    """
    the function of deal crd  is to  get card in random way
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card):
    """
    take the card and get the value of this card
    then return it's value
    """
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(com_score, ply_score):
    """
    is comparing between you and computer
    and return who win

    """
    if com_score == ply_score:
        return "Draw"
    elif com_score == 0:
        return "Lose, opponent has BlackJack"
    elif ply_score == 0:
        return "Win, you have BlackJack"
    elif ply_score > 21:
        return "You went over, you lose"
    elif com_score > 21:
        return "Opponent went over, you win"
    elif ply_score > com_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    player_cards = []
    computer_cards = []
    is_game_over = False # Boolean

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        print(logo)
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {player_cards}, current score {player_score}")
        print(f"First card of computer {computer_cards[0]}")

        if computer_score == 0 or player_score == 0 or player_score > 21:
            is_game_over = True
        else:
            choice_player = input("Type 'y' to get a new card or 'n' to pass: ").lower()
            if choice_player == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {player_cards}, final score {player_score}")
    print(f"Opponent's final hand {computer_cards}, final score {computer_score}")
    print(compare(computer_score, player_score))

while input("Do you want to play again? Type 'y' to play or 'n' to end: ").lower() == 'y':
    print("\n" * 20)
    play_game()