from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiaryModelForm
from info.models import Diary
from django.core.paginator import Paginator
from info.forms import DiaryModelForm

# Create your views here.
def info(request):
        diary_list = Diary.objects.all().order_by('-created_at')
        paginator = Paginator(diary_list, 5) 
        page = request.GET.get('page')
        info = paginator.get_page(page) 
        return render(request, "resume.html", {"info": info})

# def create(request):
#     if request.method == 'POST':
#         form = TeamModelForm(request.POST)  
#         if form.is_valid():  
#             form.save() 
#             return redirect('info')  
#     else:
#         form = TeamModelForm()  
#     return render(request, 'form_create.html', {'form': form})



def home(request):
    return render(request, "index.html")

# def create(request):
#     if request.method == 'POST':
#         form = DiaryModelForm(request.POST)  # 입력된 데이터를 form에 저장
#         if form.is_valid():  # 폼이 유효한지 검사
#             form.save()  # DB에 저장
#             return redirect('home')  # 홈으로 리다이렉트
#     else:
#         form = DiaryModelForm()  # GET 요청일 경우 빈 폼을 전달
#     return render(request, 'diary_create.html', {'form': form})


def diary_create(request): # 이름은 다르게!
    if request.method == 'POST':
        form = DiaryModelForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = request.user      
            diary.save()                  
            return redirect('info')
    else:
        form = DiaryModelForm()
    return render(request, 'diary_create.html', {'form': form})


def diary_list(request):
    diaries = Diary.objects.all().order_by('-created_at')
    return render(request, "diary_list.html", {"diaries" : diaries})


def diary_update(request, id):
    diary = get_object_or_404(Diary, pk=id)
    if request.method == 'POST':
        form = DiaryModelForm(request.POST, request.FILES, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
        form = DiaryModelForm(instance=diary)
    return render(request, 'diary_create.html', {'form': form})

def diary_delete(request, id):
    diary = get_object_or_404(Diary, pk=id)
    diary.delete()
    return redirect('info')

def diary_detail(request, id):
    diary = get_object_or_404(Diary, pk=id) 
    return render(request, "diary_detail.html", {"diary": diary})