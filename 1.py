python3 -m venv myenv
source myenv/bin/activate
pip install -r /path/to/requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py runserver

   pip install gunicorn
   gunicorn <todo_list>.wsgi:application

server {
       listen 80;
       server_name example.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }

   ln -s /etc/nginx/sites-available/myproject.conf /etc/nginx/sites-enabled/
   service nginx restart