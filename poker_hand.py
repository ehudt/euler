#from itertools import defaultdict
from collections import Counter, defaultdict

ranks = {
			'high card' : 1,
			'one pair' : 2,
			'two pairs' : 3,
			'three of a kind' : 4,
			'straight' : 5,
			'flush' : 6,
			'full house' : 7,
			'four of a kind' : 8,
			'straight flush' : 9,
	}

cards_str = ['Nothing', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

class Card(object):
	"""Represents a card in a deck"""
	def __init__(self, num, color):
		super(Card, self).__init__()
		self.num = cards_str.index(num) + 1
		self.color = color
		self.repr = num + color
	def get_num(self):
		return self.num
	def __repr__(self):
		return self.repr
	def __sub__(self, other):
		return self.get_num() - other.get_num()
		
class PokerHand(object):
	"""Represent a poker hand"""
	def __init__(self, cards):
		super(PokerHand, self).__init__()
		self.cards = cards
		self.counter = Counter(''.join(map(str,cards)))
		self.rank, self.rank_value = self.get_rank()
	def high_card(self):
		return max(self.cards, key=lambda card : card.get_num())
	def low_card(self):
		return min(self.cards, key=lambda card : card.get_num())
	def is_flush(self):
		return 	self.counter['D'] == 5 or \
				self.counter['H'] == 5 or \
				self.counter['C'] == 5 or \
				self.counter['S'] == 5
	def is_straight(self):
		if self.high_card() - self.low_card() != 4:
			return False
		for c, count in self.counter.iteritems():
			if c in cards_str and count > 1:
				return False
		return True
	def get_rank(self):
		is_straight = self.is_straight()
		is_flush = self.is_flush()
		if is_straight and is_flush:
			return 'straight flush', self.high_card().get_num()
		sets = defaultdict(lambda : 0)
		represent = defaultdict(lambda : [])
		for c, count in self.counter.iteritems():
			if count > 1 and c in cards_str:
				sets[count] += 1
				represent[count].append(cards_str.index(c) + 1)
		if sets[4] == 1:
			return 'four of a kind', represent[4][0]
		if sets[3] == 1 and sets[2] == 1:
			return 'full house', represent[3][0]
		if is_flush:
			return 'flush', self.high_card().get_num()
		if is_straight:
			return 'straight', self.high_card().get_num()
		if sets[3] == 1:
			return 'three of a kind', represent[3][0]
		if sets[2] == 2:
			return 'two pairs', max(represent[2])
		if sets[2] == 1:
			return 'one pair', represent[2][0]
		return 'high card', self.high_card().get_num()
	def __cmp__(self, other):
		if ranks[self.rank] != ranks[other.rank]:
			return ranks[self.rank] - ranks[other.rank]
		else:
			return self.rank_value - other.rank_value
	def __repr__(self):
		return ' '.join(map(str, self.cards))
				
def main():
	f = open("poker.txt")
	player1_wins = 0
	for line in f:
		all_cards = line.strip("\n").split()
		player1 = PokerHand([Card(s[0], s[1]) for s in all_cards[:5]])
		print 'Player 1:', player1
		player2 = PokerHand([Card(s[0], s[1]) for s in all_cards[5:]])
		print 'Player 2:', player2
		if player1 > player2:
			print 'Winner: Player 1,', player1.rank
			player1_wins += 1
		else:
			print 'Winner: Player 2', player2.rank
	print player1_wins

if __name__ == '__main__':
	main()