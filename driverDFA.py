from DFA import DFA, Transition, State

q1 = State("Q1", False)
q2 = State("Q2", True)
q3 = State("Q3", True)

t1 = Transition(q1, q2, 'a')
t2 = Transition(q1, q3, 'b')
t3 = Transition(q2, q2, 'a')
t4 = Transition(q3, q3, 'b')

transitions = {t1, t2, t3, t4}

dfa = DFA(transitions, q1)
print(dfa.Eval("a"))
dfa.Draw()
