from django.http import JsonResponse,HttpResponse
import pickle
from django.shortcuts import render
from .forms import PYTHON_IDE
from .compiler import Compiler
from .utility import list_files_and_folders
from django.contrib.staticfiles.storage import staticfiles_storage
import os


def run_code(request,save):
   
        code = request.POST.get("code", "")
        if code:
            pik = {}
            if os.path.exists("data.pickle") and os.path.getsize("data.pickle") > 0:
                with open("data.pickle", 'rb') as f2:
                    pik = pickle.load(f2)
            problemid = str(request.session.get('problemid', '1'))
            print(problemid)
            pik[problemid] = code
            with open("data.pickle", 'wb') as f:
                pickle.dump(pik, f)

            Com = Compiler(code)
            Com.run()
            output = Com.output()
        return JsonResponse({'output': output})

# def run_code(request,save):
   
#         code = request.POST.get("code", "")
#         if code:
#             if save:
#                 file_path = staticfiles_storage.path('newfile.py')
#                 with open(file_path,"w") as f:
#                     temp = code.split("\n")
#                     f.writelines(temp)
#             Com = Compiler(code)
#             Com.run()
#             output = Com.output()
#         return JsonResponse({'output': output})

# def home_page(request):
#     if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
#         return run_code(request,True)
    
#     file_path = staticfiles_storage.path('newfile.py')
#     with open(file_path,"r") as f:
#         data = f.readlines()
#     data = "".join(data)
   
#     df ={"data":data}
    
  
    
#     return render(request, "index.html",df)

def home(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return run_code(request,False)
  
    return render(request, "index.html")

def dyanmic_route(request,problemid=1):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return run_code(request,False)
  
    with open("data.pickle",'rb') as f:
        pik= pickle.load(f)
    data = pik[str(problemid)]
    df ={"data":data}
    return render(request, "index.html",df)

def dyanmic_route2(request,problemid=1):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return run_code(request,False)
    request.session['problemid'] = problemid
    with open("data.pickle",'rb') as f:
        pik= pickle.load(f)
    if str(problemid) not in pik:
        pik[str(problemid)] = "# Not used Write your code here\n"
        
    
    data = pik[str(problemid)]
    df ={"data":data}
    return render(request, "index.html",df)