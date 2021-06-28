def get_numeric(hour):
    s_idx = hour.find(":")
    my_hour = int(hour[:s_idx] + hour[s_idx+1:])
    return my_hour

def get_freetime(calendar, bound):
	my_freetime = []

	if get_numeric(bound[0]) < get_numeric(calendar[0][0]):
		my_freetime.append([bound[0], calendar[0][0]])

	for i in range(len(calendar)-2):
		my_freetime.append([calendar[i][1], calendar[i+1][0]])

	if get_numeric(bound[1]) > get_numeric(calendar[-1][1]):
		my_freetime.append([bound[1], calendar[-1][1]])

	return my_freetime
	

def compare_freetime(your_freetime, my_freetime):
	free = []
	for yh in your_freetime:
		for mh in my_freetime:
			if get_numeric(yh[0]) <= get_numeric(mh[0]):
				start = yh[0]
			else:
				start = mh[0]
			
			if get_numeric(yh[1]) <= get_numeric(mh[1]):
				end = yh[1]
			else:
				end = mh[1]
			free.append([start, end])
	return free

# Main code

your_calendar = [["10:00", "12:30"], ["14:00","16:00"]]
my_calendar = [["9:00", "12:00"], ["15:00", "16:30"]]

your_dailybound = ["10:00", "18:00"]
my_dailybound = ["9:00", "18:00"]

your_freetime = get_freetime(your_calendar, your_dailybound)
my_freetime = get_freetime(my_calendar, my_dailybound)

total_freetime = compare_freetime(your_freetime, my_freetime)

print(total_freetime)
