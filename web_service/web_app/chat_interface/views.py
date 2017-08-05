import logging

APP_NAME = 'yo'
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)


def index(request):
    """
    Anatomy of endpoint:
        /?token=XXX&endpoint=launch_emr&channel_name=tests&env=dev&cluster_name=diogo_test&core_nodes=1&task_nodes=1
    :param request:
    :return:
            (django.http import JsonResponse)
    """
    return request