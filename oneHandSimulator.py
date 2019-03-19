#Author: Roberto Pacheco
#Date: 18/02/2019
#Last modified: 18/02/2019

import random

#create object card with a number's card and sign
class Card(object):
	def __init__(self, number, sign):
		self.number = number
		self.sign = sign

#create the experiment's object
class OnePairExperiment(object):
	def __init__(self, qntdNumber, signList, NR_INTERACTIONS, SIZE_HAND):
		self.qntdNumber = qntdNumber
		self.signList = signList
		self.NR_INTERACTIONS = NR_INTERACTIONS
		self.SIZE_HAND = SIZE_HAND

	#generate shuffled deck
	def deckGenerator(self):
		deck = []
		for i in range(1, self.qntdNumber):
			for j in self.signList:
				deck.append(Card(i,j))
		random.shuffle(deck)
		return deck

	#one pair experiment
	def OnePairProb(self):
		singlePair = 0
		for interaction in range(self.NR_INTERACTIONS):
			pair = 0
			deck = self.deckGenerator()
			for i in range(self.SIZE_HAND):
				for j in range(i+1, self.SIZE_HAND):
					card1 = deck[i].number
					card2 = deck[j].number
					#counting a existed pair
					if(card1 == card2):
						pair+=1
			#counting if exist only one pair
			if(pair == 1):
				singlePair+=1
		probability = float(singlePair)/float(NR_INTERACTIONS)
		return probability


QNTD_NUMBER = 13
SIGN_LIST = ["copa", "ouro", "espada", "paus"]
NR_INTERACTIONS = 10000
SIZE_HAND = 5

onePair = OnePairExperiment(QNTD_NUMBER, SIGN_LIST, NR_INTERACTIONS, SIZE_HAND)
probOneHand = onePair.OnePairProb()
print("A probabilitade do evento de aparecer somente um par: %s"%probOneHand)

















