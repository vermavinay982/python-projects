from pprint import pprint
import copy
"""
[x] create system to check 
[x] generate matrix
[x] column based approach
[x] make it work for 4x4 
[x] implement brute force with 4 loops
[x] implement brute force with 8 loops
[x] tree based 
[x] create a generator

print_mat - print individual one using location of 1
print_mat2 - print all ones using matrix
check row - if there are no conflicts in row
check col - no conlficts in col
check ldiag - from top left to bottom right - 00,11,22,33 = i-j same
check rdiag - from top right to bottom left - 03,12,21,30 = i+j same
check all - check all conditions for given 1 - True if perfect
check matrix - check for all ones - if any of is conflict, stop
gen matrix - input of column values, place 1 in matrix 
gen values - tree based back tracking

taking too much time for 8x8
"""


def print_mat(k,l,n):
	for i in range(n):
		for j in range(n):
			if (k,l)==(i,j):
				print('X',end=' ')
			else:
				print('-',end=' ')
		print()
	print()

def print_mat2(mat):
	n = len(mat)
	for i in range(n):
		for j in range(n):
			if mat[i][j]:
				print('X',end=' ')
			else:
				print('-',end=' ')
		print()
	print()

def check_row(i,j,matrix,show=False):
	# move left to right
	for x in range(n):
		if matrix[i][x]==1 and (not (i,x) == (i,j)):
			if show: print("Row",i,x)
			return False
	return True

def check_col(i,j,matrix,show=False):
	# print(matrix)
	# move top to bottom
	for x in range(n):
		if matrix[x][j]==1 and (not (x,j) == (i,j)):
			if show: print("Col",x,j)
			return False
	return True

def check_ldiag(i,j,matrix,show=False):
	# X - - - 
	# - X - - 
	# - - X - 
	# - - - X 
	# 03 = diff -1
	# 02,13 = diff -2
	# 01,12,23 = diff -1
	# 00,11,22,33 = diff 0
	# 10,21,32 = diff 1
	# 20,31 = diff 2
	# 30 = diff 3
	diag_sub = i-j
	if show:
		print(f"Diag Sum Left: {diag_sub}")
	for k in range(n):
		for l in range(n):
			if (k,l) == (i,j): continue
			if matrix[k][l]==1:
				if (k-l)==diag_sub:
					return False
	return True

def check_rdiag(i,j,matrix,show=False):
	# - - - X 
	# - - X - 
	# - X - - 
	# X - - - 
	# 00 = sum 0
	# 01,10 = sum 1
	# 02,11,20 = sum 2
	# 03,12,21,30 = sum 3
	# 13,22,31 = sum 4
	# 23,32 = sum 5
	# 33 = sum 6
	diag_sum = i+j
	if show: print(f"Diag Sum Right: {diag_sum}")
	for k in range(n):
		for l in range(n):
			if (k,l) == (i,j): continue
			if matrix[k][l]==1:
				if (k+l)==diag_sum:
					return False
	return True

def check_all(i,j,matrix,show=False):
	"""
	check with respect to all other ones present
	# if clear, return True
	# if blocked, return False
	"""
	# rf = check_row(i,j,matrix)
	# cf = check_col(i,j,matrix)
	# rdf = check_rdiag(i,j,matrix)
	# ldf = check_ldiag(i,j,matrix)
	# # print(f"row:{rf} and col:{cf} and rd:{rdf} and ld:{ldf}")
	# if rf and cf and rdf and ldf:
	# 	if show: print("All Clear")
	# 	return True
	# if show:
	# 	print("Not Clear")

	"""
	faster way, avoid checking if failed at first
	worst case - checking till last condition
	best case - failed at first only
	"""
	if check_row(i,j,matrix):
		if check_col(i,j,matrix):
			if check_rdiag(i,j,matrix):
				if check_ldiag(i,j,matrix):
					return True
	return False

def check_matrix(matrix,show=False):
	"""
	to check all the ones
	"""
	result = False
	for j in range(n):
		for i in range(n):
			if matrix[i][j]==1:
				result = check_all(i,j,matrix)
				if show: 
					print(f"Checking ({i},{j})")
					print_mat(i,j,n)
					print(result)
					print()
				# for the last 1, if it gets true, it returns true
				# but in reality if any one condition for that 1 is False,
				# return False
				if result is False:
					return False

	return result

def gen_matrix(matrix, col_val):
	"""
	1,1,1,1 means every column first element is 1
	whole first row is 1

	0,0,0,0 - first row all are ones
	"""
	n = len(matrix)
	for r in range(n):
		# for Column, change i 
		for c in range(n):
			# if row matches, put a 1
			try:
				if r == col_val[c]:
					# move to next value
					matrix[r][c]=1
			except:
				# if less values there, fine skip it
				pass
	# print(matrix)
	return matrix

# matrix   = [[0,1,0,0],
#     		[0,0,0,1],
#     		[1,0,0,0],
#     		[0,0,1,0]]

# matrix   = [[1,0,0,0],
#     		[0,0,0,0],
#     		[0,0,0,0],
#     		[0,0,0,0]]

# matrix   = [[0,0,1,0],
#     		[1,0,0,0],
#     		[0,0,0,1],
#     		[0,1,0,0]]

# matrix   = [[1,0,0,0],
#     		[1,0,1,0],
#     		[0,0,0,0],
#     		[0,0,0,0]]

matrixq   = [[0,0,0,0],
    		 [0,0,0,0],
    		 [0,0,0,0],
    		 [0,0,0,0]]

matrixq   = [[0,0,0,0,0,0,0,0],
    		 [0,0,0,0,0,0,0,0],
    		 [0,0,0,0,0,0,0,0],
    		 [0,0,0,0,0,0,0,0],

    		 [0,0,0,0,0,0,0,0],
    		 [0,0,0,0,0,0,0,0],
    		 [0,0,0,0,0,0,0,0],
    		 [0,0,0,0,0,0,0,0]]


n = len(matrixq)

########################## checking generate matrix
# col_val = [0,0,0,0]
# col_val = [1,1,1,1]
# col_val = [0,1,2,3]
# col_val = [3,2,1,0]

# gen_mt = copy.deepcopy(matrixq)
# gen_mt = gen_matrix(gen_mt, col_val)
# print_mat2(gen_mt)

###################################################
######################### checking matrix
# col_val = [1,3,0,2]
# matrix = gen_matrix(matrix, col_val)
# pprint(matrix)
# matrix = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
# matrix = [[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
# matrix = [[0, 1, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 0, 1]]
# matrix = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
# # pprint(matrix)

# res = check_matrix([[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0]],True)
# print(res)
# exit()

########################################## BRUTE FORCE ############
############## 4x4 matrix
# for i in range(n):
# 	for j in range(n):
# 		for k in range(n):
# 			for l in range(n):
# 				col_val = [i,j,k,l]
# 				gen_mt = copy.deepcopy(matrixq)
# 				gen_mt = gen_matrix(gen_mt, col_val)
# 				# print(gen_mt)
# 				res = check_matrix(gen_mt)
# 				if res:
# 					print("Found",res,col_val)
# 					print_mat2(gen_mt)
############## 8x8 matrix
# for a in range(n):
# 	for b in range(n):
# 		for c in range(n):
# 			for d in range(n):
# 				for e in range(n):
# 					for f in range(n):
# 						for g in range(n):
# 							for h in range(n):
# 								col_val = [a,b,c,d,e,f,g,h]
# 								gen_mt = copy.deepcopy(matrixq)
# 								gen_mt = gen_matrix(gen_mt, col_val)
# 								# print(gen_mt)
# 								res = check_matrix(gen_mt)
# 								if res:
# 									print("Found",res,col_val)
# 									print_mat2(gen_mt)
# 					print("Here")			
########################################## BRUTE FORCE ############

vals = [i for i in range(n)]

def gen_values(val=[]):
	"""
	move to more values to find answer
	stop if
		generated more than required, only n can be answer, else waste
		duplicate numbers are found - it will be on same row, avoid
		getting blocked, for sure add anything it will stay blocked


	return means
		dont add further to this string, result
	not return means
		we are at right track, keep adding more to reach goal of 4 words

	"""
	if len(val)>n or len(val)>len(set(val)):

		# limit is 4 of generating list of column
		# repeating element found, removed by set
		# print("Due to this",len(set(val)),len(val))
		return


	col_val = val
	gen_mt = copy.deepcopy(matrixq)
	gen_mt = gen_matrix(gen_mt, col_val)
	res = check_matrix(gen_mt)
  
	# print(gen_mt)
	# print(val,res)

	if not res and len(val):
		print(f"Due to Wrong End, Stopped {val}")
		return


	if res and len(val)==n:
		print("####################### Found",res,col_val)
		print_mat2(gen_mt)
		print("###########")


	for v in vals:
		gen_values(val+[v])

gen_values()