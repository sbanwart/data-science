def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def partial_difference_quotient(f, v, i, h):1
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0) # add h to just the ith element of vars
        for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h 

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
        for i, _ in enumerate(v)]

def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size + direction_i
        for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

def safe(f):
    """return a new function that's the same as f, except that it outputs infinity whenever f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf') # this means "infinity" in Python
    return safe_f
    