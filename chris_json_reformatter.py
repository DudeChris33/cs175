if __name__ == "__main__":
	squiggleNeeded = True
	with open("testing copy.jsonl", "r") as readFile:
		with open("testing.json", "w") as writeFile:
			writeFile.write("[\n")
			for readLine in readFile:
				if not readLine or readLine.strip() == '':
					writeFile.write("\n")
					continue
				
				if squiggleNeeded:
					writeFile.write("\t{\n")
					squiggleNeeded = False
				
				readLine = readLine.strip("[]'").strip()
				if readLine.startswith(r'//'):
					# writeFile.write('\t\t' + readLine + '\n')
					continue
				
				readLine = readLine.strip().strip(r"{},").strip()
				readLineList = readLine.split('"')
				
				# print(readLineList)
				writeFile.write('\t\t"move": "' + readLineList[-4].strip() + '",\n')
				writeFile.write('\t\t"desc": "' + readLineList[-6].strip() + '",\n')
				writeFile.write('\t\t"fen": "' + readLineList[-2].strip() + '",\n')
				writeFile.write('\t\t"prev": ')
				
				writeFile.write('"[')
				newMove = readLineList[0].split("[")[-1].strip()
				newMove = newMove.replace('"', '')#.replace("'", "")
				newMove = newMove.replace('[', '').replace(']', '')
				newMove = newMove[::-1].replace(',', '', 1)[::-1]
				writeFile.write(newMove)
				writeFile.write(']"\n')
				
				writeFile.write("\t},\n")
				squiggleNeeded = True
			writeFile.write("]")
			# MANUALLY DELETE LAST COMMA
					