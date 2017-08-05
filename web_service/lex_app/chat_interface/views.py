
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

import json
import logging

APP_NAME = 'yo'
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)


@csrf_exempt
def index(request):
    """
    :param request:
    :return:
            (django.http import JsonResponse)
    """
    print("PUTA")
    print(request)
    return HttpResponse("Hello world: {}".format(request))