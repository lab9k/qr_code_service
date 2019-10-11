# QR code service

## Prerequisites
 * Python 3.6 / Python 3.7
 * pip
 
## installation

```bash
pip install -r requirements.txt
```

## Run production server

```bash
export DJANGO_SETTINGS_MODULE="qr_service.settings.production"
export SECRET_KEY="s3cR3T_k3y"
export DEBUG=0
python manage.py runserver 8000
```


## deploy with docker

### create env file
```bash
cp .env.example .env
```

#### build

```bash
docker-compose build
```

#### run
```bash
docker-compose up
```

* Your server is now available at localhost:1337

You can configure the used port in docker-compose.yml in services.nginx.ports