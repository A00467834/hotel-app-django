from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializers
from .models import Hotels


@api_view(['GET', 'POST'])
def Hotels_list(request):
    if request.method == 'GET':
        hotels_list = Hotels.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(hotelSerializer.data)
    if request.method == 'POST':
        hotel_request = request.data
        serialize_request_data = HotelSerializers(data=hotel_request)
        if serialize_request_data.is_valid():
            serialize_request_data.save()

        return Response({"Message": "Added Successfully"})
