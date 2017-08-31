import requests
import json
import csv


def read_exam(url="exam.csv"):
    url = url
    QUESTIONS = []
    QUESTION_TEXTS = []
    ANSWERS = ["B", "D", "B","ACF", "AF", "AGE", "ABCDEF", "B", "CD", "B", "ABCDEFG"]
    WRONG = ["ACDEFG", "ABCEFG", "ACDEFG", "BDEG", "BCDEG", "BCDFG", "G", "ACDEFG", "ABEFG", "ACDEFG", ""]
    trial = []
    
    with open(url) as link:
        link_reader = csv.reader(link)

        header_row = next(link_reader)
        
        for row in link_reader:
            try:
                QUESTIONS.append(row[0])
                QUESTION_TEXTS.append(row[1])
                
                
            except IndexError:
                pass
        #print(QUESTIONS)
        run = list(zip(("".join((QUESTIONS))), ANSWERS))
        #print(run)
        running = list(zip(QUESTIONS, QUESTION_TEXTS, ANSWERS, WRONG))
        #print(running)
        


        helping = dict(id=0,my_answer = "b")
        #print(type(run))
        for k,v in run:
            trial.append({"id": int(k),"my_answer": v})
        #print(trial)
        
        MY_ANSWERS_JS = json.dumps(trial, indent=4, sort_keys=True)
        print(MY_ANSWERS_JS)
        #print(json.loads(MY_ANSWERS_JS))
        return (QUESTIONS,QUESTION_TEXTS, WRONG)
read_exam()


