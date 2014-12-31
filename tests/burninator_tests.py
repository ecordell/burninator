from mock import *
from nose.tools import *

from burninator import Burninator

try:
    import builtins
    patch_string = 'builtins.print'
except ImportError:
    import __builtin__
    patch_string = '__builtin__.print'


class TestBurninator(object):

    def setup(self):
        self.burninator = Burninator()

    def test_burninate(self):
        with patch(patch_string) as mock_print:
            self.burninator.burninate()
            mock_print.assert_has_calls(
                [
                    call('Burninated!')
                ]
            )
