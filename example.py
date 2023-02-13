import numpy as np
import cv2 as cv

from typing import List
import json

from Point_in_Polygon import Point_in_Polygon

#---- Загружаем данные ----#
pth_data="./data_polygs_points.json"
with open(pth_data, 'r') as jsn_file:
    list_polygs = json.load(jsn_file)
list_polygs=list_polygs["data"]
# print(list_polygs)
polyg_obj=list_polygs[2]


## Иницилизируем класс подаем туда полигон
polyg=polyg_obj['polygon']
polyg_checkr=Point_in_Polygon(polyg)

## Подаем точку
point=polyg_obj["point_out"][0]
answer=polyg_checkr.point_in_polyg(point) # -> bool
print(f"Point in polygon: {answer}")

# Сохраним картинку с данной точкой
point=polyg_obj["point_out"][0]
img_poly=polyg_checkr.plot_point_in_polyg(point)
filename= "./img_out.jpg"
cv.imwrite(filename, img_poly)