import copy
input = "7-input.txt";


input_file = open(input ,"r")

requirements = {
'A': [],
'B': [],
'C': [],
'D': [],
'E': [],
'F': [],
'G': [],
'H': [],
'I': [],
'J': [],
'K': [],
'L': [],
'M': [],
'N': [],
'O': [],
'P': [],
'Q': [],
'R': [],
'S': [],
'T': [],
'U': [],
'V': [],
'W': [],
'X': [],
'Y': [],
'Z': []}
requirements_len = {
'A': 61,
'B': 62,
'C': 63,
'D': 64,
'E': 65,
'F': 66,
'G': 67,
'H': 68,
'I': 69,
'J': 70,
'K': 71,
'L': 72,
'M': 73,
'N': 74,
'O': 75,
'P': 76,
'Q': 77,
'R': 78,
'S': 79,
'T': 80,
'U': 81,
'V': 82,
'W': 83,
'X': 84,
'Y': 85,
'Z': 86}

# Create list of requirements
for line in input_file:
    preReq = line[line.index("Step ")+5:line.index(" must")]
    req = line[line.index("before step ")+12:line.index(" can")]
    if (req in requirements):
        requirements[req].append(preReq)
    else:
        requirements[req] = [preReq]

# take a snapshot of the requirements before building the job string
requirements_copy = copy.deepcopy(requirements)

def getStepWithNoPreReq(prev_steps):
    steps = []
    for step in requirements:
        if (requirements[step] == []):
            steps.append(step)
    return sorted(steps)

workers = ['.', '.', '.', '.', '.']
steps = []
joblist = ""
while (len(joblist) < 26):
    steps = getStepWithNoPreReq(steps)
    # asign job to available_worker
    for s in steps:
        for w in workers:
            if (workers[w] == '.'):
                print "worker available"
                workers[w] == s
                requirements[s].append("-")
    # make workers do work
    for w in workers:
        if (workers[w] != '.'):
            requirements_len[workers[w]] = requirements_len[workers[w]] - 1
            if (requirements_len[workers[w]] == 0):
                joblist = joblist + workers[w]
                print "job " + workers[w] + " done"
                for req in requirements:
                    if (workers[w] in requirements[req]):
                        requirements[req].remove(workers[w])

print joblist
print requirements_copy
