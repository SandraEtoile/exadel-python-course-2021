from typing import NamedTuple
import abc
import math


class Point2D(NamedTuple):
    x: float
    y: float

    def __str__(self):
        return f"({self.x}, {self.y})"


class Shape2D(abc.ABC):
    @property
    @abc.abstractmethod
    def area(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def __contains__(self, point: Point2D) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class Rectangle(Shape2D):
    def __init__(self, bottom_left: list, width, length):
        self.bottom_left = bottom_left
        self.width = width
        self.length = length

    @property
    def area(self) -> float:
        return self.width * self.length

    def calculate_top_right_coordinates(self):
        return self.bottom_left[0] + self.length, self.bottom_left[1] + self.width

    def __contains__(self, point: Point2D) -> bool:
        top_right = self.calculate_top_right_coordinates()
        if self.bottom_left[0] <= point.x <= top_right[0] and self.bottom_left[1] <= point.y <= top_right[1]:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"({self.bottom_left}, {self.width}, {self.length})"


class Square(Rectangle):
    def __init__(self, bottom_left: list, side_size):
        super().__init__(bottom_left, side_size, side_size)


class Circle(Shape2D):
    def __init__(self, center: list, radius):
        self.center = center
        self.radius = radius

    @property
    def area(self) -> float:
        return round(pow(self.radius, 2) * math.pi, 1)

    def __contains__(self, point: Point2D) -> bool:
        if (pow(point.x - self.center[0], 2) + pow(point.y - self.center[1], 2)) <= pow(self.radius, 2):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"({self.center}, {self.radius})"


class Shape2DCollection(Shape2D):
    def __init__(self, shapes: list):
        self.shapes = shapes

    @property
    def area(self) -> float:
        return sum(shape.area for shape in self.shapes)

    def __contains__(self, point: Point2D) -> bool:
        for shape in self.shapes:
            if shape.__contains__(point):
                return True
            else:
                continue
        return False

    def __str__(self) -> str:
        return f"({self.shapes})"
