from rest_framework import generics
from faq.models import FAQ
from faq.serializers import FAQSerializer
from faq.tasks import translate_text

class FAQListView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def perform_create(self, serializer):
        faq = serializer.save()
        translate_text.delay(faq.id)  # Asynchronously trigger translation after save