import numpy as np
import cv2 as cv

from typing import List


class Point_in_Polygon:
    def __init__ (self, polyg: List[List[int]]):  # Для иницилизации класса нужно подать полигон в виде листа в котором лист в виде точки[[709.6, 390.2],[824.3, 28.1], [920.1, 393.4]]
        self.polyg = np.array([polyg], dtype=np.int32 )    # points 2d
        self.w,self.h = np.max(self.polyg[0], axis=0)  

        # 2chanel (2d) numpy image GrayScale
        self.__filled_polyg_2d = np.zeros((self.h,self.w),dtype=np.uint8)  # empty 2d image
        cv.fillPoly( self.__filled_polyg_2d, self.polyg, 1)  # matrix filled_polyg
        
        # 3chanel (3d) numpy image RGB colour FOR POLIITNG
        self.__filled_polyg_3d = np.zeros((self.h,self.w, 3),dtype=np.uint8)  # empty 2d image
        cv.fillPoly(self.__filled_polyg_3d, self.polyg, color=(255, 255, 255))
        
        self.__size_point= int((self.h+self.w)/300) or 1
        
    def point_in_polyg (self, point: List[int]) -> bool:  # Функция которая принимает точку выдает => True/False
        x,y = point
        x,y=int(x),int(y)
        if self.w<x or self.h<y:
            return False
        return bool(self.__filled_polyg_2d[y,x])
    
    def plot_point_in_polyg(self, point: List[int]) -> np.ndarray:
        in_polygon=self.point_in_polyg(point)
        
        filled_polyg_3d=np.copy(self.__filled_polyg_3d)
        point = (int(point[0]), int(point[1]))
        
        if in_polygon:
            cv.fillPoly(filled_polyg_3d, self.polyg, color=(0, 255, 0))
            filled_polyg_3d = cv.circle(filled_polyg_3d, point, radius=self.__size_point, color=(0, 0, 255), thickness=self.__size_point)
            return filled_polyg_3d
        else:
            filled_polyg_3d = cv.circle(filled_polyg_3d, point, radius=self.__size_point, color=(0, 0, 255), thickness=self.__size_point)
            return filled_polyg_3d

    
