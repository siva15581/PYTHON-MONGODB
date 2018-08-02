from pymongo import MongoClient
db = MongoClient('localhost:27017').Students

Option = input('Select option to proceed (1--Insert, 2--Update, 3--Delete , 4--Search, 5--Results) :: ')

################################  INSERT OPERATION ##################################
if Option == "":
		print ("\n\n****************  Please enter only values *******************")

elif int(Option) == 1:

	Name = input('Enter the name :: ')

	if Name.strip() != "" :

		S1 = input('Enter the Term-1 score :: ')
		S2 = input('Enter the Term-2 score :: ')
		S3 = input('Enter the Term-3 score :: ')

		if S1 == "":
			S1=0
		if S2 == ""	:
			S2=0
		if S3 == "":
			S3=0

		ID = db.Practice.count()
		db.Practice.insert({"_id": int(ID), "name": Name, "results":[{"evaluation":"term1","score":float(S1)},{"evaluation":"term2","score":float(S2)},{"evaluation":"term3","score":float(S3)}]})
		
		print("\n\n>>>>>> Last record inserted is given below:\n")
		for rec in db.Practice.find({"_id": int(ID)}):
			print (rec)

	else:
		
		print ("\n\n****************  Name should be entered *******************")


################################  UPDATE OPERATION ##################################
elif int(Option) == 2:	
	

	Option = input('(1---Update by ID, 2---Update by Name) :: ')

	if Option == "":
		print ("\n\n****************  Please enter only values *******************")

	elif int(Option) == 1:

		ID = input("Enter ID to Search :: ")
		if ID != "":		

			S1 = input('Enter the Term-1 score :: ')
			S2 = input('Enter the Term-2 score :: ')
			S3 = input('Enter the Term-3 score :: ')

			if S1 == "":
				S1=0
			if S2 == ""	:
				S2=0
			if S3 == "":
				S3=0

			db.Practice.update({"_id": int(ID)}, {"$set": {"results.0.score":float(S1),"results.1.score":float(S2),"results.2.score":float(S3)}})		
			print("\n\n>>>>>> Last record updated is given below:\n")
			for rec in db.Practice.find({"_id": int(ID)}):
				print (rec)
		else:
			print ("\n\n****************  ID should be entered *******************")			

	elif int(Option) == 2:		

		Name = input("Enter Name to Search :: ")
		
		if Name != "":

			S1 = input('Enter the Term-1 score :: ')
			S2 = input('Enter the Term-2 score :: ')
			S3 = input('Enter the Term-3 score :: ')

			if S1 == "":
				S1=0
			if S2 == ""	:
				S2=0
			if S3 == "":
				S3=0

			db.Practice.update({"name": Name}, {"$set": {"results.0.score":float(S1),"results.1.score":float(S2),"results.2.score":float(S3)}})		
			print("\n\n>>>>>> Last record updated is given below:\n")
			for rec in db.Practice.find({"name": Name}):
				print (rec)
		else:
			print ("\n\n****************  Name should be entered *******************")

	else:
		print("\n\n****************  Invalid Input *******************")	


################################  DELETE OPERATION ##################################
elif int(Option) == 3:	
	
	Option = input('(1---Delete by ID, 2---Delete by Name) :: ')

	if Option == "":
		print ("\n\n****************  Please enter only values *******************")

	elif int(Option) == 1:

		ID = input("Enter ID to Search :: ")
		if ID != "":		

			db.Practice.remove({"_id": int(ID)});
			print("\n\n>>>>>> Last record deleted is with ID:{}".format(ID))
			for rec in db.Practice.find({"_id": int(ID)}):
				print (rec)
			print("\n>>>>>> No record found with ID:{}".format(ID))
					
		else:
			print ("\n\n****************  ID should be entered *******************")			

	elif int(Option) == 2:		

		Name = input("Enter Name to Search :: ")
		
		if Name != "":

			db.Practice.remove({"name": Name});
			print("\n>>>>>> Last record deleted is with Name:{}".format(Name))
			for rec in db.Practice.find({"name": Name}):
				print (rec)
			print("\n\n>>>>>> No record found with Name:{}".format(Name))

		else:
			print ("\n\n****************  Name should be entered *******************")

	else:
		print("\n\n****************  Invalid Input *******************")


################################  SEARCH OPERATION ##################################
elif int(Option) == 4:
	
	Option = input('(1---Search by ID, 2---Search by Name) :: ')

	if Option == "":
		print ("\n\n****************  Please enter only values *******************")

	elif int(Option) == 1:
		ID = input("Enter ID to Search :: ")
		
		if ID != "":

			print("\n\n >>>>>>>>> Please find the below search:\n")			
			for rec in db.Practice.find({"_id": int(ID)}):
				print (rec)
		else:
			print ("\n\n****************  ID should be entered *******************")		

	elif int(Option) == 2:		

		Name = input("Enter Name to Search :: ")
		
		if Name != "":

			print("\n\n >>>>>>>>>>> Please find the below search:\n")
			for rec in db.Practice.find({"name": Name}):
				print (rec)

		else:
			
			print ("\n\n****************  Name should be entered *******************")					

	else:
		print("\n\n****************  Invalid Input *******************")

elif int(Option) == 5:
	
	print ("\n ****************************************** EMPLOYEE TRAINING SCORE ANALYSIS RESULTS **************************************")


	#************************************** QUESTION-1 *************************************
	print()
	print ("\n\n(1) FIND COUNT & PERCENTAGE OF EMPLOYEES WHO FAILED IN TERM-1, PASSING SCORE = 37 :: ")
	print("-------------------------------------------------------------------------------------\n")
	
	pipe = [{'$unwind': "$results"},
			{'$match': {"results.evaluation":"term1"}},
			{'$group': {
		   		"_id": "null",
		   		"TotalEMP": {'$sum': 1},
		   		"FailCount": {'$sum': {'$cond': [{ "$lt": ["$results.score", 37 ] },1 ,0]}}}},
			{'$project': {
	   			"_id": 0,
	   			"TotalEMP":1,
	   			"FailCount":1,	   
	   			"PercentFail": {'$concat': [{'$toString': {'$divide': [{'$trunc': {'$multiply': [{'$multiply': [{'$divide': 
	                		  ["$FailCount","$TotalEMP"]},100]},100]}},100]}},"","%"]}
	   		}}]

	Output = db.Practice.aggregate(pipeline = pipe)	
	print(list(Output))
	#************************************** QUESTION-1 *************************************


	#************************************** QUESTION-2 *************************************
	print("\n\n")
	print("(2) FIND EMPLOYEES WHO FAILED IN AGGREGATE (TERM-1 + TERM-2 + TERM-3) :: ")	
	print("--------------------------------------------------------------------------\n")

	pipe = [{'$unwind': "$results"},
	{'$group': {
		   "_id": "$name",		   
		   "TotalScore": {'$sum': "$results.score"}
		 }
	},
	{'$match': {"TotalScore": { "$lt": 37*3 } } },
	{'$project': {
	   "_id":1,
	   "TotalScore":1
	   }
	}]

	Output = db.Practice.aggregate(pipeline = pipe)	
	print(list(Output))
	#************************************** QUESTION-2 *************************************


	#************************************** QUESTION-3 *************************************
	print("\n\n")
	print ("(3) FIND THE AVERAGE SCORE OF TRAINEES FOR TERM-1 :: ")
	print("-----------------------------------------------------\n")
	
	pipe = [{'$unwind': "$results"},
			{'$match': {"results.evaluation": "term1"}},
			{'$group': {
		   		"_id": "null",
		   		"TotalCount": {'$sum': 1},
		   		"ScoreSumForTerm1": {'$sum': "$results.score"}
		 		}
			},
			{'$project': {
	   			"_id":0,
	   			"TotalCount": 1,	   
	   			"ScoreSumForTerm1": {'$divide': [{'$trunc': {'$multiply': ["$ScoreSumForTerm1",100]}},100]},
	   			"AverageScoreForTerm1": {'$divide': [{'$trunc': {'$multiply': [{'$divide': ["$ScoreSumForTerm1", "$TotalCount"]},100]}},100]}
	   			}
			}]

	Output = db.Practice.aggregate(pipeline = pipe)	
	print(list(Output))
	#************************************** QUESTION-3 *************************************	


	#************************************** QUESTION-4 *************************************
	print("\n\n")
	print ("(4) FIND THE AVERAGE SCORE OF TRAINEES FOR AGGREGATE (TERM-1 + TERM-2 + TERM-3)   :: ")
	print("-------------------------------------------------------------------------------------\n")
	
	pipe = [
			{'$unwind': "$results"},
			{'$group': {
		   		"_id": "null",
		   		"AverageOfAggregateScores": {'$avg': "$results.score"}
		 		}
			},
			{'$project': {
	   			'_id':0,
	   			"AverageOfAggregateScores": {'$divide': [{'$trunc': {'$multiply': ["$AverageOfAggregateScores",100]}},100]}
	   			}
			}]

	Output = db.Practice.aggregate(pipeline = pipe)	
	print(list(Output))
	#************************************** QUESTION-4 *************************************	


	#************************************** QUESTION-5 *************************************
	print("\n\n")
	print ("(5) FIND THE NUMBER OF EMPLOYEES WHO FAILED IN ALL THE TERMS (TERM-1 + TERM-2 + TERM-3)   :: ")
	print("---------------------------------------------------------------------------------------------\n")	

	Output = int(db.Practice.find({"results.0.score" : {"$lt":37},"results.1.score" : {"$lt":37},"results.2.score" : {"$lt":37}}).count());	
	print("\n\n >>>>>>>>>>>>>>>>> TOTAL COUNT :: ", Output)
	#************************************** QUESTION-5 *************************************	


	#************************************** QUESTION-6 *************************************
	print("\n\n")
	print ("(6) FIND THE NUMBER OF EMPLOYEES WHO FAILED IN ANY OF THE 3 TERMS(TERM-1 + TERM-2 + TERM-3)   :: ")
	print("-------------------------------------------------------------------------------------------------\n")	

	Output = int(db.Practice.find({"$or": [{"results.0.score" : {"$lt":37}},{"results.1.score" : {"$lt":37}},{"results.2.score" : {"$lt":37}}]}).count());
	print("\n\n >>>>>>>>>>>>>>>>> TOTAL COUNT :: ", Output)
	#************************************** QUESTION-6 *************************************	

else:
	print ("\n\n****************  Invalid Input *******************")