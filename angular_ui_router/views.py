from django.views.generic.base import View
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
class HomeView(View):
    def get(self,request):
        return render(request,"index.html")
    
def partials(request, folder, template=None ):
    
    l_template  = "%s/%s" %(folder, template)
    
    return render_to_response(
                                l_template, 
                                RequestContext(request, {})
                                )