from django.shortcuts import get_object_or_404, render

from django.views import View

class HomeView(View):
    """Homepage"""
    template_name = 'netbox_cloud/homepage.html'

    # service incoming GET HTTP requests
    def get(self, request):
        """Get request."""
        
        return render(
            request,
            self.template_name,
        )