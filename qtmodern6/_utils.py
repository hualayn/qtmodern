import sys
from os.path import join, dirname, abspath
import PySide6
import platform

QT_VERSION = tuple(int(v) for v in PySide6.__version__.split('.'))
""" tuple: Qt version. """

PLATFORM = platform.system()


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, dirname(abspath(__file__)), relative_path)
    return join(dirname(abspath(__file__)), relative_path)
