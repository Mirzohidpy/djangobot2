from django.shortcuts import render
from .models import User, Teacher, Level, ExistingStudent, TrialVideos, Answer, Question, LessonOrder, PrimeVideo, \
    PrimeTest, Tests
from .serializers import UserSerializer, TeacherSerializer, LevelSerializer, ExistingStudentSerializer, \
    TrialVideosSerializer, QuestionSerializer, AnswerSerializer, \
    LessonOrderSerializer, PrimeVideoSerializer, PrimeTestSerializer, TestsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeacherList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class LevelList(ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ExistingStudentList(ListCreateAPIView):
    queryset = ExistingStudent.objects.all()
    serializer_class = ExistingStudentSerializer


class ExistingStudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = ExistingStudent.objects.all()
    serializer_class = ExistingStudentSerializer


class TrialVideosList(ListCreateAPIView):
    queryset = TrialVideos.objects.all()
    serializer_class = TrialVideosSerializer


class TrialVideosDetail(RetrieveUpdateDestroyAPIView):
    queryset = TrialVideos.objects.all()
    serializer_class = TrialVideosSerializer


class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerList(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class LessonOrderList(ListCreateAPIView):
    queryset = LessonOrder.objects.all()
    serializer_class = LessonOrderSerializer


class PrimeVideoList(ListCreateAPIView):
    queryset = PrimeVideo.objects.all()
    serializer_class = PrimeVideoSerializer


class PrimeVideoDetail(RetrieveUpdateDestroyAPIView):
    queryset = PrimeVideo.objects.all()
    serializer_class = PrimeVideoSerializer


class PrimeTestList(ListCreateAPIView):
    queryset = PrimeTest.objects.all()
    serializer_class = PrimeTestSerializer


class PrimeTestDetail(RetrieveUpdateDestroyAPIView):
    queryset = PrimeTest.objects.all()
    serializer_class = PrimeTestSerializer


class TestsList(ListCreateAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer


class TestsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
