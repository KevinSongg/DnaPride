differentInputs = int(input())
 
for t in range(differentInputs):
	output = ""
	numBases = int(input())
	sequence = input()
	for n in range(numBases):
		c = sequence[n]
		if c == "A":
			output += "T"
		elif c == "T":
			output += "A"
		elif c == "G":
			output += "C"
		elif c == "C":
			output += "G"
		else:
			output = "Error RNA nucleobases found!"
			break
	print(output)
