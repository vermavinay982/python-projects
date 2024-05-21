matrix   = [[0,0,1,0],
    		[1,0,0,0],
    		[0,0,0,1],
    		[0,1,0,0]]

# matrix   = [[1,0,0,0],
#     		[1,0,1,0],
#     		[0,0,0,0],
#     		[0,0,0,0]]

n = len(matrix)

for i in range(n):
	for j in range(n):
		# val = matrix[i][j]
		val = (i,j)
		print(val,end=' ')
	print()

print('\n'*1)

def print_mat(func):
	for i in range(n):
		for j in range(n):
			# val = matrix[i][j]
			if func(i,j):
				val = 'X'
			else:
				val = '-'
			print(val,end=' ')
		print()
	print('\n'*1)

def c1(i,j):
	if i==j:return True
	return False

def c2(i,j,val=0):
	if (i-j)==val:return True
	return False

def c3(i,j,val=1):
	if (i-j)==val:return True
	return False

def c7(i,j,val=4):
	if (i+j)==val:return True
	return False

def c4(i,j,val=3):
	if (i+j)==val:return True
	return False

def c5(i,j,val=2):
	if (i+j)==val:return True
	return False

def c6(i,j,val=1):
	if (i+j)==val:return True
	return False

print_mat(c1)
print_mat(c2)
print_mat(c3)
print_mat(c4)
print_mat(c5)
print_mat(c6)
print_mat(c7)

"""
(0, 0) (0, 1) (0, 2) (0, 3) 
(1, 0) (1, 1) (1, 2) (1, 3) 
(2, 0) (2, 1) (2, 2) (2, 3) 
(3, 0) (3, 1) (3, 2) (3, 3) 


X - - - 
- X - - 
- - X - 
- - - X 


X - - - 
- X - - 
- - X - 
- - - X 


- - - - 
X - - - 
- X - - 
- - X - 


- - - X 
- - X - 
- X - - 
X - - - 


- - X - 
- X - - 
X - - - 
- - - - 


- X - - 
X - - - 
- - - - 
- - - - 


- - - - 
- - - X 
- - X - 
- X - - 

"""

