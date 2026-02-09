class ConstraintSatisfactionProblem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for constraint in self.constraints.get(variable, []):
            if not constraint(variable, value, assignment):
                return False
        return True

    def backtrack(self, assignment): 
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                assignment.pop(var)  # backtrack

        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def order_domain_values(self, variable, assignment):
        return self.domains[variable]


# ---------------- Example Usage ----------------

variables = ['A', 'B', 'C']

# Domains with color names
domains = {
    'A': ['Red', 'Green', 'Blue'],
    'B': ['Red', 'Green', 'Blue'],
    'C': ['Red', 'Green', 'Blue']
}

# Constraints: neighboring variables must have different colors
constraints = {
    'A': [
        lambda var, val, ass: 'B' not in ass or ass['B'] != val
    ],
    'B': [
        lambda var, val, ass: 'A' not in ass or ass['A'] != val,
        lambda var, val, ass: 'C' not in ass or ass['C'] != val
    ],
    'C': [
        lambda var, val, ass: 'B' not in ass or ass['B'] != val
    ]
}

# Solve CSP
csp = ConstraintSatisfactionProblem(variables, domains, constraints)
solution = csp.backtrack({})

if solution:
    print("Solution found:")
    for variable, value in solution.items():
        print(f"{variable}: {value}")
else:
    print("No solution found.")
