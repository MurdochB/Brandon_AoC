input = "4-input.txt";

input_file = open(input ,"r")

# Sort file
sorted_lines = sorted(input_file.readlines())


sleep_dicts = {}
sleep_count = {}

guard = ""
sleep_start = ""
sleep_end = ""

for line in sorted_lines:
    if("Guard" in line):
        guard = line[line.index("Guard #")+7:line.index(" begins")]
    if("falls asleep" in line):
        sleep_start = line[line.index(":")+1:line.index("]")]
    if("wakes up" in line):
        sleep_end = line[line.index(":")+1:line.index("]")]
        if (guard not in sleep_dicts):
            sleep_dicts[guard] = []
            sleep_count[guard] = 0
        sleep_dicts[guard].append("From " + sleep_start + " To " + sleep_end)
        sleep_count[guard] = sleep_count[guard] + (int(sleep_end) - int(sleep_start) - 1)

# find the biggest sleeper:
biggest_sleeper = ""
max_sleep = 0;
for g in sleep_count:
    if (sleep_count[g] > max_sleep):
        max_sleep = sleep_count[g]
        biggest_sleeper = g

print "The biggest sleeper is: " + biggest_sleeper

# Now find the most common time asleep

print sleep_dicts[biggest_sleeper]
