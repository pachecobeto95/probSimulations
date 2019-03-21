#Author: Roberto Pacheco
#Date: 18/02/2019
#Last modified: 18/02/2019

import random, scipy.stats, sys
#import pandas as pd
import numpy as np

def confidence_interval(data, confidence=0.95):
    data = 1.0 * np.array(data)
    n = len(data)
    mean, se = np.mean(data), scipy.stats.sem(data)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return mean, h



#create object card with a number's card and sign
class Card(object):
	def __init__(self, number, sign):
		self.number = number
		self.sign = sign

#create the experiment's object
class CardsPoker(object):
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

	def royalFlush(self):
		singlePair = 0
		royalFlushList = [1,10,11,12,13]
		for interaction in range(self.NR_INTERACTIONS):
			count = 0
			deck = self.deckGenerator()
			hand = []
			handSign = []
			for i in range(self.SIZE_HAND):
				card = deck[i].number
				cardSign = deck[i].sign
				hand.append(card)
				handSign.append(cardSign)
				if(len(hand) == self.SIZE_HAND):
					if(handSign[1:] == handSign[:-1]):
						hand = sorted(hand)
						if(hand == royalFlushList):
							print(hand)
							count+=1

	def straightFlush(self):
		straightFlushList2 = []
		for i in range(1,11):
			straightFlushList = []
			for j in range(i, i+5):
				straightFlushList.append(j)
			straightFlushList2.append(straightFlushList)
		count = 0
		for interaction in range(self.NR_INTERACTIONS):
			deck = self.deckGenerator()
			hand = []
			handSign = []
			for i in range(self.SIZE_HAND):
				card = deck[i].number
				cardSign = deck[i].sign
				hand.append(card)
				handSign.append(cardSign)
				if(len(hand) == self.SIZE_HAND):
					if(handSign[1:] == handSign[:-1]):
						hand = sorted(hand)
						if(hand in straightFlushList2):
							count+=1

		#counting if exist only one pair
		probability = float(count)/float(NR_INTERACTIONS)
		return probability


	def flush(self):
		count=0
		for interaction in range(self.NR_INTERACTIONS):
			deck = self.deckGenerator()
			handSign = []
			for i in range(self.SIZE_HAND):
				card = deck[i].number
				cardSign = deck[i].sign
				handSign.append(cardSign)
				if(len(handSign) == self.SIZE_HAND):
					if(handSign[1:] == handSign[:-1]):
						count+=1
		probability = float(count)/float(NR_INTERACTIONS)
		return probability

	def straight(self):
		straightFlushList2 = []
		for i in range(1,11):
			straightFlushList = []
			for j in range(i, i+5):
				straightFlushList.append(j)
			straightFlushList2.append(straightFlushList)
		count = 0
		for interaction in range(self.NR_INTERACTIONS):
			deck = self.deckGenerator()
			hand = []
			handSign = []
			for i in range(self.SIZE_HAND):
				card = deck[i].number
				cardSign = deck[i].sign
				hand.append(card)
				handSign.append(cardSign)
				if(len(hand) == self.SIZE_HAND):
					hand = sorted(hand)
					if(hand in straightFlushList2):
						count+=1
		probability = float(count)/float(NR_INTERACTIONS)
		return probability

	def fourOfKind(self):
		fourKindCount = 0
		for interaction in range(self.NR_INTERACTIONS):
			count = 0
			deck = self.deckGenerator()
			for i in range(self.SIZE_HAND):
				for j in range(i+1, self.SIZE_HAND):
					card1 = deck[i].number
					card2 = deck[j].number
					#counting a existed pair
					if(card1 == card2):
						count+=1
			if(count == 4):
				fourKindCount+=1
		#counting if exist only one pair
		probability = float(fourKindCount)/float(NR_INTERACTIONS)
		return probability

	def threeOfKind(self):
		fourKindCount = 0
		for interaction in range(self.NR_INTERACTIONS):
			count = 0
			deck = self.deckGenerator()
			for i in range(self.SIZE_HAND):
				for j in range(i+1, self.SIZE_HAND):
					card1 = deck[i].number
					card2 = deck[j].number
					#counting a existed pair
					if(card1 == card2):
						count+=1
			if(count == 3):
				fourKindCount+=1
		#counting if exist only one pair
		probability = float(fourKindCount)/float(NR_INTERACTIONS)
		return probability

	#one pair experiment
	def onePair(self):
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

	#one pair experiment
	def twoPair(self):
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

	def noPair(self):
		count = 0
		for interaction in range(self.NR_INTERACTIONS):
			deck = self.deckGenerator()
			cardList = []
			for i in range(self.SIZE_HAND):
				card = deck[i].number
				cardList.append(card)	
			if(len(set(cardList)) != len(cardList)):
				count+=1

		probability = float(count)/float(NR_INTERACTIONS)
		return probability



QNTD_NUMBER = 13
SIGN_LIST = ["copa", "ouro", "espada", "paus"]
NR_INTERACTIONS = 10000
SIZE_HAND = 5
NR_EXPERIMENT = 100
probabilityList = []

for k in range(NR_EXPERIMENT):
	experiment = CardsPoker(QNTD_NUMBER, SIGN_LIST, NR_INTERACTIONS, SIZE_HAND)
	#royalFlush = experiment.royalFlush()
	straightFlush = experiment.straightFlush()
	#flush = experiment.flush()
	#straight = experiment.straight()
	#onePair = experiment.onePair()
	#twoPair = experiment.twoPair()
	#threeOfKind = experiment.threeOfKind()
	#fourOfKind = experiment.fourOfKind()
	#nopair = experiment.noPair()
	probabilityList.append(nopair)

mean, h = confidence_interval(probabilityList)
print("O intervalo de confianca: [%s, %s]"%(mean-h, mean+h))
