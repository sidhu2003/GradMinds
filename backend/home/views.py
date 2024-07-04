from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict(request):
    form = StudentForm()
    message = ""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            preferred_branch = form.cleaned_data['preferred_branch']
            score = form.cleaned_data['score']
            category = form.cleaned_data['category']
            form.save()
            data_map = {
                ('IIT Kharagpur', 'General'): [674],
                ('IIT Kharagpur', 'OBC'): [592],
                ('IIT Kharagpur', 'SC'): [385],
                ('IIT Kharagpur', 'ST'): [254],

                ('IIT Bombay', 'General'): [785],
                ('IIT Bombay', 'OBC'): [633],
                ('IIT Bombay', 'SC'): [418],
                ('IIT Bombay', 'ST'): [387],

                ('IIT Madras', 'General'): [785],
                ('IIT Madras', 'OBC'): [633],
                ('IIT Madras', 'SC'): [418],
                ('IIT Madras', 'ST'): [378],

                ('IIT Guwahati', 'General'): [763],
                ('IIT Guwahati', 'OBC'): [722],
                ('IIT Guwahati', 'SC'): [696],
                ('IIT Guwahati', 'ST'): [541],

                ('IIT Hyderabad', 'General'): [598],
                ('IIT Hyderabad', 'OBC'): [552],
                ('IIT Hyderabad', 'SC'): [490],
                ('IIT Hyderabad', 'ST'): [747],

                ('IIT Jodhpur', 'General'): [382],
                ('IIT Jodhpur', 'OBC'): [398],
                ('IIT Jodhpur', 'SC'): [280],
                ('IIT Jodhpur', 'ST'): [219],

                ('IIT Kanpur', 'General'): [475],
                ('IIT Kanpur', 'OBC'): [427],
                ('IIT Kanpur', 'SC'): [285],
                ('IIT Kanpur', 'ST'): [285],

                ('IIT Patna', 'General'): [549],
                ('IIT Patna', 'OBC'): [538],
                ('IIT Patna', 'SC'): [439],
                ('IIT Patna', 'ST'): [410],

                ('IIT Tirupati', 'General'): [637],
                ('IIT Tirupati', 'OBC'): [557],
                ('IIT Tirupati', 'SC'): [498],
                ('IIT Tirupati', 'ST'): [318],

                ('NIT Calicut', 'General'): [474],
                ('NIT Calicut', 'OBC'): [339],
                ('NIT Calicut', 'SC'): [263],
                ('NIT Calicut', 'ST'): [221],

                ('NIT Rourkela', 'General'): [579],
                ('NIT Rourkela', 'OBC'): [496],
                ('NIT Rourkela', 'SC'): [309],
                ('NIT Rourkela', 'ST'): [289],

                ('NIT Surathkal', 'General'): [501],
                ('NIT Surathkal', 'OBC'): [460],
                ('NIT Surathkal', 'SC'): [375],
                ('NIT Surathkal', 'ST'): [311],

                ('NIT Tiruchirappalli', 'General'): [640],
                ('NIT Tiruchirappalli', 'OBC'): [460],
                ('NIT Tiruchirappalli', 'SC'): [375],
                ('NIT Tiruchirappalli', 'ST'): [356],

                ('NIT Warangal', 'General'): [750],
                ('NIT Warangal', 'OBC'): [663],
                ('NIT Warangal', 'SC'): [414],
                ('NIT Warangal', 'ST'): [291],
            }
            college_name = 'IIT Kharagpur'
            flag = 1
            key = (college_name, category)
            if key not in data_map:
                flag = 0
            else:
                if score < data_map[key][0]:
                    flag = 0
            if flag == 1: 
                message = "Congratulations! You are eligible"    
            else:
                message = "Sorry! You are not eligible"
    return render(request, 'predict.html', {'form': form, 'message': message})

    
def analysis(request):
    return render(request, 'analysis.html')

