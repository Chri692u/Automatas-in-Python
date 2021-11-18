from DFA import DFA

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
