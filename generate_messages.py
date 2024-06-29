import os
from django.core.management import call_command

def clean_locale_files():
    locale_dir = os.path.join(os.getcwd(), 'locale')
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith('.po') or file.endswith('.pot'):
                os.remove(os.path.join(root, file))

def main():
    clean_locale_files()
    call_command('makemessages', locale='fr', ignore=['venv/*', 'env/*'], no_wrap=True)

if __name__ == "__main__":
    main()
