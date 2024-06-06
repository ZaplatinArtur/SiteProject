from django.shortcuts import render

from .forms import ImageForm
from .models import Image
import threading
import tkinter as Tk
import cv2
import numpy as np

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            scan_photo(CLASS_TEST,"001.jpg")
            #at this point, I want to pass to the function a photo that has just been sent to the form
            return render(request, 'polling/pool.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()


    return render(request, 'polling/pool.html', {'form': form})


# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
import os, os.path

CATALOGUE = {28831199: (19, 'плохо'), 29323263: (32, 'хорошо'), 23063547: (11, 'удовлетворительно'), 33501183: (8, 'хорошо'), 33516503: (5, 'хорошо'),
             29322235: (34, 'хорошо'), 33548799: (8, 'плохо'), 27242493: (26, 'отлично'), 32975835: (27, 'хорошо'), 31436789: (19, 'отлично'),
             29356029: (8, 'отлично'), 33025017: (36, 'отлично'), 33532917: (35, 'отлично'), 33549819: (32, 'плохо'), 32992211: (23, 'хорошо'),
             32976887: (28, 'хорошо'), 28814847: (3, 'плохо'), 33516507: (3, 'хорошо'), 32993267: (22, 'хорошо'), 33501147: (11, 'хорошо'),
             32975859: (30, 'хорошо'), 26734577: (29, 'отлично'), 26718201: (30, 'отлично'), 20951007: (36, 'удовлетворительно'), 31452671: (4, 'плохо'),
             31451615: (28, 'плохо'), 23064539: (13, 'удовлетворительно'), 33517559: (4, 'хорошо'), 25161683: (28, 'удовлетворительно'), 18870227: (29, 'удовлетворительно'),
             33516531: (6, 'хорошо'), 31435263: (12, 'плохо'), 31436283: (36, 'плохо'), 33532383: (24, 'плохо'), 25161695: (4, 'удовлетворительно'),
             33500127: (9, 'хорошо'), 33517523: (7, 'хорошо'), 28815357: (14, 'отлично'), 25160667: (14, 'удовлетворительно'), 30928351: (21, 'плохо'),
             32976863: (25, 'хорошо'), 29322231: (36, 'хорошо'), 23047167: (35, 'удовлетворительно'), 25160703: (2, 'удовлетворительно'), 33024479: (25, 'плохо'),
             32993279: (16, 'хорошо'), 20950015: (34, 'удовлетворительно'), 33009653: (7, 'отлично'), 31436793: (18, 'отлично'), 20967411: (24, 'удовлетворительно'),
             26717663: (23, 'плохо'), 25160691: (26, 'удовлетворительно'), 30911999: (5, 'плохо'), 33008625: (39, 'отлично'), 33025535: (1, 'плохо'),
             27240927: (30, 'плохо'), 18869247: (3, 'удовлетворительно'), 30928885: (21, 'отлично'), 18870239: (5, 'удовлетворительно'), 30928379: (37, 'плохо'),
             29305855: (40, 'хорошо'), 23064575: (1, 'удовлетворительно'), 32976891: (26, 'хорошо'), 33009657: (6, 'отлично'), 33532411: (40, 'плохо'),
             32992251: (18, 'хорошо'), 29356017: (9, 'отлично'), 29322195: (39, 'хорошо'), 23064535: (21, 'удовлетворительно'), 20951035: (40, 'удовлетворительно'),
             29338111: (10, 'плохо'), 25161719: (16, 'удовлетворительно'), 32992223: (17, 'хорошо'), 27258873: (24, 'отлично'), 29355001: (40, 'отлично'),
             20966367: (6, 'удовлетворительно'), 33500151: (12, 'хорошо'), 30912509: (22, 'отлично'), 18852831: (39, 'удовлетворительно'), 33025013: (37, 'отлично'),
             27257343: (14, 'плохо'), 29323227: (35, 'хорошо'), 20967383: (20, 'удовлетворительно'), 33550325: (1, 'отлично'), 28813791: (27, 'плохо'),
             32992247: (20, 'хорошо'), 26718197: (31, 'отлично'), 20966355: (30, 'удовлетворительно'), 23048159: (37, 'удовлетворительно'), 23064563: (25, 'удовлетворительно'),
             23063507: (31, 'удовлетворительно'), 33009119: (17, 'плохо'), 29339641: (10, 'отлично'), 23063519: (7, 'удовлетворительно'), 33008637: (38, 'отлично'),
             30910943: (29, 'плохо'), 27242481: (27, 'отлично'), 27241983: (6, 'плохо'), 33549297: (33, 'отлично'), 26734589: (28, 'отлично'),
             33517535: (1, 'хорошо'), 25161723: (8, 'удовлетворительно'), 18853887: (33, 'удовлетворительно'), 25145343: (32, 'удовлетворительно'), 25144287: (38, 'удовлетворительно'),
             23063543: (19, 'удовлетворительно'), 26734079: (7, 'плохо'), 29323251: (38, 'хорошо'), 30928889: (20, 'отлично'), 33501143: (13, 'хорошо'),
             29339131: (34, 'плохо'), 32975831: (29, 'хорошо'), 33533937: (3, 'отлично'), 33009147: (33, 'плохо'), 28831733: (13, 'отлично'),
             32993243: (19, 'хорошо'), 31453169: (17, 'отлично'), 27258869: (25, 'отлично'), 33532921: (34, 'отлично'), 20966391: (18, 'удовлетворительно'),
             29323223: (37, 'хорошо'), 18869207: (23, 'удовлетворительно'), 20966395: (10, 'удовлетворительно'), 30912497: (23, 'отлично'), 27258335: (22, 'плохо'),
             33500115: (15, 'хорошо'), 32975871: (24, 'хорошо'), 33500155: (10, 'хорошо'), 32993239: (21, 'хорошо'), 33533949: (2, 'отлично'),
             27258363: (38, 'плохо'), 29339103: (18, 'плохо'), 18869211: (15, 'удовлетворительно'), 29322207: (33, 'хорошо'), 26717691: (39, 'плохо'),
             31436255: (20, 'плохо'), 20967387: (12, 'удовлетворительно'), 33517563: (2, 'хорошо'), 33008127: (9, 'плохо'), 33026033: (5, 'отлично'),
             25160663: (22, 'удовлетворительно'), 33549791: (16, 'плохо'), 29355519: (2, 'плохо'), 29354463: (26, 'плохо'), 18869235: (27, 'удовлетворительно'),
             31453181: (16, 'отлично'), 28815345: (15, 'отлично'), 32976851: (31, 'хорошо'), 33501171: (14, 'хорошо'), 26733023: (31, 'плохо'),
             29339637: (11, 'отлично'), 30927359: (13, 'плохо'), 18870263: (17, 'удовлетворительно'), 28831227: (35, 'плохо'), 28831737: (12, 'отлично'),
             33549309: (32, 'отлично'), 18870267: (9, 'удовлетворительно'), 33026045: (4, 'отлично'), 26716671: (15, 'плохо'), 28830207: (11, 'плохо')}


CLASS_TEST = [
    {'name': 'Андрей', 'surname': 'Иванов'},
    {'name': 'Аня', 'surname': 'Петрова'},
    {'name': 'Елизавета', 'surname': 'Белоброва'},
    {'name': 'Анастасия', 'surname': 'Курова'},
    {'name': 'Полина', 'surname': 'Тутова'},
    {'name': 'Артур', 'surname': 'Заплатин'},
    {'name': 'Даниил', 'surname': 'Совин'},
    {'name': 'Артур', 'surname': 'Пирожков'}]

remaining_students = []


def get_contours_topology(image):
    """
    Принимает в качестве параметра цветное изображение в формате RGB и возвращает:
     - список обнаруженных контуров
     - их топология (дерево включений)
     - изображение в серых оттенках
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 1000)
    ced_image = cv2.Canny(blurred, 50, 180)
    cv2.imshow('canny', ced_image)
    contours, hierarchy = cv2.findContours(ced_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours, hierarchy, gray


def edging(contour):
    """
    Принимает в качестве параметра массив точек и возвращает
    массив вершин прямоугольника, наилучшим образом обрамляющий контур.
    """
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    angle = rect[-1]
    if angle < -45:
        angle += 90
    elif angle > 45:
        angle -= 90

    if angle == 0:
        min_index = np.argmin(box[:, 0])
    elif angle == 90:
        min_index = np.argmin(box[:, 1])
    else:
        min_index = np.argmin(box[:, 0] + box[:, 1])
    box = np.roll(box, -min_index, axis=0)

    return [box]


def extract_identifier(im_gray, box, image_display, group=CLASS_TEST):
    """
     Принимает в качестве параметра изображение в оттенках серого
     и прямоугольник в виде массива вершин, который должен обрамлять карточку.
     Пишет на отображаемом изображении ответ ученика, который владеет карточкой.
     Возвращает целое число, идентифицирующее карточку.
    """
    str_code = ''
    tops = [tuple(top) for top in box[0]]
    x_min = min(tops, key=lambda t: t[0])[0]
    x_max = max(tops, key=lambda t: t[0])[0]
    y_min = min(tops, key=lambda t: t[1])[1]
    y_max = max(tops, key=lambda t: t[1])[1]
    if x_max > x_min and y_max > y_min:
        zone = im_gray[y_min:y_max, x_min:x_max]
        depart = np.float32(tuple(map(lambda t: (t[0] - x_min, t[1] - y_min), tops[:3])))
        purpose = np.float32(((0, 0), (200, 0), (200, 200)))
        mat = cv2.getAffineTransform(depart, purpose)

        straightened_area = cv2.warpAffine(zone, mat, (200, 200))
        contrasting_area = cv2.threshold(straightened_area, 80, 255, cv2.THRESH_BINARY)[1]
        difference = 5
        for j in range(5):
            for i in range(5):
                x_min = 40 * i + difference
                x_max = 40 * (i + 1) - difference
                y_min = 40 * j + difference
                y_max = 40 * (j + 1) - difference
                zone = contrasting_area[y_min:y_max, x_min:x_max]

                if cv2.mean(zone)[0] > 127:
                    str_code += '0'
                else:
                    str_code += '1'
                cv2.rectangle(contrasting_area, (40 * i + difference, difference + 40 * j), (40 * (i + 1) - difference, 40 * (j + 1) - difference), (255, 255, 255))
        int_ret = int(str_code, 2)
        anchor = tops[0]
        if CATALOGUE.get(int_ret):
            rang_stud = CATALOGUE.get(int_ret)[0] - 1
            if rang_stud < len(group):
                text = 'done'
                cv2.putText(image_display, text, anchor, cv2.FONT_HERSHEY_SIMPLEX, 3.0, (0, 0, 255), 8)
    else:
        int_ret = 0
    return int_ret


def extract_identifiers(image, group=CLASS_TEST):
    """
    извлекает ВСЕ обнаруженные карточки на изображении и возвращает список
    считанных идентификаторов.
    """
    res = []
    contours, hierarchy, im_gray = get_contours_topology(image)

    for rang, contour in enumerate(contours):
        topology = hierarchy[0][rang]
        if topology[0] == -1 and topology[1] == -1 and topology[2] == -1 and topology[3] != -1:
            rang_fat = topology[3]
            topology_fat = hierarchy[0][rang_fat]
            rang_grand_fat = topology_fat[3]
            if rang_grand_fat != -1:
                grand_fat = contours[rang_grand_fat]
                rectangle = edging(grand_fat)
                if cv2.contourArea(grand_fat) > 0:
                    try:
                        res.append(extract_identifier(im_gray, rectangle, image, group))
                    except:
                        pass
    return res


def recognizes_cards(image, group=CLASS_TEST):
    '''if stop_scan:
        return []'''
    return [CATALOGUE.get(identifier) for identifier in extract_identifiers(image, group) if
            CATALOGUE.get(identifier)]


def delete_missing_students(group):
    """
     Принимает в качестве параметра список учащихся в классе.
     Предлагает пользователю отметить отсутствующих в окне Tkinter.
     Возвращает список фактически присутствующих учеников.
    """
    global remaining_students

    window = Tk.Tk()
    window.title('Отсутствующие')
    for student in group:
        presence = Tk.IntVar()
        presence.set(1)
        student.update({'present': presence})
        button = Tk.Checkbutton(window, text=student['name'] + ' ' + student['surname'], onvalue=0, offvalue=1, variable=student['present'], justify=Tk.RIGHT)
        button.pack(anchor="w")

    def confirm_input():
        window.quit()
        window.destroy()

    button = Tk.Button(window, text="Подтвердить", command=confirm_input)
    button.pack()
    window.mainloop()
    remaining_students = [rem for rem in group if rem['present'].get()]
    for student in remaining_students:
        student.pop('present')


def displaying_remaining_students():
    """Отображает список оставшихся учеников в окне Tkinter"""
    global remaining_students
    displaying_remaining_students = Tk.Tk()
    displaying_remaining_students.title('Нераспознанные ученики')
    card_remaining_stud = Tk.Frame(displaying_remaining_students)

    for student in remaining_students:
        label = Tk.Label(card_remaining_stud, text=student['name'] + ' ' + student['surname'])
        label.pack()
    card_remaining_stud.pack()

    def updating_list(window=displaying_remaining_students):
        global remaining_students
        if not remaining_students:
            return
        cadre = window.winfo_children()[0]
        if len(cadre.children) > len(remaining_students):
            print('#####')
            print(str(len(cadre.children)) + ',' + str(len(remaining_students)))
        cadre.destroy()
        cadre = Tk.Frame(window)
        for student in remaining_students:
            text = f"{student['name']} {student['surname']}"
            label = Tk.Label(cadre, text=text)
            label.pack()
        cadre.pack()
        window.after(500, updating_list)
    displaying_remaining_students.after(500, updating_list)
    displaying_remaining_students.mainloop()


def scan_photo(group, name_photo):
    '''Сканирует карточки на фото'''
    global answers, input_field, label_entry_get
    answers = []
    #label_entry_get['text'] = f'{input_field.get()}'
    #name = str(str(name_photo) + ".jpg")
    frame = cv2.imread(name_photo, cv2.IMREAD_COLOR)
    #cv2.imshow('gfgfgg', frame)
    for identification, answer in recognizes_cards(frame, group):
        if identification <= len(group):
            answers.append((identification, answer))
    print('Сканирование завершено')
    print('Результаты:')
    for identification, answer in answers:
        print(f'Студент: {group[identification - 1]["name"]} {group[identification - 1]["surname"]}, Ответ: {answer}')
    print(answers)


def scan_video_stream(group, camera=0):
    """Сканирует видеопоток с камеры и распознает карточки,
        пока все ученики не будут распознаны"""
    global stop_scan
    stop_scan = False
    global remaining_students, answers
    answers = []
    cap = cv2.VideoCapture(camera, cv2.CAP_ANY)
    while remaining_students and not stop_scan:
        correct_reading, frame = cap.read()
        if correct_reading:
            cv2.imshow('catch', frame)
            for identification, answer in recognizes_cards(frame, group):
                if identification <= len(group) and group[identification - 1] in remaining_students:
                    answers.append((identification, answer))
                    rang_stud = remaining_students.index(group[identification - 1])
                    remaining_students.pop(rang_stud)
            cv2.imshow('catch', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            cap.release()
            cv2.destroyAllWindows()
        if not remaining_students:
            stop_scan = True
            cap.release()
            cv2.destroyAllWindows()
            print('Сканирование завершено')
            print('Результаты:')
            for identification, answer in answers:
                print(f'Студент: {group[identification - 1]["name"]} {group[identification - 1]["surname"]}, Ответ: {answer}')

    print(answers)


def real_time_scanner(group, camera=0, window=None):
    """Запускает сканирование видеопотока с камеры
        и отображает список оставшихся учеников в окне Tkinter"""
    if window:
        window.quit()
        window.destroy()
    delete_missing_students(group)
    t = threading.Thread(target=displaying_remaining_students)
    t.start()
    scan_video_stream(group, camera)


def select_card():
    global label_entry_get, input_field
    input_window = Tk.Tk()
    input_window.title("Введите название фото")
    input_text = Tk.StringVar()
    input_field = Tk.Entry(input_window, textvariable=input_text)
    input_field.pack()

    label_entry_get = Tk.Label(input_window)
    label_entry_get.pack()

    ok_button = Tk.Button(input_window, text="OK", command=(lambda: scan_photo(CLASS_TEST, input_field.get())))
    ok_button.pack()

    input_window.mainloop()


def select_class_video(group, window=None):
    """выбрать класс и запустить сканирование"""
    if window:
        window.quit()
        window.destroy()
    m_window = Tk.Tk()
    m_window.title("Выбор класса")
    button_group_1 = Tk.Button(m_window, text="1 класс", command=(lambda: real_time_scanner(group, 0, m_window)))
    button_group_1.pack()
    m_window.mainloop()


def select_class_photo():
    """выбрать класс и запустить сканирование"""
    select_card()


def main():
    main_window = Tk.Tk()
    main_window.title('Выбрать действие')
    text = Tk.Text(height=5, width= 30, font=('Arial 14', 18))
    text.pack()

    text.insert("1.0", "Выберите действие:")
    text.tag_add('title', 1.0)
    text.tag_config('title', justify='center')
    button_video = Tk.Button(main_window, text = 'Запустить сканирование с видеопотока', command=lambda: select_class_video(CLASS_TEST, main_window))
    button_photo = Tk.Button(main_window, text= 'Выбрать фото', command=lambda:select_class_photo())
    button_video.pack()
    button_photo.pack()
    main_window.mainloop()


if __name__ == '__main__':
    scan_photo(CLASS_TEST,"15_5.jpg")