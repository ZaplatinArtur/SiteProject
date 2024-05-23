from django.shortcuts import render
<<<<<<< HEAD
import cv2
=======

>>>>>>> d737c4a (Initial commit)

# Create your views here.
def pool(request):
    data = {
        'title': "Опросник"
    }
<<<<<<< HEAD

=======
>>>>>>> d737c4a (Initial commit)
    return render(request, 'polling/pool.html',data)