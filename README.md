# ClubHome
### A clubhouse clone as part of Django crash course by Yothin Muangsommuk (เขียนงูให้วัวกลัว)

## How to set up project
I'm encouraging using PyCharm to developing this project since it can managing the initial process to install the dependencies.

If you using PyCharm you can just import this project via `Import from VCS` and then PyCharm will create virtualenv and install 3rd party library we defined in requirements.txt

If you using other editor you can follow below step to setting up this project

1. Clone this project or download from GitHub
   ```
   git clone git@github.com:yothinix/clubhome-django.git
   ```
2. Create virtualenv for the project
    ```
    python -m venv venv
    ```
3. Activate the virtualenv
   ```
   # For Windows
   .\venv\Scripts\Activate.bat
   
   # For Mac / Linux
   ./venv/bin/activate
   ```
4. Install all dependencies via pip
   ```
   pip install -r requirements.txt
   ```
5. Migrate the initial database
   ```
   cd clubhome
   python manage.py migrate
   ```
6. Start development server
   ```
   python manage.py runserver
   ```
   
## Additional link
* [GitHub: gatukgl / hello-clubhouse](https://github.com/gatukgl/hello-clubhouse)
* [Yothin Muangsommuk - Don't reinvent the wheel with Django generic - PySomTum #1](https://www.youtube.com/watch?v=6S0P9DMZYRQ)
* [GitHub: yothinix / pysomtum-generic-demo example code](https://github.com/yothinix/pysomtum-generic-demo)
* [Obey the Testing Goat! - Test-Driven Web Development with Python](https://www.obeythetestinggoat.com/pages/book.html#toc)
* [How to start production ready Django project from scratch](https://www.notion.so/yothinix/How-to-start-production-ready-Django-project-from-scratch-47202c49ef6f47bc88b75e82f3dc9fed)
