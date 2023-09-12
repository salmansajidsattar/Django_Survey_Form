from django.db import models

# # Create your models here.
class Question(models.Model):
    Question_Key=models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=100)
    def __str__(self):
        return self.question_text
    
class Modern_Home(models.Model):
    Question_Key=models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=100)
    def __str__(self):
        return self.question_text
    
class Sales_team(models.Model):
    Question_Key=models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=100)
    def __str__(self):
        return self.question_text

class Finished_Inventory(models.Model):
    Question_Key=models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=100)
    def __str__(self):
        return self.question_text
    
class Builder_Data(models.Model):
    Builder_Key=models.AutoField(primary_key=True)
    Builder_name=models.CharField(max_length=50,null=False)
    Community=models.CharField(max_length=50,null=False)
    Inspected_by=models.CharField(max_length=50,null=True,default="")
    date_time=models.DateTimeField(null=True,default="")
    Summary_Description=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.Community
    def __str__(self):
        return self.Builder_name
    def __str__(self):
        return self.Inspected_by
    def __str__(self):
        return self.Summary_Description

class PDFDocument(models.Model):
    pdf_file = models.FileField(upload_to='pdfs')

# class Join(models.Model):
#     Join_Key=models.AutoField(primary_key=True)
#     Foriegn_key=models.ForeignKey(Builder_Data, on_delete=models.CASCADE)
#     mcq_question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer=models.CharField(max_length=2,null=False)
#     image_Description=models.CharField(max_length=250,null=True)
#     image = models.ImageField(upload_to="uploads",null=True)
#     def __str__(self):
#         return self.answer
#     def __str__(self):
#         return self.image_Description
#     def __str__(self):
#         return self.Foriegn_key

# class Join_Modern_Home(models.Model):
#     Join_Key=models.AutoField(primary_key=True)
#     Foriegn_key=models.ForeignKey(Builder_Data, on_delete=models.CASCADE)
#     mcq_question = models.ForeignKey(Modern_Home, on_delete=models.CASCADE)
#     answer=models.CharField(max_length=2,null=False)
#     image_Description=models.CharField(max_length=250,null=True)
#     image = models.ImageField(upload_to="uploads_1",null=True)
#     def __str__(self):
#         return self.answer
#     def __str__(self):
#         return self.Foriegn_key
#     def __str__(self):
#         return self.image_Description

# class Join_Sales(models.Model):
#     Join_Key=models.AutoField(primary_key=True)
#     Foriegn_key=models.ForeignKey(Builder_Data, on_delete=models.CASCADE)
#     mcq_question = models.ForeignKey(Sales_team, on_delete=models.CASCADE)
#     answer=models.CharField(max_length=2,null=False)
#     image_Description=models.CharField(max_length=250,null=True)
#     image = models.ImageField(upload_to="uploads_2",null=True)
#     def __str__(self):
#         return self.answer
#     def __str__(self):
#         return self.Foriegn_key
#     def __str__(self):
#         return self.image_Description

# class Join_Inventory(models.Model):
#     Join_Key=models.AutoField(primary_key=True)
#     Foriegn_key=models.ForeignKey(Builder_Data, on_delete=models.CASCADE)
#     mcq_question = models.ForeignKey(Finished_Inventory, on_delete=models.CASCADE)
#     answer=models.CharField(max_length=2,null=False)
#     image_Description=models.CharField(max_length=250,null=True)
#     image = models.ImageField(upload_to="uploads_3",null=True)
#     def __str__(self):
#         return self.answer
#     def __str__(self):
#         return self.Foriegn_key
#     def __str__(self):
#         return self.image_Description
    
# class Add_address(models.Model):
#     Foriegn_key=models.ForeignKey(Builder_Data, on_delete=models.CASCADE)
#     address=models.CharField(max_length=150,null=False)
#     def __str__(self):
#         return self.Foriegn_key
#     def __str__(self):
#         return self.address

# class ImageUpload(models.Model):
#     Foriegn_key=models.ForeignKey(Add_address, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="Inventory_uploads")     
#     def __str__(self):
#         return self.Foriegn_key.address 


