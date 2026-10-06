from django.shortcuts import render

def index(request):
    # Student data
    student = {
        'name': 'Rahul Verma',
        'marks': {
            'Maths': 85,
            'Science': 92,
            'English': 78,
            'History': 88,
            'Computer': 95
        }
    }
    
    # calculate total using sum()
    total = sum(student['marks'].values())
    
    # calculate percentage
    percent = (total / 500) * 100
    
    context = {
        'student_name': student['name'],
        'marks': student['marks'],
        'total': total,
        'percentage': percent
    }
    
    return render(request, 'task1_student_portal/index.html', context)
