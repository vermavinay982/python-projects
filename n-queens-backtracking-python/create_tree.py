set_all = {1,2,3}

blanks = 5 

def is_valid(res):
	inp_set = set(res)
	if len(res)==len(inp_set):
		return True
	else:
		return False

def gen_result(res=[], blanks=3):
	print(res)
	if not is_valid(res):
		return res

	if len(res)==blanks:
		return res

	for val in set_all:
		gen_result(res+[val],blanks)
	return res


print()
print(gen_result([],blanks))