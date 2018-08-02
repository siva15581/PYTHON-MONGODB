from bottle import run, route, template
from pymongo import MongoClient
db = MongoClient('localhost:27017').Students


#************************************** QUESTION-1 *************************************
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

Output1 = db.Practice.aggregate(pipeline = pipe)



#************************************** QUESTION-2 *************************************
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

Output2 = db.Practice.aggregate(pipeline = pipe)



#************************************** QUESTION-3 *************************************
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

Output3 = db.Practice.aggregate(pipeline = pipe)



#************************************** QUESTION-4 *************************************
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

Output4 = db.Practice.aggregate(pipeline = pipe)



#************************************** QUESTION-5 *************************************
Output5 = int(db.Practice.find({"results.0.score" : {"$lt":37},"results.1.score" : {"$lt":37},"results.2.score" : {"$lt":37}}).count());	



#************************************** QUESTION-6 *************************************
Output6 = int(db.Practice.find({"$or": [{"results.0.score" : {"$lt":37}},{"results.1.score" : {"$lt":37}},{"results.2.score" : {"$lt":37}}]}).count());


@route('/')
def index():
	return template('Results.tpl', Output1=list(Output1), Output2=list(Output2), Output3=list(Output3), Output4=list(Output4), Output5=Output5, Output6=Output6)

run(debug=True, reloader = True)