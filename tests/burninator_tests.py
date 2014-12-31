from mock import *
from nose.tools import *

from burninator import Burninator


class TestBurninator(object):

    def setup(self):
        self.burninator = Burninator()

    def test_burninate(self):
        with patch('__builtin__.print') as mock_print:
            self.burninator.burninate()
            mock_print.assert_has_calls(
                [
                    call('Burninated!')
                ]
            )
