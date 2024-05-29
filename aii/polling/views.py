from django.shortcuts import render

import cv2
#import algoritm.read_plickers as al



# Create your views here.
def pool(request):
    data = {
        'title': "Опросник"
    }


    return render(request, 'polling/pool.html',data)