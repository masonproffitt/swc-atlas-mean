def mean(num_list):
	try:
		return sum(num_list) / len(num_list)
	except ZeroDivisionError as detail:
		return float("nan")
