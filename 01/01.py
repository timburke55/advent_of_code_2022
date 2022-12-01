
current_total = 0
totals = [0,0,0]
with open("01/day_1_input.txt", "r") as input:
    
    for line in input:
        line = line.strip()
        if line == "":
            if current_total > totals[0]:
                totals[0] = current_total
                totals.sort()
            current_total = 0
        else:
            current_total += int(line)
    sum_total = sum(totals)
    print(sum_total)