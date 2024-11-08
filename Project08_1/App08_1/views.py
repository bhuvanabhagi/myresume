from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def calculate(request):
    if request.method == 'POST':
        try:
            # Convert input values to float (works for both integers and floats)
            val1 = float(request.POST['num1'])
            val2 = float(request.POST['num2'])
            operation = request.POST['operation']

            # Perform calculation based on the selected operation
            if operation == 'add':
                result = val1 + val2
            elif operation == 'subtract':
                result = val1 - val2
            elif operation == 'multiply':
                result = val1 * val2
            elif operation == 'divide':
                if val2 != 0:
                    result = val1 / val2
                else:
                    result = "Division by zero error!"
            else:
                result = "Invalid operation!"

            return render(request, 'result.html', {'result': result})

        except ValueError:
            return HttpResponse("Invalid input! Please enter valid numbers.")
    return HttpResponse("Invalid request method.")
