# from django.shortcuts import render
from django.http import HttpResponse
import logging
import random

# Create your views here.

def hello_world(request):
    logging.info("Received request to /hello/: {}".format(request))
    return HttpResponse("Hello World")

def hello_name(request, name):
    logging.info("Received request to /hello/<name>: {}".format(request))
    return HttpResponse(f"Hello {name}")


def draw_random(request):
    logging.info("Received request to /random/: {}".format(request))
    random_number = random.randint(0,100)
    return HttpResponse(f"Drawn number: {random_number}")

def draw_random_with_max(request, max_number):
    logging.info("Received request to /random/<max_number>: {}".format(request))
    
    random_number = random.randint(0,max_number)

    return HttpResponse(f"""
        The user entered the value {max_number}.
        The following number was drawn: {random_number}
        """)

def draw_random_with_min_and_max(request, min_number, max_number):
    logging.info("""
        Received request to /random/<max_number>/<min_number>: {}
        """.format(request)
    )
    random_number = random.randint(min_number,max_number)
    return HttpResponse(f"""
        The user entered the values {min_number} and {max_number}.
        The following number was drawn: {random_number}
        """)