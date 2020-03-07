from sklearn import metrics
import pandas as pd
import os
import csv

import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import anytree
from .models import Job,Node,Skillset,Tool,Resource,M_to_M,Aptitude_Test

# Create your views here.
def HomePage(request):
    print("Printed in views.Homepage")
    return render(request,'CareerGuidance/HomePage.html')

def InputForm(request):
    print("Printed in views.InputForm")
    
    return render(request,'CareerGuidance/InputForm.html')

def Output(request):
    params = {}
    from . import tree
    #print(tree.mba)
    print("Printed in views.Output")
    if(request.method == 'POST'):
        Tools = []
        Resources = []
        # Job=[]
        Path = []
        age = request.POST.get('age')
        qualification = request.POST.get('qualification')
        interest = request.POST.get('interest')
        # print(interest,age,qualification)
        job = Job.objects.get(Job_Name=interest)
        print(job.Job_Name)
        print(job.Job_id)
        try:
            n_id = M_to_M.objects.get(Node_id = job.Job_id)
        except ObjectDoesNotExist:
            n_id = 1
        finally:
            pass
        
        sk_id = Skillset.objects.get(Job_id= job.Job_id)
        print(sk_id.Skill_Name)
        # Resources = list(sk_id.Skill_Name)
        # R_id = 
        # relation = Node.objects.get(Node_id = n_id.Node_id)
        R_id = Resource.objects.filter(Skill_id = sk_id.Skill_id)
        #print(R_id,R_id.Resource_Link)
        print(R_id,'hi')
        for i in R_id:
            Resources.append(i.Resource_Link)
        try:
            T_id = Tool.objects.get(Skill_id = sk_id.Skill_id )
        except ObjectDoesNotExist:
            T_id = 1
        finally:
            pass
        
        print(T_id.Tool_Name,T_id.Tool_id)
        Tools = T_id.Tool_Name
        Tdante = []
        Tdante = Tools.strip('[]').split(',')
        print(Tools,Resources)
        Skills = []
        Skills = sk_id.Skill_Name.strip('[]').split(',')
        print(Skills)
        pros = []
        cons = []
        Path_list = []
        flag = 0
        Time_list = []
        Total_Time = 0
        Cumulative_Time = []
        
        mynode = n_id.Node_id.Node_Name


        if mynode[0] == '[':
            mynode = mynode.strip("[]").split(',')
            for i in mynode:
                # schema = tree.route(i)
                node = tree.a
                for k in node:
                    if i == k.name:
                        for j in k.path[::-1]:
                            break
        else:
            node = tree.a
            for i in node:
                if i.name == mynode:
                    for j in i.path[::-1]:
                        print(j)
                        Cumulative_Time.append(Total_Time)
                        Time_list.append(i.avgTime)
                        new_id = Node.objects.get( Node_Name = j.name )
                        pros.append(new_id.pros)
                        cons.append(new_id.cons)
                        if flag == 0 :
                            j = str(j)
                            Path_list = j[5:-12].strip("''").split('/')[1:]
                            
                            flag = flag + 1 

        pros = pros[::-1]
        cons = cons[::-1]

        index = Path_list.index(qualification)

        Path_list = Path_list[index::]
        pros = pros[index::]
        cons = cons[index::]
        Time_list = Time_list[index::]


        data = []
        for i in range(len(Path_list)):
            dictionary = {}
            dictionary['Stage'] = i+1
            dictionary['Path_list'] = Path_list[i]
            dictionary['pros'] = pros[i]
            dictionary['cons'] = cons[i]
            dictionary['Time_list'] = Time_list[i]
            data.append(dictionary)

        params = {'data' : data ,'total_length':len(Path_list),'resources':Resources,'tools':Tdante}

    return render(request,'CareerGuidance/OutputPage.html',params) 

def aptitude(request):
    Questions = Aptitude_Test.objects.all()
    Questions_Dict = {'Questions':Questions}
    print(Questions)
    for i in Questions:
        print(i.Question)
    if request.method == 'POST':
        Ans1 = request.POST.get('Ans1')
        Ans2 = request.POST.get('Ans2')
        Ans3 = request.POST.get('Ans3')
        Ans4 = request.POST.get('Ans4')
        Ans5 = request.POST.get('Ans5')
        Ans6 = request.POST.get('Ans6')
        Ans7 = request.POST.get('Ans7')
        Ans8 = request.POST.get('Ans8')
        Ans9 = request.POST.get('Ans9')
        Ans10 = request.POST.get('Ans10')
        ls = [Ans1,Ans2,Ans3,Ans4,Ans5,Ans6,Ans7,Ans8,Ans9,Ans10]
        print(Ans10)
        Answers = []
        for i in range(0,10):
            if ls[i] == Aptitude_Test.objects.get(Question_id = i+1).Answer:
                Answers.append(1)
            else :
                Answers.append(0)
        print(Answers)
        col_name = ['Ans_1','Ans_2','Ans_3','Ans_4','Ans_5','Ans_6','Ans_7','Ans_8','Ans_9','Ans_10','Target']
        df = pd.read_csv('CareerGuidance/data.csv',names = col_name)
        df.head()
        df.Target.unique()
        y=df.iloc[:,-1]
        y= np.array(y)

        X=df[['Ans_1', 'Ans_2', 'Ans_3', 'Ans_4','Ans_5','Ans_6','Ans_7','Ans_8','Ans_9','Ans_10',]]
        y=df['Target']  # Labels

        clf=RandomForestClassifier(n_estimators=100)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
        clf.fit(X_train,y_train)
        y_pred=clf.predict(X_test)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print("Accuracy:",(metrics.accuracy_score(y_test, y_pred))*100)
        species_idx = clf.predict([Answers])[0]
        print(species_idx)
        # newrow = ls.append(species_idx)
        # newrow = [Ans1,Ans2,Ans3,Ans4,Ans5,Ans6,Ans7,Ans8,Ans9,Ans10,species_idx]
        Answers.append(species_idx)
        
        # print(dante)
        path = os.path.join(BASE_DIR,'CareerGuidance\data.csv')
        with open(path,'a',newline='') as outfile:
            append = csv.writer(outfile)
            append.writerow(Answers)
        Questions_Dict = {'Questions':Questions,'Answer':'We hope you choose a career in '+ species_idx +''}


    return render (request, 'CareerGuidance/aptitude.html',Questions_Dict)

