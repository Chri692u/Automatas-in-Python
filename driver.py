from DFA import DFA

# DFA setup
q0 = 0
q1 = 1
q2 = 2
Ø = 3

Q = set((q0, q1, q2, Ø))
q = q0
sigma = set(('a', 'b'))
F = set((q1, q2))

transitions = { q0 : {'a':q1, 'b':q2},
		q1 : {'a':q1, 'b':Ø},
		q2 : {'a':Ø, 'b':q2},
		Ø  : {'a':Ø, 'b':Ø}}

dfa = DFA(Q, sigma, q, F, transitions)

print(dfa.Eval())
print(dfa.Accept('aaaaaaaa'))
dfa.Draw('DFA')


#NFA setup
q0 = 0
q1 = 1
q2 = 2
q3 = 3

Q = set((q0, q1, q2, q3, Ø))
q = q0
sigma = set(('a', 'b'))
F = set((q3))

#Does not require a transition for each state in the NFA. e is epsilon
transitions = { q0 : {'e':q1, 'e':q2},
		q1 : {'a':q1, 'b':q3},
		q2 : {'b':q2, 'a':q3},
		q3 : {'a':q3}
}

nfa = NFA(Q, sigma, q, F, transitions)
