

def somaCruzada(A,B):
	return[a+b for a in A for b in B]
# units, peers, and squares 

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = somaCruzada(rows, cols)

setRows = [somaCruzada(rows,c) for c in cols]
setColumns = [somaCruzada(c,cols) for c in rows]
#setVoisins = [somaCruzada(rs,cs) for c in rows]


print("Set of rows: ")
print (setRows)

print("Set of Columns: ")
print (setColumns)

