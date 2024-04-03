# django-ecommerce-api
ecommerce api con django y django rest framework

# para desplegar
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# despliegue con docker
docker compose up -d
docker exec -it ecommerce.api python manage.py migrate
docker exec -it ecommerce.api python manage.py createsuperuser
docker exec -it ecommerce.api python manage.py collectstatic