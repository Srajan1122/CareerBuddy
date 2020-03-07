from django.core.exceptions import ObjectDoesNotExist
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
    return render (request, 'CareerGuidance/aptitude.html')

