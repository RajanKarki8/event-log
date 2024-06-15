import json
from pathlib import Path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

json_file_path = Path('data.json')

def read_data():
    if not json_file_path.exists():
        return []
    with open(json_file_path, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def index(request):
    events = read_data()
    return render(request, 'main/listing.html', {'events': events})

@login_required(login_url='/login')
def create_event(request):
    if request.method == 'POST':
        events = read_data() 
        new_event = {
            'id': str(len(events) + 1),
            'speaker_name': request.POST['speaker_name'],
            'speech_title': request.POST['speech_title'],
            'description': request.POST['description'],
            'total_audience': request.POST['total_audience'],
            'date': request.POST['date'],
            'gender': request.POST['gender'],
            'Genre': request.POST['Genre']
        }
        events.append(new_event)
        write_data(events)
        return redirect('index')
    return render(request, 'main/create.html')

@login_required(login_url='/login')
def update_event(request, pk):
    events = read_data()
    event = next((event for event in events if event['id'] == pk), None)
    if not event:
        return HttpResponse('Event not found', status=404)
    if request.method == 'POST':
        event['speaker_name'] = request.POST['speaker_name']
        event['speech_title'] = request.POST['speech_title']
        event['description'] = request.POST['description']
        event['total_audience'] = request.POST['total_audience']
        event['date'] = request.POST['date']
        event['gender'] = request.POST['gender']
        event['Genre'] = request.POST['Genre']
        write_data(events)
        return redirect('index')
    return render(request, 'main/update.html', {'event': event})

@login_required(login_url='/login')
def delete_event(request, pk):
    events = read_data()
    events = [event for event in events if event['id'] != pk]
    write_data(events)
    messages.info(request, 'Event deleted successfully!')
    return redirect('index')


