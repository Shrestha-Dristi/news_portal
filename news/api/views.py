from django.http import JsonResponse

def news(request):
    return JsonResponse({
        "name":"testing",
        "testing":"test",
        "data":{
            "test":"hellp"
        }
    })