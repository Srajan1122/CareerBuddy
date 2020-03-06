from django.db import models

# Create your models here.



class Job(models.Model):
    Job_id = models.IntegerField(
        primary_key=True, unique=True, null=False, blank=False)
    Job_Name = models.CharField(max_length = 50,default = "")
    def __str__(self):
        return self.Job_Name
class Node(models.Model):
    Node_id = models.IntegerField(
        primary_key=True, unique=True, null=False, blank=False)
    Node_Name = models.CharField(max_length = 50,default = "")
    def __str__(self):
        return self.Node_Name
class M_to_M(models.Model):
    Node_id = models.ForeignKey(
        Node, on_delete=models.CASCADE, default='null')
    Job_id = models.ForeignKey(
        Job, on_delete=models.CASCADE, default='null')
class Skillset(models.Model):
    Skill_id = models.IntegerField(
        primary_key=True, unique=True, null=False, blank=False)
    Skill_Name = models.CharField(max_length = 50,default = "")
    Job_id = models.ForeignKey(
        Job, on_delete=models.CASCADE, default='null')
    def __str__(self):
        return self.Skill_Name
class Resource(models.Model):
    Resource_id = models.IntegerField(
        primary_key=True, unique=True, null=False, blank=False)
    Resource_Link = models.CharField(max_length = 1000 , default = "")
    Skill_id =   models.ForeignKey(
        Skillset, on_delete=models.CASCADE, default='null')
    def __str__(self):
        return self.Resource_Link
class Tool(models.Model):
    Tool_id = models.IntegerField(
        primary_key=True, unique=True, null=False, blank=False)
    Tool_Name = models.CharField(max_length = 1000 , default = "")
    Skill_id =   models.ForeignKey(
        Skillset, on_delete=models.CASCADE, default='null')
    def __str__(self):
        return self.Tool_Name

    