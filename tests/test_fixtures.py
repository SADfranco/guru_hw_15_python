"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from pages.github_main import github_main

def test_github_desktop(desktop_version):
    github_main.open()
    github_main.desktop_sign_in()
    github_main.should_have_text_sign_in()


def test_github_mobile(mobile_version):
    github_main.open()
    github_main.mobile_sign_in()
    github_main.should_have_text_sign_in()