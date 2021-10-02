from unittest import TestCase, mock
from b import XYZ


class Test(TestCase):

    def test_b(self):
        mocked_a_class = mock.Mock()
        mocked_a_instance = mocked_a_class.return_value
        mocked_a_instance.my_method.return_value = 4
        with mock.patch("b.SomeClass", mocked_a_class):
            # mock_my_method.return_value = 4
            b_i = XYZ()
            x = b_i.new_fn()
            assert x == 4
