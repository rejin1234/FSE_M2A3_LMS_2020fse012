sudo ln -s /bin/sh /bin/sh^M
cd /root/
pip3 install -r requirements.txt
python manage.py makemigrations && python manage.py migrate
nohup python manage.py runserver 0.0.0.0:8000 &
