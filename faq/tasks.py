from celery import shared_task
from googletrans import Translator
from .models import FAQ

@shared_task
def translate_text(faq_id, question):
    translator = Translator()
    faq = FAQ.objects.get(id=faq_id)
    faq.question_hi = translator.translate(question, dest='hi').text
    faq.question_bn = translator.translate(question, dest='bn').text
    faq.save()
