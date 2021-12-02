from NFA import NFA

#NFA setup
#Each state is an integer
q0 = 0
q1 = 1
q2 = 2
q3 = 3
q4 = 4

#set of possible states
Q = {q0, q1, q2, q3, q4}

#Start state
q = q0

#Accepted symbols
sigma = {'a', 'b'}

#Final state
F = {q3}

#Transition function
#Does not require a transition for each symbol for each state.
#'e' is epsilon
#DOES require that each epsilon transition is in a set like q0:{'e':{q1, q2}}
transitions = { q0 : {'e': {q1, q2}},
		q1 : {'a':q1, 'b':q3},
		q2 : {'a':q2, 'b':q3},
		q3 : {'a':q3, 'e':{q4} },
		q4 : {'a':q3, 'b':q4}
}

#Construction of NFA Class
nfa = NFA(Q, sigma, q, F, transitions)
print(nfa.Accept('aaaaaaaaab'))
nfa.Draw('NFA')
