from random import randint

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.text import slugify
from rest_framework import serializers

from django.http import JsonResponse



from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Course, Lessons, Comment, Category, Contact
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer, CommentsSerializer, CategorySerializer, QuizSerializer, UserSerializer, ContactSerializer


@api_view(['POST'])
def create_course(request):
    status = request.data.get('status')

    print(request.data)

    if status == 'published':
        status = 'draft'

    course = Course.objects.create(
        title=request.data.get('title'),
        slug='%s-%s' % (slugify(request.data.get('title')), randint(1000, 10000)),
        short_description=request.data.get('short_description'),
        long_description=request.data.get('long_description'),
        status=status,
        created_by=request.user
    )

    for id in request.data.get('categories'):
        course.categories.add(id)
    
    course.save()

    # Lessons

    for lesson in request.data.get('lessons'):
        tmp_lesson = Lessons.objects.create(
            course=course,
            title=lesson.get('title'),
            slug=slugify(lesson.get('title')),
            short_description=lesson.get('short_description'),
            long_description=lesson.get('long_description'),
            status=Lessons.DRAFT
        )

    return Response({'course_id': course.id})



@api_view(['GET'])
def get_quiz(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.filter(status=Course.PUBLISHED)

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_frontpage_courses(request):
    courses = Course.objects.filter(status=Course.PUBLISHED)[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def get_course(request, slug):
    course = Course.objects.filter(status=Course.PUBLISHED).get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    if request.user.is_authenticated:
        course_data = course_serializer.data
    else:
        course_data = {}

    return Response({
        'course': course_data,
        'lessons': lesson_serializer.data
    })

@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    serializer = CommentsSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
   
    course = Course.objects.get(slug=course_slug)
    lesson = Lessons.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(course=course, lesson=lesson, name=data.get('name'), content=data.get('content'), created_by=request.user)

    serializer = CommentsSerializer(comment)

    return Response(serializer.data)

@api_view(['GET'])
def get_author_courses(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = user.courses.filter(status=Course.PUBLISHED)

    user_serializer = UserSerializer(user, many=False)
    courses_serializer = CourseListSerializer(courses, many=True)

    return Response({
        'courses': courses_serializer.data,
        'created_by': user_serializer.data
    })



@api_view(['POST'])
def submit_contact(request):
    # Assuming you have a Contact model and ContactSerializer for serializing data

    # Check if the request method is POST
    if request.method == 'POST':
        # Deserialize the data using the ContactSerializer
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            # If the data is valid, save it to the database
            serializer.save()

            # You can customize the response data as needed
            response_data = {
                'message': 'Contact form submitted successfully.'
            }

            return Response(response_data)
        else:
            # If the data is not valid, return an error response
            return Response(serializer.errors, status=400)
    else:
        # Handle other HTTP methods if needed
        return Response({'message': 'Method not allowed.'}, status=405)
