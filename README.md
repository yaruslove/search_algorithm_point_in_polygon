## Check point in polygon

![](./img_show.jpg)
Алгоритм опреледеления точки в полигоне построен на базе библиотек **"Numpy"** и **"OpenCV"**  

Полигоны и Точки Должны быть с **положительными координатами!!!**


## Как работает?
Для запуска скрипта необходимо иницилизировать класс и подать туда полигон  
```
polyg = List[List[int,int]]

polyg =  [[1150,  419],
            [1115,  353],
            [1005,  289],
            [ 836,  301],
            [ 729,  343],
            ........    ,
            [1126,  262],
            [1200,  395],
            [1215,  576]]
```
Инизилизируем и проверяем точку
```
checker = Point_in_Polygon(polyg)

point = [1199.1, 510.2]
answer = checker.point_in_polyg(point) # -> bool
```

## Функция отрисовки
```
checker = Point_in_Polygon(polyg)

point = [1199.1, 510.2]
img_np = checker.plot_point_in_polyg(point) # -> np.ndarray.
```

## Сохранить картинку в файл
```
filename= "./img.jpg"
cv2.imwrite(filename, img_np)
```


