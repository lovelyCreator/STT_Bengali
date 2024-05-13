from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# from django.http import StreamingHttpResponse
# import time

# def stream_transcription(request):
#     def event_stream():
#         while True:
#             # Perform live transcription (implement your live transcription logic here)
#             transcription = "Live transcription text..."
#             yield "data: {\"transcription\": \"%s\"}\n\n" % transcription
#             time.sleep(1)  # Simulate real-time updates every second
# .
#     response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
#     response['Cache-Control'] = 'no-cache'
#     return response