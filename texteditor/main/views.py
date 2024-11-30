import json
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator

@login_required
def home(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        text = request.POST.get('text', '')

        if action == 'bold':
            result = f"<b>{text}</b>"
        elif action == 'italic':
            result = f"<i>{text}</i>"
        elif action == 'capitalize':
            result = text.upper()
        elif action == 'remove_whitespace':
            result = text.replace(' ', '')
        elif action == 'lowercase':
            result = text.lower()
        elif action == 'titlecase':
            result = title_case(text)
        else:
            result = text  

        return JsonResponse({'result': result})

    return render(request, 'main/home.html')


def title_case(text):
    return ' '.join([word.capitalize() for word in text.split()])


@csrf_exempt
def translate_to_urdu(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            text = data.get('text', '')
            translator = Translator()
            translation = translator.translate(text, dest='ur')
            return JsonResponse({'result': translation.text})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
