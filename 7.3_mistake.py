def compute_patterns(inputs=None, pattern="new pattern"):
    if inputs is None:
        inputs = ["a list based on "]
    inputs[0] += pattern
    print(*inputs)

compute_patterns()
compute_patterns()

# OR

def compute_patterns(inputs=None, pattern="new pattern"):
    if inputs is None:
        inputs = []
    inputs.append(pattern)
    patterns = ["a list based on "] + inputs
    print(*patterns, sep="")

compute_patterns()
compute_patterns()
