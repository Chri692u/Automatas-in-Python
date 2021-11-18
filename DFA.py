import os

class DFA:
	def __init__(self, Q, sigma, q, F, delta):
		self.Q = Q #A finite set of states
		self.Symbols = sigma #A set of input symbols
		self.Start = q #An initial state
		self.Final = F #A set of final states
		self.Delta = delta #Transition functions implemented as a dictionary of hashmaps
 	
	def Eval(self):
		valid = False
		empty = set()

		#If no final states or states at all
		if self.Final == empty or self.Q == empty:
			print("DFA invalid")
			return False

		#If each state can transition on every symbol in sigma
		for key in self.Delta:
			transition = self.Delta[key]
			transitionSpace = set()
			for sym in transition:
				transitionSpace.add(sym)

			if transitionSpace == self.Symbols:
				valid = True
			else:
				return False
		
		return valid

	def Accept(self, inputString):
		if not self.Eval():
			return
		
		currentState = self.Start
		for i in inputString:
			currentState = self.Delta[currentState][i]
		return currentState in self.Final

	def Draw(self, filename):
		#Only draw if DFA is valid
		if not self.Eval():
			print("DFA invalid")
			return

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
				s = s + f"{state} -> {self.Delta[state][sym]} [label=\"{sym}\"]\n"
		s = s + "}"

		#Make svg file
		os.system(f"echo '{s}' > DFA.dot")
		os.system(f"dot -Tsvg DFA.dot > {filename}.svg")
		os.system("rm DFA.dot")
		
