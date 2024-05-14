"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

import pytest
from pages.github_main import github_main


@pytest.mark.parametrize("driver", ["desktop"], indirect=True)
def test_github_desktop(driver):
    github_main.open()
    github_main.desktop_sign_in()
    github_main.should_have_text_sign_in()


@pytest.mark.parametrize("driver", ["mobile"], indirect=True)
def test_github_mobile(driver):
    github_main.open()
    github_main.mobile_sign_in()
    github_main.should_have_text_sign_in()
