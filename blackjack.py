import random


class Deck:
    suit_of_card = ['пики', 'черви', 'трефы', 'бубны']
    deck_of_cards = [[2, 'двойка'],
                     [3, 'тройка'],
                     [4, 'четверка'],
                     [5, 'пятерка'],
                     [6, 'шестерка'],
                     [7, 'семерка'],
                     [8, 'восьмерка'],
                     [9, 'девятка'],
                     [10, 'десятка'],
                     [10, 'валет'],
                     [10, 'дама'],
                     [10, 'король'],
                     [11, 'туз']
                     ]

    def __init__(self):
        self.total_deck = []
        for i in self.suit_of_card:
            for j in self.deck_of_cards:
                info_card = []
                info_card.extend(j)
                info_card.append(i)
                self.total_deck.append(info_card)

    def choice_card(self):
        card = random.choice(self.total_deck)
        self.total_deck.remove(card)
        return card


class Player:
    def __init__(self, name, type_pl):
        self.name = name
        self.type_pl = type_pl
        self.cards = []
        self.point = 0
        self.total_point = [0, 0, 0]
        self.game = True

    def count_point(self):
        if self.cards[-1][1] == 'туз' and self.point > 21:
            self.point += 1
        else:
            self.point += self.cards[-1][0]


class Game:
    def __init__(self, deck, *players, rate=10):
        self.deck = deck
        self.players = players
        self.rate = rate

    def start_game(self):
        for i in self.players:
            self.first_cards(i)
        self.party_of_game()

    def party_of_game(self):
        while True:
            check = []
            for i_pl in self.players:
                if i_pl.type_pl == 'player' and i_pl.game:
                    self.action(i_pl)

                if i_pl.type_pl == 'computer' and i_pl.game:
                    self.step_comp(i_pl)
                check.append(i_pl.game)
            if True not in check:
                break
        self.result_of_party()

    def first_cards(self, player):         # Выбор первых двух карт
        for i in range(2):
            player.cards.append(deck.choice_card())
            player.count_point()
        if player.type_pl == 'player':
            print('Ваши карты:', end='')
            for mycard in player.cards:
                print(mycard[1], mycard[2], end='.')

    def take_card(self, player):
        new_card = deck.choice_card()
        player.cards.append(new_card)
        player.count_point()
        if player.type_pl == 'player':
            print('Ваша карта:', end='')
            print(new_card[1], new_card[2])

    def action(self, player):
        if player.game:
            print('\nХод игрока')
            action = int(input('Дейстивие:\n1. Взять карту.\n 2. Остановиться\n--->'))
            if action == 1:
                self.take_card(player)
            else:
                player.game = False

    def step_comp(self, comp):
        if comp.point < 21 and comp.game:
            print('\nХод компьютера...')
            action = random.randint(1, 2)
            if action == 1:
                self.take_card(comp)
                print('Компьютер взял карту')
            else:
                print('Компьютер пассует')
                comp.game = False
        else:
            print('_______')
            comp.game = False

    def result_of_party(self):
        print('Результаты партии:')
        winner = [0, 0]
        for i_pl in self.players:
            print(i_pl.name, 'количество очков', i_pl.point)
            if i_pl.point == winner[0]:
                print('Ничья')
                winner[1] = 0
            if i_pl.point <= 21 and i_pl.point > winner[0]:
                winner = [i_pl.point, i_pl.name]
        print('Победитель:', winner[1], winner[0], 'очков')
        self.total_result(winner[1])
        self.end_of_game()

    def total_result(self, name_win):
        for i_pl in self.players:
            if i_pl.name == name_win:
                i_pl.total_point[0] += 1
            if name_win == 0:
                i_pl.total_point[2] += 1
            if i_pl.name != name_win:
                i_pl.total_point[1] += 1


    def total_result_table(self):
        for i_pl in self.players:
            print('У игорока {}: {} Побед, {} Поражений, {} сыграно в ничью'.
                  format(i_pl.name, i_pl.total_point[0], i_pl.total_point[1], i_pl.total_point[2]))

    def end_of_game(self):
        exit_of_game = input('Продолжить игру? (да/нет) ')
        if exit_of_game == 'да':
            for i_pl in self.players:
                i_pl.cards = []
                i_pl.point = 0
                i_pl.game = True
            blackjack.start_game()
        else:
            print('Конец игры')
            self.total_result_table()


deck = Deck()
pl_1 = Player('user', 'player')
pl_2 = Player('computer', 'computer')
blackjack = Game(deck, pl_1, pl_2)

blackjack.start_game()
