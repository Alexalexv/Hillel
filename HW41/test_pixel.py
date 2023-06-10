from HW41.pixel_with_defects import Pixel
from HW41.modules import multiply, divide
import pytest


@pytest.mark.parametrize("r, g, b, r_, g_, b_",
                         [pytest.param(1, 1, 1, 1, 1, 1), pytest.param(0, 0, 0, 0, 0, 0),
                          pytest.param(255, 255, 255, 255, 255, 255),
                          pytest.param(1.1, 1.1, 1.1, 1, 1, 1,
                                       marks=pytest.mark.xfail(reason='float not converts to int'))])
def test_initialization_success(r, g, b, r_, g_, b_):
    pixel = Pixel(r, g, b)
    assert pixel.r == r_ and pixel.g == g_ and pixel.b == b_
    assert isinstance(pixel.r and pixel.g and pixel.b, int)


@pytest.mark.parametrize("r, g, b", [(256, 256, 256), (-1, -1, -1), (256, 255, 255), (255, 256, 255), (255, 255, 256),
                                     (-1, 1, 1), (1, -1, 1), (1, 1, -1)])
def test_initialization_value_error(r, g, b):
    with pytest.raises(ValueError) as exc_info:
        Pixel(r, g, b)
    assert str(exc_info.value) == f'One of the Pixel components ({r}, {g}, {b}) is not in range of [0, 255]'


@pytest.mark.parametrize("r, g, b, r_, g_, b_, r_res, g_res, b_res", [(1, 1, 1, 1, 1, 1, 2, 2, 2),
                                                                      (1, 1, 1, 255, 255, 255, 255, 255, 255),
                                                                      (255, 255, 255, 1, 1, 1, 255, 255, 255)])
def test_add_class(r, g, b, r_, g_, b_, r_res, g_res, b_res):
    pixel = Pixel(r, g, b)
    pixel_ = Pixel(r_, g_, b_)
    pixel_res = pixel_ + pixel
    assert pixel_res.r == r_res and pixel_res.g == g_res and pixel_res.b == b_res
    assert isinstance(pixel_res.r and pixel_res.g and pixel_res.b, int)


test_data = [pytest.param(1, 1, 1, 1, 1, 1, 0, 0, 0),
             pytest.param(1, 1, 1, 255, 255, 255, 0, 0, 0, marks=pytest.mark.xfail(reason='float returns'))]


@pytest.mark.parametrize("r, g, b, r_, g_, b_, r_res, g_res, b_res", test_data)
def test_sub_class(r, g, b, r_, g_, b_, r_res, g_res, b_res):
    pixel = Pixel(r, g, b)
    pixel_ = Pixel(r_, g_, b_)
    pixel_res = pixel - pixel_
    assert pixel_res.r == r_res and pixel_res.g == g_res and pixel_res.b == b_res
    assert isinstance(pixel_res.r and pixel_res.g and pixel_res.b, int)


test_data = [pytest.param(1, 2, 3, 4, 8, 12, 2),
             pytest.param(1, 2, 3, 0, 0, 0, 0.1, marks=pytest.mark.xfail(reason='float returns')),
             pytest.param(1, 2, 3, 255, 255, 255, 256)]


@pytest.mark.parametrize("r, g, b, r_res, g_res, b_res, multiplier", test_data)
def test_multiplier(r, g, b, r_res, g_res, b_res, multiplier):
    pixel = Pixel(r, g, b)
    pixel_res = pixel * multiplier
    pixel_res = multiplier * pixel_res
    assert pixel_res.r == r_res and pixel_res.g == g_res and pixel_res.b == b_res
    assert isinstance(pixel_res.r and pixel_res.g and pixel_res.b, int)


test_data = [pytest.param(12, 12, 12, 4, 4, 4, 3),
             pytest.param(12, 12, 12, 2, 2, 2, 5)]


@pytest.mark.parametrize("r, g, b, r_res, g_res, b_res, divider", test_data)
def test_division(r, g, b, r_res, g_res, b_res, divider):
    pixel = Pixel(r, g, b)
    pixel_res = pixel / divider
    assert pixel_res.r == r_res and pixel_res.g == g_res and pixel_res.b == b_res
    assert isinstance(pixel_res.r and pixel_res.g and pixel_res.b, int)


test_data = [pytest.param(Pixel(1, 1, 1), 'multiply', '10', id='multiply by string'),
             pytest.param(Pixel(2, 2, 2), 'divide', 'number', id='divide by string')]


@pytest.mark.parametrize("test_class, func_name, value", test_data)
def test_type_error_division_or_multiplication(test_class, func_name: str, value):
    func = globals()[func_name]
    with pytest.raises(Exception) as exc_info:
        func(test_class, value)
    assert str(exc_info.typename) == 'TypeError'


test_data = [pytest.param(Pixel(1, 1, 1), 'multiply', -1, id='multiply by -1'),
             pytest.param(Pixel(2, 2, 2), 'divide', -1, id='divide by -1',
                          marks=pytest.mark.xfail(reason='No exception in case of division by -1')),
             pytest.param(Pixel(3, 3, 3), 'multiply', 0, id='multiply by zero'),
             pytest.param(Pixel(3, 3, 3), 'divide', 0, id='division by zero',
                          marks=pytest.mark.xfail(reason='Unexpected exception'))]


@pytest.mark.parametrize("test_class, func_name, value", test_data)
def test_value_error_division_or_multiplication(test_class, func_name: str, value):
    func = globals()[func_name]
    with pytest.raises(Exception) as exc_info:
        func(test_class, value)
    assert str(exc_info.typename) == 'ValueError'


test_data = [pytest.param(Pixel(1, 1, 1), Pixel(1, 1, 1), True, id='expeced eval is true'),
             pytest.param(Pixel(1, 1, 1), Pixel(0, 0, 0), False, id='expeced eval is false')]


@pytest.mark.parametrize('pixel, pixel_, expected_eval ', test_data)
def test_evaluation_of_classes(pixel, pixel_, expected_eval):
    evaluation = pixel_ == pixel
    assert evaluation == expected_eval


def test_pixel_str():
    pixel = Pixel(14, 128, 236)
    expected = 'Pixel object\n\tRed: 14\n\tGreen: 128\n\tBlue: 236\n'
    assert pixel.__str__() == expected


def test_pixel_repr():
    pixel = Pixel(14, 128, 236)
    expected = 'Pixel(14, 128, 236)'
    assert pixel.__repr__() == expected


test_data = [
    pytest.param(1, 50, 200, 10, marks=pytest.mark.xfail(
        reason='method can set values out of range, float returns, wrong order of colors'))]


@pytest.mark.parametrize('r, g, b, area', test_data)
def test_get_pixel_near(r, g, b, area):
    pixel = Pixel(r, g, b)
    for i in range(10):
        pixel_ = pixel.get_pixel_near(area)
        assert [pixel_.r, pixel_.g, pixel_.b] == pytest.approx([r, g, b], abs=area)
        assert isinstance(pixel_.r and pixel_.g and pixel_.b, int)

