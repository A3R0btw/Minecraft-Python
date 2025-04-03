# pip install ursina - установка библеотеки
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()  # Создаём основное приложение Ursina (окно игры)
player = FirstPersonController()  # Создаём персонажа с видом от первого лица и помещаем его в сцену
Sky()  # Добавляем небо в сцену


boxes = []  # Создаём пустой список для хранения всех кубов (блоков)

# Создаём сетку из кубов (20x20)
for i in range(20):  # Цикл по оси Z
  for j in range(20):  # Цикл по оси X
    # Создаём кнопку (Button - интерактивный куб)
    box = Button(
        color=color.white,  # Цвет куба (белый)
        model='cube',  # Форма куба
        position=(j, 0, i),  # Позиция куба в пространстве (X, Y, Z) - Y=0, чтобы кубы стояли на земле
        texture='трава.png',  # Текстура куба (изображение травы)
        parent=scene,  # Делаем сцену родителем куба (чтобы он отображался)
        origin_y=0.5  # Смещаем центр куба по оси Y (чтобы он стоял на земле правильно)
    )
    boxes.append(box)  # Добавляем созданный куб в список boxes

# Функция обработки ввода с клавиатуры и мыши
def input(key):  # Функция вызывается при каждом нажатии клавиши
  for box in boxes:  # Перебираем все кубы в списке
    if box.hovered:  # Если мышь наведена на куб
      if key == 'left mouse down':  # Если нажата левая кнопка мыши
        # Создаём новый куб рядом с выбранным
        new = Button(
            color=color.white,  # Цвет куба (белый)
            model='cube',  # Форма куба
            position=box.position + mouse.normal,  # Позиция нового куба: позиция текущего + нормаль мыши (направление от камеры к кубу)
            texture='трава.png',  # Текстура куба (изображение травы)
            parent=scene,  # Делаем сцену родителем куба
            origin_y=0.5  # Смещаем центр куба по оси Y
        )
        boxes.append(new)  # Добавляем новый куб в список
      if key == 'right mouse down':  # Если нажата правая кнопка мыши
        boxes.remove(box)  # Удаляем куб из списка
        destroy(box)  # Уничтожаем куб из сцены (удаляем из памяти)


app.run()
