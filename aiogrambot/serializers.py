from rest_framework import serializers

from .models import User, Teacher, Level, ExistingStudent, TrialVideos, \
    Question, Answer, LessonOrder, PrimeVideo, Tests, PrimeTest
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LessonOrderSerializer(ModelSerializer):
    class Meta:
        model = LessonOrder
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ExistingStudentSerializer(ModelSerializer):
    teacher = serializers.StringRelatedField()
    level = serializers.StringRelatedField()

    class Meta:
        model = ExistingStudent
        fields = '__all__'


class TrialVideosSerializer(ModelSerializer):
    level = serializers.StringRelatedField()
    lesson_name = serializers.StringRelatedField()

    class Meta:
        model = TrialVideos
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer',
            'is_correct',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    level = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = [
            'id', 'title', 'level', 'points', 'answer', 'open_period'
        ]


class PrimeVideoSerializer(ModelSerializer):
    level = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()
    lesson_name = serializers.StringRelatedField()

    class Meta:
        model = PrimeVideo
        fields = '__all__'


class TestsSerializer(ModelSerializer):
    level = serializers.StringRelatedField()
    lesson_name = serializers.StringRelatedField()

    class Meta:
        model = Tests
        fields = '__all__'


class PrimeTestSerializer(ModelSerializer):
    level = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()
    lesson_name = serializers.StringRelatedField()

    class Meta:
        model = PrimeTest
        fields = '__all__'
