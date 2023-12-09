from assertpy import assert_that

import dtrade.about as about

class TestAbout:
    def test_about(self):
        assert_that(about.package).is_equal_to('dtrade')