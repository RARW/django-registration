from django.test import TestCase

import registration

from registration.tests.backends import *
from registration.tests.forms import *
from registration.tests.models import *
from registration.tests.views import *


class RegistrationVersionInfoTests(TestCase):
    """
    Test django-registration's internal version-reporting
    infrastructure.
    
    """
    def setUp(self):
        self.version = registration.VERSION

    def tearDown(self):
        registration.VERSION = self.version
    
    def test_get_version(self):
        """
        Test the version-info reporting.
        
        """
        versions = [
            {'version': (1, 0, 0, 'alpha', 0),
             'expected': r'1\.0(\.dev\d+)?'},
            {'version': (1, 0, 1, 'alpha', 1),
             'expected': r'1\.0\.1a1'},
            {'version': (1, 1, 0, 'beta', 2),
             'expected': r'1.1b2'},
            {'version': (1, 2, 1, 'rc', 3),
             'expected': r'1.2.1c3'},
            {'version': (1, 3, 0, 'final', 0),
             'expected': r'1.3'},
            {'version': (1, 4, 1, 'beta', 0),
             'expected': r'1.4.1b'},
            ]
        
        for version_dict in versions:
            registration.VERSION = version_dict['version']
            self.assertRegexpMatches(registration.get_version(), version_dict['expected'])
