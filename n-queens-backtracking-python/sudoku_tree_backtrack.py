import copy

num_set = {1:{1,2,3,4,5,6,7,8,9},
		   2:{1,2,3}}

sudoku_sets = {1:[[5,3,0, 0,7,0, 0,0,0],
				 [6,0,0, 1,9,5, 0,0,0],
				 [0,9,8, 0,0,0, 0,6,0],
				 [8,0,0, 0,6,0, 0,0,3],
				 [4,0,0, 8,0,3, 0,0,1],
				 [7,0,0, 0,2,0, 0,0,6],
				 [0,6,0, 0,0,0, 2,8,0],
				 [0,0,0, 4,1,9, 0,0,5],
				 [0,0,0, 0,8,0, 0,7,9]],
			2: [[1,0,0],
				 [2,0,0],
				 [3,1,2]],
		    3: [[3,0,0],
				 [0,0,0],
				 [0,0,0]],
			4: [[2,0,3],
				 [1,0,0],
				 [0,0,1]]}

sudoku = sudoku_sets[2]
set_all = num_set[1]


def give_rows(sudoku):
	# print("Row Values")
	res = []
	for row in sudoku:
		res.append(row)
	return res

def give_cols(sudoku):
	# print("Column Values")
	res = []
	for i in range(len(sudoku)):
		col = [row[i] for row in sudoku]
		res.append(col)
	return res

def give_grids(sudoku):
	# print("Grid Values")
	res = []
	grid_h = int(len(sudoku)/3)
	for i in range(grid_h):
		for j in range(grid_h):
			i_fr, i_to = i*grid_h, (i+1)*grid_h
			j_fr, j_to = j*grid_h, (j+1)*grid_h

			grid = []
			for row in sudoku[i_fr:i_to]:
				# print(row[j_fr:j_to])
				grid = grid+row[j_fr:j_to]
			res.append(grid)			
	return res

def check_row(array):
	array = [i for i in array if i != 0]
	set_array = set(array)
	if not (len(set_array)==len(array)):
		return False
	return True

def check_sudoku(sudoku, show=False):
	rows_f=True
	cols_f=True	
	grids_f=True

	for i,array in enumerate(give_rows(sudoku)):
		if check_row(array) is False:
			rows_f=False
			print(f"Error at {i} Row")
			break
	else:
		if show: print("Row Correct")

	for i,array in enumerate(give_cols(sudoku)):
		if check_row(array) is False:
			cols_f=False	
			print(f"Error at {i} Col")
			break
	else:
		if show: print("Col Correct")
	
	for i,array in enumerate(give_grids(sudoku)):
		if check_row(array) is False:
			grids_f=False
			print(f"Error at {i} Grid")
			break
	else:
		if show: print("Grid Correct")

	print()
	print(f"[Row:{rows_f} and Col:{cols_f} and Grid:{grids_f}]")

	if rows_f and cols_f and grids_f:
		print("**Sudoku is Correct Till Now**")
		return True

	print("**Incorrect Sudoku Till Now**")
	return False

def fill_blanks(array, show=False):
	num_blank=0
	k=0
	error = False
	num_arr = len(array)

	arg_sudoku = copy.deepcopy(sudoku)

	for i in range(len(arg_sudoku)):
		for j in range(len(arg_sudoku)):
			if arg_sudoku[i][j]==0:
				# print(f"(R{i}, C{j})",end='--')
				num_blank+=1
				try:
					arg_sudoku[i][j]=array[k]
					k+=1
					if show:
						print(arg_sudoku[i][j],end=' ')
				except:
					error = True
					if show:
						print('x',end=' ')
					pass
			else:
				if show:
					print(arg_sudoku[i][j],end=' ')
				# print('-',end=' ')
	
	if error:
		print(f"You passed {num_arr}/{num_blank} values, {num_blank-num_arr} more needed")
	
	left_blanks = num_blank-num_arr

	return left_blanks, arg_sudoku

def is_valid(res):
	inp_set = set(res)
	print('\n\n')
	print("#"*50)
	print(res)

	blanks, arg_sudoku = fill_blanks(res)
	correct_flag 	   = check_sudoku(arg_sudoku)

	print("#"*50)

	# All values found, and is correct
	if blanks == 0 and correct_flag:
		return 2

	# Not all found but going correct
	if blanks>0 and correct_flag:
		return 1
	
	return 0

def gen_result(res=[]):

	# 	exit()
	flag = is_valid(res)

	if flag==2:
		print("Solution Found")
		exit()
		return

	if flag==0:
		print("Dead End Found")
		# Input given is not correct
		# No need to go further
		return

	if flag==1:
		# Generate more values
		# add more values in output
		for val in set_all:
			# 3 way tree
			gen_result(res+[val])

	print()
	return


print(gen_result([]))
# res == [1,3,2,3,2]:

check_sudoku(sudoku, show=True)
# fill_blanks([1,3,2,3,2])
# check_sudoku(sudoku)

