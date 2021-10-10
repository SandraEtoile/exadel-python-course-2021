import unittest

from tasks.task08.shapes import Circle, Point2D, Rectangle, Square, Shape2DCollection


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle([1, 2], 5)
        area = circle.area
        self.assertEqual(area, 78.5, "Correct value is 78.5")

    def test_circle_contains_point(self):
        circle = Circle([1, 2], 5.0)
        point = Point2D(1.0, 3.0)
        self.assertTrue(circle.__contains__(point), "Correct value is True")

    def test_circle_contains_negative_point(self):
        circle = Circle([-1, 2], 5.0)
        point = Point2D(1.0, 1.0)
        self.assertTrue(circle.__contains__(point), "Correct value is True")

    def test_circle_contains_point_on_line(self):
        circle = Circle([1, 2], 5.0)
        point = Point2D(1.0, 7.0)
        self.assertTrue(circle.__contains__(point), "Correct value is True")

    def test_circle_not_contains_point(self):
        circle = Circle([1, 2], 5.0)
        point = Point2D(10.0, 7.0)
        self.assertFalse(circle.__contains__(point), "Correct value is False")

    def test_rectangle_area(self):
        rectangle = Rectangle([1, 2], 5, 10)
        area = rectangle.area
        self.assertEqual(area, 50, "Correct value is 50")

    def test_rectangle_contains_point(self):
        rectangle = Rectangle([1, 2], 5, 10)
        point = Point2D(2.0, 3.0)
        self.assertTrue(rectangle.__contains__(point), "Correct value is True")

    def test_rectangle_contains_negative_point(self):
        rectangle = Rectangle([-1, 2], 5, 10)
        point = Point2D(2.0, 3.0)
        self.assertTrue(rectangle.__contains__(point), "Correct value is True")

    def test_rectangle_contains_point_on_line(self):
        rectangle = Rectangle([1, 2], 5, 10)
        point = Point2D(1.0, 3.0)
        self.assertTrue(rectangle.__contains__(point), "Correct value is True")

    def test_rectangle_not_contains_point(self):
        rectangle = Rectangle([1, 2], 5, 10)
        point = Point2D(12.0, 8.0)
        self.assertFalse(rectangle.__contains__(point), "Correct value is False")

    def test_square_area(self):
        square = Square([1, 2], 5)
        area = square.area
        self.assertEqual(area, 25, "Correct value is 25")

    def test_square_contains_point(self):
        square = Square([1, 2], 5)
        point = Point2D(2.0, 3.0)
        self.assertTrue(square.__contains__(point), "Correct value is True")

    def test_square_contains_negative_point(self):
        square = Square([-1, 2], 5)
        point = Point2D(2.0, 3.0)
        self.assertTrue(square.__contains__(point), "Correct value is True")

    def test_square_contains_point_on_line(self):
        square = Square([1, 2], 5)
        point = Point2D(1.0, 3.0)
        self.assertTrue(square.__contains__(point), "Correct value is True")

    def test_square_not_contains_point(self):
        square = Square([1, 2], 5)
        point = Point2D(12.0, 8.0)
        self.assertFalse(square.__contains__(point), "Correct value is False")

    def test_shape2d_collection_area(self):
        square = Square([1, 2], 5)
        rectangle = Rectangle([1, 2], 5, 10)
        circle = Circle([1, 2], 5)
        shape_2d_collection = Shape2DCollection([square, rectangle, circle])
        self.assertEqual(shape_2d_collection.area, 153.5, "Correct value is 153.5")

    def test_shape2d_collection_contains_point(self):
        square = Square([10, 2], 5)
        rectangle = Rectangle([10, 2], 5, 10)
        circle = Circle([1, 2], 5)
        point = Point2D(1.0, 3.0)
        shape_2d_collection = Shape2DCollection([square, rectangle, circle])
        self.assertTrue(shape_2d_collection.__contains__(point))

    def test_shape2d_collection_not_contains_point(self):
        square = Square([10, 2], 5)
        rectangle = Rectangle([10, 2], 5, 10)
        circle = Circle([10, 2], 5)
        point = Point2D(1.0, 3.0)
        shape_2d_collection = Shape2DCollection([square, rectangle, circle])
        self.assertFalse(shape_2d_collection.__contains__(point))


if __name__ == '__main__':
    unittest.main()
