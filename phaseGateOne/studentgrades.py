def get_student_Scores():
	number_of_students = int(input("How many students do you have?\n"))	

	numberOfSubjects = int(input("How many subjects do they offer?\n"))

	studentsArray = []
	scoresArray = [][]
		
	total = 0
	sum_of_all_scores = []
		for index in range(0, len(studentsArray)):
			for secondIndex in range(0, numberOfSubjects)):
				
				student_number = int(input("Entering scores for student ", index))
				
				
				studentScore = int(input("Enter score for subject ", secondIndex)

				int  = input.nextInt()
			
				scoresArray[index-1][secondIndex-1] = studentScore

				print("Saving >>>>>>>>>>>>>>>>>>>>>>>\n")
				print("Saved successfully")

				total += scoresArray[index-1][secondIndex-1]
				average[index-1] = total[index-1]/numberOfSubjects

			highest = average[index-1]
			if average[index-1] > highest:
				highest = average[index-1]
			print("Highest average is: ", highest, "\nStudent with the first position is student ", index)
		
				

			print("Average is: ", average[index-1])

			print("Total for student", index, " is: ", total[index-1])

			print(scoresArray)

			print(total)

			print(average)



		
			sum_of_all_scores[index-1] = total
			sum_of_all_scores[index] = 0
			print(scoresArray)
			print(sum_of_all_scores)