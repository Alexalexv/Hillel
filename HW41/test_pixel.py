from HW41.pixel_with_defects import Pixel
import pytest


@pytest.mark.parametrize("r, g, b, r_, g_, b_",
                         [(1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0), (255, 255, 255, 255, 255, 255)])
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
