from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Student
from .form import StudentForm

# Create your views here.
class IndexView(View):
    template_name = "index.html"
    def get_context(self):
        students = Student.objects.all()
        context = {"students" : students,}
        return context
    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({"form":form})
        raise Exception("hhh")
        response = render(request, self.template_name,context=context)
        return response
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data["name"]
            student.sex = cleaned_data["sex"]
            student.email = cleaned_data["email"]
            student.profession = cleaned_data["profession"]
            student.qq = cleaned_data["qq"]
            student.phone = cleaned_data["phone"]
            student.save()
            return HttpResponseRedirect(reverse("index"))
        context = self.get_context()
        context.update({"form":form})
        return render(request,self.template_name, context=context)
class PrettyView(IndexView):
    template_name = "pretty.html"
# def index(request):
#     students = Student.get_all()
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("index"))
#     else:
#         form = StudentForm()
#     context = {"students" : students, "form" : form}
#     # words = "Words"
#     return render(request, 'index.html', context = context)