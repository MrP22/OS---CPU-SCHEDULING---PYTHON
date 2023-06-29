import os

def main():
	print("CPU SCHEDULING")
	print("1 - SHORTEST JOB FIRST")
	print("2 - PRE-EMPTIVE PRIORITY")
	print("3 - ROUND ROBIN")
	res = int(input("Choose CPU you want to try: ")) #Choose of what CPU will be select
	if res == 1:
		os.system("cls") #Clear the Screen
		CPU_SJF()
	elif res == 2:
		os.system("cls")
		CPU_PP()
	elif res == 3:
		os.system("cls")
		CPU_RR()
	else:
		print("Wrong Input")

def CPU_SJF():
	# Taking the number of processes
	n = int(input("Enter number of process: "))
	# Matrix for storing Process Id, Burst Time, Average Waiting Time & Average Turn Around Time.
	A = [[0 for j in range(4)] for i in range(100)]
	total, avg_wt, avg_tat = 0, 0, 0
	print("Enter Burst Time:")
	for i in range(n): # User Input Burst Time and alloting Process Id.
		A[i][1] = int(input(f"P{i+1}: "))
		A[i][0] = i + 1
	for i in range(n): # Sorting process according to their Burst Time.
		index = i
		for j in range(i + 1, n):
			if A[j][1] < A[index][1]:
				index = j
		temp = A[i][1]
		A[i][1] = A[index][1]
		A[index][1] = temp
		temp = A[i][0]
		A[i][0] = A[index][0]
		A[index][0] = temp
	A[0][2] = 0 # Calculation of Waiting Times
	for i in range(1, n):
		A[i][2] = 0
		for j in range(i):
			A[i][2] += A[j][1]
		total += A[i][2]
	avg_wt = total / n
	total = 0
	# Calculation of Turn Around Time and printing the data.
	print("P	 BT	 WT	 TAT")
	for i in range(n):
		A[i][3] = A[i][1] + A[i][2]
		total += A[i][3]
		print(f"P{A[i][0]}	 {A[i][1]}	 {A[i][2]}	 {A[i][3]}")
	avg_tat = total / n
	print(f"Average Waiting Time= {avg_wt}")
	print(f"Average Turnaround Time= {avg_tat}")

def CPU_RR():
	# Taking the number of processes
	n = int(input("RR Enter number of process: "))

	# Matrix for storing Process Id, Burst Time, Waiting Time & Turnaround Time.
	A = [[0 for j in range(4)] for i in range(n)]

	quantum_time = int(input("Enter quantum time: "))  # User input for time quantum

	print("Enter Burst Time:")
	for i in range(n):  # User Input Burst Time and alloting Process Id.
		A[i][1] = int(input(f"P{i+1}: "))
		A[i][0] = i + 1

	# Calculation of Waiting Times and remaining burst time
	remaining_burst_time = [A[i][1] for i in range(n)]
	current_time = 0

	while True:
		all_finished = True  # Flag to check if all processes are finished
		
		for i in range(n):
			if remaining_burst_time[i] > 0:
				all_finished = False

				if remaining_burst_time[i] <= quantum_time:
					A[i][2] += current_time
					current_time += remaining_burst_time[i]
					A[i][3] = current_time
					remaining_burst_time[i] = 0
				else:
					A[i][2] += current_time
					current_time += quantum_time
					remaining_burst_time[i] -= quantum_time

		if all_finished:
			break

	# Calculation of Average Waiting Time and Average Turnaround Time
	total_wt, total_tat = 0, 0

	print("P   BT   WT   TAT")
	for i in range(n):
		A[i][2] -= sum(A[i][2:]) // n  # Adjusting waiting time
		A[i][3] = A[i][1] + A[i][2]
		total_wt += A[i][2]
		total_tat += A[i][3]
		print(f"P{A[i][0]}  {A[i][1]}  {A[i][2]}  {A[i][3]}")

	avg_wt = total_wt / n
	avg_tat = total_tat / n

	print(f"Average Waiting Time: {avg_wt}")
	print(f"Average Turnaround Time: {avg_tat}")

def CPU_PP():
	# Taking the number of processes
	n = int(input("Enter number of processes: "))

	# Matrix for storing Process Id, Burst Time, Priority, Arrival Time, Waiting Time, Turnaround Time.
	A = [[0 for j in range(6)] for i in range(n)]
	total_wt, total_tat = 0, 0

	print("Enter Burst Time, Priority, and Arrival Time:")
	for i in range(n):
		A[i][1], A[i][2], A[i][3] = map(int, input(f"P{i+1}:\t").split())
		A[i][0] = i + 1

	time = 0
	completed = 0
	ready_queue = []

	while completed != n:
		for i in range(n):
			if A[i][1] > 0 and A[i][3] <= time and i not in ready_queue:
				ready_queue.append(i)

		if len(ready_queue) == 0:
			time += 1
			continue

		highest_priority = ready_queue[0]
		for i in ready_queue:
			if A[i][2] < A[highest_priority][2]:
				highest_priority = i

		current_process = highest_priority
		A[current_process][1] -= 1
		time += 1

		if A[current_process][1] == 0:
			completed += 1
			A[current_process][5] = time - A[current_process][3]  # Turnaround Time
			A[current_process][4] = A[current_process][5] - A[current_process][1] + A[current_process][3]  # Waiting Time

		ready_queue.remove(current_process)

	# Calculation of average waiting time and average turnaround time
	for i in range(n):
		total_wt += A[i][4]
		total_tat += A[i][5]

	avg_wt = total_wt / n
	avg_tat = total_tat / n

	# Printing the data
	print("P\tBT\tPriority\tAT\tWT\tTAT")
	for i in range(n):
		print(f"P{A[i][0]}\t{A[i][1]}\t{A[i][2]}\t\t{A[i][3]}\t{A[i][4]}\t{A[i][5]}")

	print(f"Average Waiting Time = {avg_wt}")
	print(f"Average Turnaround Time = {avg_tat}")



if __name__ == "__main__":
	main()
