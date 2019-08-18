from rest_framework import views
from rest_framework.response import Response

from .serializers import YourSerializer
from receiptbot.receipt_crawler import *


class YourView(views.APIView):

    def get(self, request):
        current_page = get_web_page(etax_url)

        yourdata = []
        if current_page:
            a_tags = get_hrefs(current_page)
            months = get_months(a_tags)
            for month in months:
                yourdata.append({'month': month})

        results = YourSerializer(yourdata, many=True).data
        return Response(results)
