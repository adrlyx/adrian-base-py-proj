# About:

## Folder structure

```
.
├── LICENSE
├── MANIFEST.in
├── README.md
├── app
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py
│   ├── files
│   │   └── random.txt
│   ├── mod_a
│   │   ├── __init__.py
│   │   └── mod_a.py
│   └── mod_b
│       ├── __init__.py
│       └── mod_b.py
├── scripts
│   └── my-app-runner.py
└── setup.py
```

## Before you begin:

Rename files and folders:

    Change folder name: 
        adrian-base-py-proj > rename folder

    Change name of executable: 
        In setup.py change:
            "console_scripts": ['my-app = app.app:main'] > change "my-app"

    Change name of app:
        name = "cmdline-my-app", > change "cmdline-my-app"

Start coding in app/*

## Installation:

### To install in the root folder:

``
python3 setup.py install
``

To install on your system:

``
pip install .
``

## Be Aware

Project will automatically include .txt files from 'app/files/'.
This behaviour is configured in MANIFEST.in and can be edited from there.

## Development

Test code as a user:

``
python3 scripts/my-app-runner.py
``


For development:

``
pip install -e .
``