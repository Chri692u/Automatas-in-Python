import os
import random

class NFA:
	def __init__(self, Q, sigma, q, F, delta):
		self.Q = Q #A finite set of states
		self.Symbols = sigma.union('e') #A set of input symbols + epsilon
		self.Start = q #An initial state
		self.Final = F #A set of final states
		self.Delta = delta #Transition functions implemented as a dictionary of hashmaps

	def Eval(self):
		valid = False
		empty = {}

		#If no final states or states at all
		if self.Final == empty or self.Q == empty:
			return False

		#If each state can transition on atleast one symbols
		#And all transitions are valid
		for key in self.Delta:
			transition = self.Delta[key]
			for sym in transition:
				if sym in self.Symbols:
					valid = True
				else:
					return False
		return valid

	def Accept(self, inputString):
		if not self.Eval():
			return False

		currentState = self.Start
		possibleStates = []

		for i in inputString:
			for sym in self.Delta[currentState].keys():
				if sym == 'e':
					for state in self.Delta[currentState][sym]:
						possibleStates.append(state)
				else:
					try:
						possibleStates.append(self.Delta[currentState][i])
					except:
						print("No transition for " + str(i))			
			#pick random current state, this is very limited nondeterminism
			print(currentState)
			print(possibleStates)	
			possibleListLength = len(possibleStates)
			currentState = possibleStates.pop(random.randint(0, possibleListLength - 1))	
		
		#Did we reach a final state?
		for state in possibleStates:
			if state in self.Final:
				return True

		return False

	def Draw(self, filename):
		#Only draw if DFA is valid
		if not self.Eval():
			return False

		#Make .dot string
		s = "Digraph DFA {\n"
		#Draw states
		for state in self.Q:
			if state == self.Start:
				s = s + f"{self.Start} [shape=circle style=filled fillcolor=lightblue]\n"
			else:
				s  = s + f"{state} [shape=circle]\n"
		#Special case for final states
		for f in self.Final:
			s  = s + f"{f} [shape=doublecircle]\n"
		
		#Draw transitions
		for state in self.Delta:
			for sym in self.Symbols:
				try:
					s = s + f"{state} -> {self.Delta[state][sym]} [label=\"{sym}\"]\n"
				except:
					print("No transition for " + str(sym))		
		s = s + "}"

		#Make svg file
		os.system(f"echo '{s}' > DFA.dot")
		os.system(f"dot -Tsvg DFA.dot > {filename}.svg")
		os.system("rm DFA.dot")
		
		return True
