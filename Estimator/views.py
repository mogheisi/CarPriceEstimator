from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CarSerializer
from .ScraperApp import Scraper
from .EstimatorApp import Estimator as EstimatorFunc


@api_view(['GET'])
def index(request):
    return Response({'message': 'Hello, world!'})


class Estimator(APIView):
    serializer_class = CarSerializer

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            brand = serializer.data.get('brand')
            name = serializer.data.get('name')
            model = serializer.data.get('model')
            kilometer = serializer.data.get('kilometer')
            accuracy = serializer.data.get('accuracy')

            Scraper(brand, name, model, kilometer, int(accuracy))
            price = EstimatorFunc(brand, name, model, kilometer)

            return Response(f'قیمت تخمینی خودروی شما :{price.answer[0]}')
        return Response(serializer.errors)

