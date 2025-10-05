import pulp

m = pulp.LpProblem("Confitures", pulp.LpMaximize)
x1 = pulp.LpVariable("x1", lowBound=175)
x2 = pulp.LpVariable("x2", lowBound=160)
x3 = pulp.LpVariable("x3", lowBound=150)
y1 = pulp.LpVariable("y1", lowBound=0)
y2 = pulp.LpVariable("y2", lowBound=0)

m += 1.6*x1 + 1.4*x2 + 1.2*x3 + 2.0*y1 + 1.9*y2
m += x1 + 0.5*y1 + 0.5*y2 <= 1000
m += x2 + 0.5*y1 <= 600
m += x3 + 0.5*y2 <= 800

m.solve()

for v in m.variables():
    print(v.name, "=", v.value())
print("Z =", pulp.value(m.objective))
