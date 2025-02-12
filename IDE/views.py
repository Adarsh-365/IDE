from django.http import JsonResponse,HttpResponse
import pickle
from django.shortcuts import render
from .forms import PYTHON_IDE
from .compiler import Compiler
from .utility import list_files_and_folders


def run_code(request,save):
   
        code = request.POST.get("code", "")
        if code:
            if save:
                with open("static/newfile.py","w") as f:
                    temp = code.split("\n")
                    f.writelines(temp)
            Com = Compiler(code)
            Com.run()
            output = Com.output()
        return JsonResponse({'output': output})

def home_page(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return run_code(request,True)
    
    
    with open("static/newfile.py","r") as f:
        data = f.readlines()
    data = "".join(data)
   
    df ={"data":data}
    
  
    
    return render(request, "index.html",df)


def dyanmic_route(request,problemid):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return run_code(request,False)
  
    with open("data.pickle",'rb') as f:
        pik= pickle.load(f)
    data = pik[str(problemid)]
    df ={"data":data}
    return render(request, "index.html",df)