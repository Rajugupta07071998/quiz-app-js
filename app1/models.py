from django.db import models
import uuid

# Create your models here.

class Quiz_Table(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100,blank=True)
    option4 = models.CharField(max_length=100, blank=True)
    answer = models.CharField(max_length=100)


class QuizQuestions(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    question_text = models.TextField(null=False)

    def __str__(self):
        return self.question_text


class QuizAnswers(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    answer_value = models.CharField(max_length=100, null=False)
    answer_text = models.TextField(null=False)
    question = models.ForeignKey(QuizQuestions, null=False, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text





class QuizCorrectAnswers(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    answer = models.ForeignKey(QuizAnswers, null=False, on_delete=models.CASCADE)

 
class State(models.Model):
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

