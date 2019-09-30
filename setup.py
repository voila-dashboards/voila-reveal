from setuptools import setup
import os

data_files = []
for root, dirs, files in os.walk('share'):
    root_files = [os.path.join(root, i) for i in files]
    data_files.append((root, root_files))

setup_args = {
    'name': 'voila-reveal',
    'version': '0.0.2',
    'packages': [],
    'data_files': data_files,
    'install_requires': [
        'voila>=0.1.15,<0.2'
    ],
    'author': 'Voila Development team',
    'author_email': 'jupyter@googlegroups.com',
    'url': 'https://github.com/voila-dashboards/voila-reveal/'
}

if __name__ == '__main__':
    setup(**setup_args)
