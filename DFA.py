import os

class State:
	def __init__(self, label, isAccepting):
		self.Label = label
		self.AcceptState = isAccepting

class Transition:
	def __init__(self, fromState, toState, condition):
		self.To = toState
		self.From = fromState
		self.Condition = condition
	
	def Eval(self, input):
		if self.Condition == input:
			return True
		else:
			return False
	
class DFA:
	def __init__(self, transitions, startState):
		self.StartState = startState
		self.Transitions = transitions
 	
	def Eval(self, inputString):
		accepted = False
		#Find start states transition
		for t in self.Transitions:
			if t.From.Label == self.StartState.Label:
				currentTransition = t
				currentState = currentTransition.From
				break
		
		#Test currentTransition with input string
		for i in range(len(inputString)):
			for t in self.Transitions:
				if t.Eval(inputString[i]) and (currentTransition.From.Label == currentState.Label):
					#Update current transition and state
					currentTransition = t
					currentState = currentTransition.To

					if currentState.AcceptState == True:
						accepted = True
						break

				else:
					accepted = False
		
		return accepted
	
	def Draw(self):
		#Make .dot string
		s = "Digraph DFA {\n"
		for t in self.Transitions:
			if t.From.Label == self.StartState.Label:
				s = s + f"{t.From.Label} [shape=circle style=filled fillcolor=lightblue]\n"
			if t.To.AcceptState == True:
				s  = s + f"{t.To.Label} [shape=doublecircle]\n"

			s = s + f"{t.From.Label} -> {t.To.Label} [label=\"{t.Condition}\"]\n"
		s = s + "}"

		#Make svg file
		os.system(f"echo '{s}' > DFA.dot")
		os.system(f"dot -Tsvg DFA.dot > out.svg")
		os.system("rm DFA.dot")
