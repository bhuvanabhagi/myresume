from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

def photo_view(request):
    # Adjust the path to the location of your image file
    file_path = os.path.join(settings.BASE_DIR, 'static/images/photo.jpg')
    return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')

def resume_view(request):
    # Resume information for a second-year student
    context = {
        'name': 'BHAGI BHUVANESWARI',
        'email': '2310080008@klh.edu.in',
        'phone': '8317659999',
        'address': '104 - Chapel Street , LB Nagar, Hyderabad, Telangana',
        'summary': 'Second-year Artificial Intelligence and Data Science student passionate about web development, data science, and mobile app development. Quick learner with a foundation in programming and a keen interest in gaining hands-on experience.',
        'skills': [
            'Python', 
            'HTML & CSS', 
            'DSA IN C', 
            'Java', 
            'Django Basics', 
            'Data Analysis with Pandas', 

        ],
        'education': [
            {
                'degree': 'B.Tech',
                'institution': 'KL University',
                'year': 'Expected 2027'
            },
            {
                'degree': 'SSC',
                'institution': 'Sri Chaitanya School',
                'year': '2021'
            },
            {
                'degree': 'IPE',
                'institution': 'Sri Chaitanya College',
                'year': '2023'
            }
        ],
        'experience': [
            {
                'position': 'Event Coordinator',
                'company': 'School Annual Function',
                'duration': '2019',
                'description': 'Ensured smooth event flow, and resolved any last-minute issues. Received positive feedback.'
            }
        ],
        'projects': [
            {
                'title': 'Lifestyle Routine Maker Website',
                'description': 'Developed a responsive website to showcase projects and skills. Built using HTML, CSS, and basic JavaScript.',
                'technologies': ['HTML', 'CSS', 'JavaScript']
            },
            {
                'title': 'Data Analysis Project',
                'description': 'Analyzed a dataset using Pandas to uncover trends and visualized findings with Matplotlib.',
                'technologies': ['Python', 'Pandas', 'Matplotlib']
            },
            {
                'title': 'Basic Calculator App',
                'description': 'Created a calculator app for Android using Java. The app allows users to perform basic arithmetic operations.',
                'technologies': ['Java', 'Android']
            }
        ],
        'extracurriculars': [
            {
                'activity': 'Member, Coding Club',
                'description': 'Participated in weekly coding challenges under our department.'
            },
            {
                'activity': 'Tech participant',
                'description': 'Participated in college tech events in Avinya conducted by our college.'
            }
        ],
        'languages': [
            {'language': 'English', 'proficiency': 'Fluent'},
            {'language': 'Telugu', 'proficiency': 'Native'},
            {'language': 'Hindi', 'proficiency': 'Intermediate'}
        ],
        'achievements': [
            {
                'title': 'Top Scorer in IPE',
                'description': 'Ranked among the top 5% in the IPE exams in 2023.'
            },
            
        ],
        'interests': [
            'Machine Learning', 
            'cooking', 
            'Traveling', 
            'Reading tech blogs'
        ],
        'certifications': [
            {
                'name': 'Python',
                'provider': 'GFG',
                'year': '2023'
            },
    
        ],
        'linkedin': 'https://www.linkedin.com/in/bhuvaneswari-bhagi-7ab35131a/',
        'github': 'https://github.com/bhuvana_bhagi'
    }
    return render(request, 'resume.html', context)
