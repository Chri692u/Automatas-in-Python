from DFA import DFA

#DFA setup
#Each state is an integer
q0 = 0
q1 = 1
q2 = 2
Ø = 3

#Set of possible states
Q = {q0, q1, q2, Ø}

#Start state
q = q0

#Accepted symbols
sigma = set(('a', 'b'))

#Final state
F = set((q1, q2))

#Transition function
#Requires a transition for each symbol for each state
transitions = { q0 : {'a':q1, 'b':q2},
		q1 : {'a':q1, 'b':Ø},
		q2 : {'a':Ø, 'b':q2},
		Ø  : {'a':Ø, 'b':Ø}}

#Construction of DFA class
dfa = DFA(Q, sigma, q, F, transitions)

print(dfa.Eval())
print(dfa.Accept('aaaaaaaa'))
dfa.Draw('DFA')
