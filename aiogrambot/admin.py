from django.contrib import admin
from .models import User, Teacher, Level, ExistingStudent, TrialVideos, Answer, \
    Question, LessonOrder, PrimeVideo, Tests, PrimeTest


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'chat_id',
        'full_name',
        'phone_number',
        'created_at'
    ]
    search_fields = [
        'chat_id',
        'full_name',
        'phone_number',
    ]
    list_filter = [
        'created_at',
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'phone_number',
    ]
    search_fields = [
        'full_name',
        'phone_number',
    ]
    list_filter = [
        'full_name',
        'phone_number',
    ]


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = [
        'level',
    ]
    search_fields = [
        'level',
    ]
    list_filter = [
        'level',
    ]


@admin.register(ExistingStudent)
class ExistingStudentAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'phone_number',
        'teacher',
        'level',
    ]
    search_fields = [
        'full_name',
        'phone_number',
        'teacher',
        'level',
    ]
    list_filter = [
        'full_name',
        'phone_number',
        'teacher',
        'level',
    ]


#
@admin.register(TrialVideos)
class TrialVideosAdmin(admin.ModelAdmin):
    list_display = [
        'video',
        'level',
        'lesson_name',
        'video_file_id',
    ]
    search_fields = [
        'video',
        'level',
        'lesson_name',
        'video_file_id',
    ]
    list_filter = [
        'video',
        'level',
        'lesson_name',
        'video_file_id',
    ]


#
@admin.register(LessonOrder)
class LessonOrderAdmin(admin.ModelAdmin):
    list_display = [
        'lessonName'
    ]
    search_fields = [
        'lessonName'
    ]


@admin.register(PrimeVideo)
class PrimeVideoAdmin(admin.ModelAdmin):
    list_display = [
        'video',
        'level',
        'lesson_name',
        'video_file_id',
    ]
    search_fields = [
        'video',
        'level',
        'lesson_name',
        'video_file_id',
    ]
    list_filter = [
        'video',
        'level',
        'lesson_name',
        'video_file_id',
    ]


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = [
        'test_title',
        'level',
        'lesson_name',
        'test_link',
        'is_active',
    ]
    search_fields = [
        'test_title',
        'level',
        'lesson_name',
        'test_link',
    ]
    list_filter = [
        'level',
        'lesson_name',
    ]


#
@admin.register(PrimeTest)
class PrimeTestAdmin(admin.ModelAdmin):
    list_display = [
        'test_title',
        'level',
        'teacher',
        'lesson_name',
        'test_link',
        'is_active',
    ]
    search_fields = [
        'test_title',
        'level',
        'teacher',
        'lesson_name',
        'test_link',
        'is_active',
    ]
    list_filter = [
        'level',
        'teacher',
        'lesson_name',
    ]


# class AnswerInlineModel(admin.TabularInline):
#     model = Answer
#     fields = [
#         'answer',
#         'is_correct',
#     ]
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     fields = [
#         'title',
#         'points',
#         'level',
#         'open_period'
#     ]
#     list_display = [
#         'title',
#         'updated_at'
#     ]
#     inlines = [
#         AnswerInlineModel,
#     ]
#
#
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = [
#         'answer',
#         'is_correct',
#         'question'
#     ]
