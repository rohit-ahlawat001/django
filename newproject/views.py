from django.shortcuts import render
from django.http import HttpResponse

def show_Response(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to my Django page</h1>
        <p>Your page is working.</p>
    </body>
    </html>
    """
    return HttpResponse(html)


