input = "4-input.txt";

input_file = open(input ,"r")

# Sort file
sorted_lines = sorted(input_file.readlines())


sleep_dicts = {}
guard = ""
sleep_start = ""
sleep_end = ""

for line in sorted_lines:
    if("Guard" in line):
        guard = line[line.index("Guard #")+7:line.index(" begins")]
    if("falls asleep" in line):
        sleep_start = line[line.index("[")+1:line.index("]")]
    if("wakes up" in line):
        sleep_end = line[line.index("[")+1:line.index("]")]
        print guard + "slept from " + sleep_start + " to " + sleep_end
        if (guard not in sleep_dicts):
            sleep_dicts[guard] = []
        sleep_dicts[guard].append("From " + sleep_start + " To " + sleep_end)

print sleep_dicts

# Now I have a dictionary of guards, with all the times they sleep
{
    '3251': ['From 1518-02-03 00:05 To 1518-02-03 00:34'],
    '479': ['From 1518-02-04 00:14 To 1518-02-04 00:27', 'From 1518-02-04 00:42 To 1518-02-04 00:58'],
    '137': ['From 1518-02-01 00:39 To 1518-02-01 00:55']
}
