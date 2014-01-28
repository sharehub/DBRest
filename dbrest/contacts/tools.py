import json
from django.http import HttpRequest

class ToolKits:
    """
    Toolkits functions
    """

    @staticmethod
    def coerce_put(request):
        """
        Hanlder the PUT data 
        """
        if request.method == "PUT":
            request.PUT = json.loads(request.body.replace("'", '"'))

