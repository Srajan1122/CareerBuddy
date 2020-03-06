from django.shortcuts import render
import anytree
from .models import Job,Node,Skillset,Tool,Resource,M_to_M

# Create your views here.
def HomePage(request):
    print("Printed in views.Homepage")
    return render(request,'CareerGuidance/HomePage.html')

def InputForm(request):
    print("Printed in views.InputForm")
    
    return render(request,'CareerGuidance/InputForm.html')

def Output(request):
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
        # print(job.Job_Name)
        n_id = M_to_M.objects.get(Node_id = job.Job_id)
        sk_id = Skillset.objects.get(Job_id= job.Job_id)
        print(sk_id.Skill_Name)
        # Resources = list(sk_id.Skill_Name)
        # R_id = 
        # relation = Node.objects.get(Node_id = n_id.Node_id)
        R_id = Resource.objects.get(Skill_id = sk_id.Skill_id)
        print(R_id,R_id.Resource_Link)
        Resources.append(R_id.Resource_Link)
        T_id = Tool.objects.get(Skill_id = sk_id.Skill_id )
        print(T_id.Tool_Name,T_id.Tool_id)
        Tools = T_id.Tool_Name
        Tdante = []
        Tdante = Tools.strip('[]').split(',')
        print(Tools,Resources)
        Skills = []
        Skills = sk_id.Skill_Name.strip('[]').split(',')
        print(Skills)
        Path_list = []
        flag = 0
        Time_list = []
        Total_Time = 0
        Cumulative_Time = []
        
        params = {'Skills':Skills,"Resource":Resources,"Tools":Tools,"Aim":job.Job_Name,}
        mynode = n_id.Node_id.Node_Name
        if mynode[0] == '[':
            mynode = mynode.strip("[]").split(',')
            for i in mynode:
                # schema = tree.route(i)
                node = tree.a
                for k in node:
                    print(i,k.name)
                    if i == k.name:
                        print(i,k)
                        for j in k.path[::-1]:
                            print(j)
                            break
        else:
            node = tree.a
            for i in node:
                print(i.name)
                if i.name == mynode:
                    for j in i.path[::-1]:
                        
                        # print(j[5:-12].strip("''").split('/'),type(j),j[5:-12])
                        # Path_list = j[5:-12].strip("''").split('/')[1:]
                        Total_Time = Total_Time + i.avgTime
                        Cumulative_Time.append(Total_Time)
                        Time_list.append(i.avgTime)
                        # print(avgTime)
                        if flag == 0 :
                            j = str(j)
                            Path_list = j[5:-12].strip("''").split('/')[1:]
                            flag = flag + 1


                        
                    
                        print(j)
        print(Path_list,Time_list)
        params = {'Skills':Skills,"Resource":Resources,"Tools":Tools,"Aim":job.Job_Name,'Path_list':Path_list,'Total_time':Total_Time,'Time_list':Time_list,'Cumulative_Time':Cumulative_Time}        
            
    return render(request,'CareerGuidance/OutputPage.html',params) 
