import unittest
from widget import Widget


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))


if __name__ == '__main__':
    unittest.main()
