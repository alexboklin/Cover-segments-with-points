n = int(input())
lines = [[int(x) for x in input().split()] for i in range(n)]
sorted_lines = sorted(lines, key=lambda item: item[1])

result = [sorted_lines[0]]
for line in sorted_lines:
	rightmost_line = result[-1]
	if rightmost_line[1] < line[0]:
		result.append(line)
print(len(result))
print(" ".join(str(x[1]) for x in result))
