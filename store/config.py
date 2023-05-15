from dotenv import load_dotenv
import os

load_dotenv()

# DB 
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_NAME=os.environ.get("DB_NAME")
GENDER_CHOICES = (
('M', 'Мужчина'),
('F', 'Женщина'),
('O', 'Другое')
)


