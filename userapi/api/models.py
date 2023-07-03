from django.db import models


class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    added_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#post model
class post(models.Model):
    post_id= models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    creation_date=models.DateTimeField(auto_now=True)



#like model
class like(models.Model):
    like_id=models.AutoField(primary_key=True)
    post1=models.ForeignKey(post, on_delete=models.CASCADE)
    user1=models.ForeignKey(user, on_delete=models.CASCADE)