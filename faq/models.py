from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from .tasks import translate_text  # Lazy import to avoid circular import
        translate_text.delay(self.id, self.question)

    def get_translated_question(self, lang):
        cache_key = f'faq_{self.id}_{lang}'
        translated_text = cache.get(cache_key)
        if not translated_text:
            if lang == 'hi' and self.question_hi:
                translated_text = self.question_hi
            elif lang == 'bn' and self.question_bn:
                translated_text = self.question_bn
            else:
                return "Translation not available."
            cache.set(cache_key, translated_text, timeout=86400)
        return translated_text
