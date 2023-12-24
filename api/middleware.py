


class ShopMiddleware:
    
 
    def __init__(self, get_response=None):
        if get_response is not None:
            self.get_response = get_response
            
            
            
    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        
        return response
    
    
    def process_request(self, request):
        request.x = '0'
        