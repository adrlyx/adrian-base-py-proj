About
========================

In the root folder run:

To install in the root folder:

python3 setup.py install

To install on your system:

pip install .

Before you begin:

Rename files and folders:

    Change folder name: 
        adrian-base-py-proj > rename folder

    Change name of executable: 
        In setup.py change:
            "console_scripts": ['my-app = app.app:main'] > change "my-app"

    Change name of app:
        name = "cmdline-my-app", > change "cmdline-my-app"

Start coding in app/app.py


For development:

pip install -e .