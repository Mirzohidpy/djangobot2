from django.urls import path
from .views import UserList, TeacherList, LevelList, ExistingStudentList, \
    UserDetail, TrialVideosList, TrialVideosDetail, QuestionList, QuestionDetail, AnswerList, AnswerDetail, \
    LessonOrderList, PrimeVideoList, PrimeVideoDetail, ExistingStudentDetail, TestsList, TestsDetail, PrimeTestList, \
    PrimeTestDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('teachers/', TeacherList.as_view()),
    path('levels/', LevelList.as_view()),
    path('existing-students/', ExistingStudentList.as_view()),
    path('existing-students/<int:pk>/', ExistingStudentDetail.as_view()),
    path('trial-videos/', TrialVideosList.as_view()),
    path('trial-videos/<int:pk>/', TrialVideosDetail.as_view()),
    path('questions/', QuestionList.as_view()),
    path('questions/<int:pk>/', QuestionDetail.as_view()),
    path('answers/', AnswerList.as_view()),
    path('answers/<int:pk>/', AnswerDetail.as_view()),
    path('lesson-order/', LessonOrderList.as_view()),
    path('prime-videos/', PrimeVideoList.as_view()),
    path('prime-videos/<int:pk>/', PrimeVideoDetail.as_view()),
    path('tests/', TestsList.as_view()),
    path('tests/<int:pk>/', TestsDetail.as_view()),
    path('prime-tests/', PrimeTestList.as_view()),
    path('prime-tests/<int:pk>/', PrimeTestDetail.as_view()),
]
