from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.manage_deals import handle_request, get_contact, create_deal, set_userfields


@api_view(['POST'])
def add_deal(request):
	response = handle_request(request.data)
	return Response(response)

