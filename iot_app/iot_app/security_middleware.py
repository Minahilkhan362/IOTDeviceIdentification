from django.http import HttpResponse
from .services.device_verification_service import DeviceVerificationService
from .jwt_manager import JWTManager


class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self._jwt_manager = JWTManager()
        self.verification_service = DeviceVerificationService()

        self.bypass_routes = ['/api/account/login', '/api/account/signup']

    def __call__(self, request, *args, **kwargs):
        # Only public routes are passed without verification
        if request.path not in self.bypass_routes:
            # First checking required headers are available
            if 'Authorization' not in request.headers or 'Device' not in request.headers:
                return HttpResponse("You have no permission to access", status=401)

            # Then verifying JWT token validation
            token = self._jwt_manager.verify_token(
                request.headers['Authorization'])
            if token == None:
                return HttpResponse("You have no permission to access", status=401)

            # If pass, then device verification
            if self.verification_service.predict_device_name(request) != request.headers['Device']:
                return HttpResponse("You have no permission to access", status=401)

        return self.get_response(request)
