from z3 import Solver, Int, Or, Distinct, sat
import time

def convertInput(inputGrid):
	normalized = ""
	matrix = [[0]*9 for i in range(9)]
	for element in inputGrid:	
		matrix[element[0]-1][element[1]-1] = element[2]
	for i in range(0,9):
		for j in range(0,9):
			current = matrix[i][j]
			if current == 0:				
				normalized = normalized +'.'
			else:
				normalized = normalized + str(current)
	assert len(normalized) == 81
	return normalized

#Examples of inputs
format1_1 = [(1,1,2), (1,2,9), (1,4,3), (1,6,8), (2,3,6), (2,4,4), (2,8,5), (3,4,7), (3,8,9), (4,3,1), (4,9,8), (5,1,7),(5,5,9) ,(5,7,3), (6,1,3), (6,9,5), (7,6,2), (7,9,6), (8,2,8), (8,5,1), (8,7,5) ,(9,1,5), (9,2,2), (9,5,8)]
format1_2 = [(1,4,2), (1,5,6), (1,7,7), (1,9,1), (2,1,6),(2,2,8),(2,5,7),(1,8,9) ]
format1_3 = [(1,4,2), (1,5,6), (1,7,7), (1,9,1), (2,1,6),(2,2,8),(2,5,7),(2,8,9), (3,1,1), (3,2,9),(3,6,4),(3,7,5)]

format2_1  = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
format2_2  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
format2_3  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'


grid = convertInput(format1_1)

print('Input provided: ')
print(grid)


#Construction of Sudoku structure
def crossedProduct(A,B):
	return[a+b for a in A for b in B]


digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = crossedProduct(rows, cols)

setRows = [crossedProduct(rows,c) for c in cols]
setColumns = [crossedProduct(c,cols) for c in rows]
setVoisins = [crossedProduct(rows,cols) for rows in ('ABC','DEF','GHI') for cols in ('123', '456', '789')]

allUnits = setRows + setColumns + setVoisins

# A collection of nine squares (column, row, or box) a unit and the squares that share a unit the voisins.

#print("Set of rows: ")
#print (setRows)

#print("Set of Columns: ")
#print (setColumns)

#print("Set of voisins: ")
#print (setVoisins)

#print("All units list: ")
#print (allUnits)

units = dict((s, [u for u in allUnits if s in u]) for s in squares)
voisins = dict((s, set(sum(units[s],[]))-set([s]))  for s in squares)

#print("\n\nUnits list: ")
#print (units['A1'])

#print("voisins list: ")
#print (voisins['A1'])


#Unit tests
def tests():    
    assert (len(squares) == 81)
    assert len(allUnits) == 27
    assert all(len(units[s]) == 3 for s in squares) #We have lines, rows and neighborhood
    assert all(len(voisins[s]) == 20 for s in squares) # We have 8 + 8 + 4
    assert units['A1'] == [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'],
                           ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    print('All tests passed!')                           

tests()


# Functionality
def parseGrid(grid):
	if any(element not in "123456789." for element in grid):
		raise Exception("input not valid")
	elements = crossedProduct("ABCDEFGHI", "123456789")
	values = {e: v for e,v in zip(elements, grid)}
	return values #We return the dictionary of values


def solve(grid):

	values = parseGrid(grid)
	elements = squares 
	symbols = {e: Int(e) for e in elements}

	s = Solver()

	#Each square should have a value in the interval [1,9]
	for element in symbols.values():
		s.add(Or([element == i for i in range(1, 10)]))


	#Then every row should cover every value
	for row in "ABCDEFGHI":
		s.add(Distinct([symbols[row + col] for col in "123456789"]))

	#Then every column should cover every value
	for column in "123456789":
		s.add(Distinct([symbols[row + column] for row in "ABCDEFGHI"]))

	#  Finally every block neighborhood should cover every value
	for i in range(3):
		for j in range(3):
			s.add(Distinct([symbols["ABCDEFGHI"[m + i * 3] + "123456789"[n + j * 3]] for m in range(3) for n in range(3)]))

	#Now we fill in the given intial puzzle
	for element, value in values.items():
		if value in "123456789":
			s.add(symbols[element] == value)

	if not s.check() == sat:
		raise Exception("unsolvable")

	model = s.model()
	values = {e: model.evaluate(s).as_string() for e,s in symbols.items()}
	#for key in values:
	#	print(key,'--->', values[key])
	return values


#This function will take a sudoku puzzle in dictionary format and convert it back to Matrix 9x9 structure
def constructMatrix(entry):
	matrix = [[0]*9 for i in range(9)]
	str = ''
	for key in entry:
		if entry[key] == '.':
			entry[key] = '0'
		next = entry[key]		
		str = str + next	
	for i in range(0,9):
		for j in range(0,9):
			matrix[i][j] = str[0] 
			str = str [1:]
	return matrix

def printResult(values):
	matrix = constructMatrix(values)
	for i in range(0,9):
		print(matrix[i])


#values = parseGrid(grid)
#printResult(values)

#Finally solving the puzzle
start = time.time()
res = solve(grid)
end = time.time()-start

printResult(res)
print('Puzzle solved in: ', end, ' s?' )
