#!/usr/bin/env python   manage.py는 장고에게 명령어를 수헹하게 하는 파일이라서, 매우 중요하고, 건드리면 안된다.
# config에는 설정파일이 들어간 폴더이다. venv, config와 같이 명령어를 통해 만들어진 파일들의 이름을 임의로 수정하면 안된다.
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
