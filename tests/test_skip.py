"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser
from pages.github_main import github_main


def test_github_desktop(driver_setup):
    if browser.config.window_width < 1000:
        pytest.skip("Mobile test")
    github_main.open()
    github_main.desktop_sign_in()
    github_main.should_have_text_sign_in()


def test_github_mobile(driver_setup):
    if browser.config.window_width > 1000:
        pytest.skip("Desktop test")
    github_main.open()
    github_main.mobile_sign_in()
    github_main.should_have_text_sign_in()
