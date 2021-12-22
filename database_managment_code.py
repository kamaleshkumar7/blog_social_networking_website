# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:00:42 2020

@author: skaus
"""
import sqlite3
def test(file):
    for x in file:
        print('question_id : ',x['question_id'])
        print('question postedby : ',x['question postedby'])
        print('question timestamp : ',x['question timestamp'])
        print('question title : ',x['question title'])
        print('question description : ',x['question description'])
        print('question tag : ',x['question tag'])
        print('question answers : \n')
        for a in x['question answers']:
            for b in a:
                print(b,' : ',a[b])
            print('\n')
        print('\n\n')
def collect_data_from_question(keyword):
    mydb = sqlite3.connect('server_data.db')
    if keyword != 'none':
        con = mydb.execute("SELECT  Q.question_id,A.username,Q.timestamp,Q.title, Q.description, Q.tag FROM questions Q join authentication A on (Q.user_id == A.user_id) where Q.user_id = ? order by Q.timestamp DESC ;",[keyword])
        result= con.fetchall()
        mydb.close()
        return result
    else:
        con = mydb.execute("SELECT  A.username,Q.question_id,Q.timestamp, Q.description, Q.tag FROM questions Q join authentication A on (Q.user_id == A.user_id) order by Q.timestamp DESC ;")
        result= con.fetchall()
        mydb.close()
        return result

def collect_data_form_answers(question_id):
    mydb = sqlite3.connect('server_data.db')
    con = mydb.execute("SELECT answer_id,timestamp,answer FROM answers where question_id = ? order by timestamp DESC;",[question_id])
    result= con.fetchall()
    mydb.close()
    return result

def gather_data(select_key='none',search_key ='none'):
    post={'question_id':'','question postedby':'','question timestamp':'','question title':'','question description':'','question tag':'','question answers':''}
    answers={'answer_id':'','answer timestamp':'','answer':''}
    total_answers=[]
    total_post=[]
    quesion_data=collect_data_from_question(select_key)
    for q in quesion_data:
        # post.clear()
        print(q)
        if search_key !='none':
            print("found")
        else:
            answer_data=collect_data_form_answers(q[0])
            print('----')
            answers.clear()
            if len(answer_data)!=0:
                for a in answer_data:
                    print(a)
                    print('\n')
                    answers['answer_id']=a[0]
                    answers['answer timestamp']=a[1]
                    answers['answer']=a[2]
                    total_answers.append(answers.copy())
                    
        post['question_id']=q[0]
        post['question postedby']=q[1]
        post['question timestamp']=q[2]
        post['question title']=q[3]
        post['question description']=q[4]
        post['question tag']=q[5]
        post['question answers']=total_answers
        total_post.append(post.copy())
        
        post.clear()
        print('\n\n---')
        test(total_post)
        print('---\n\n')

gather_data(2)