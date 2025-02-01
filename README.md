# FAQ API

## Installation
```bash
git clone <repo-url>
cd faq_project
docker-compose up --build
```

## API Usage
```bash
curl http://localhost:8000/api/faqs/
curl http://localhost:8000/api/faqs/?lang=hi
```

## Running Tests
```bash
python manage.py test
```
