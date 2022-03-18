# Django

![django](https://user-images.githubusercontent.com/21663254/155492556-bf75541c-1668-4629-85c2-8dff27e7d9be.png)

## Django 簡介

Django是一個由Python寫成的Web應用框架。採用MTV(model-template-views)的設計模式，即為`模型(Model)`、`視圖(views)`、`模板(templates)`。

## 開發前環境設定

### 安裝 Python3

* Ubuntu 20.04

  ```Bash
  python3 -V
  Python 3.8.10
  ```

  如果python3並未存在，可以使用pip3安裝在bash終端：

  ```Bash
  sudo apt install python3
  ```

* Windows 10

  可以從[Python.org](https://www.python.org/)安裝它。

  ```PowerShell
  python -V
  Python 3.8.10
  ```

### 虛擬環境(virtualenv)

虛擬環境能讓專案擁有自己的套件，可以有效地分開各個專案間的套件避免搞混，也能讓他人開發時，能與自己的開發環境保持一樣，避免需多開發環境上套件版本不一致的問題。

建立一個文件夾用於存放Django的所有文件，在該文件夾的路徑下先建立一個虛擬環境。

#### 安裝虛擬環境

```PowerShell
pip install virtualenv
```

#### 使用虛擬環境

將Terminal導向欲創立專案的文件夾路徑，並輸入：

```python
# virtualenv <env_name>
virtualenv .env
```

輸入完指令後，在該路徑下會新增一個新的文件夾，裡面就是虛擬環境。

`注意`: 在不同OS下建立的虛擬環境是無法共用的。

#### 進入虛擬環境

* Ubuntu 20.04

  ```Bash
  source ./.env/bin/activate
  ```

* Windows 10

  ```PowerShell
  ./.env/Scripts/activate
  ```

### 安裝Django

進入虛擬環境後，就可以安裝Django

```Markdown
pip install django
```

### 建立Django專案

```python
# django-admin startproject <project-name>
django-admin startproject django_basic
cd django_basic
```

使用**manage.py**的`runserver`命令來啟動伺服器。

```Markdown
python3 manage.py runserver
```

訪問 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 即可看到成功的網頁。

### 專案文件介紹

使用`django-admin`創建後的文件夾結構

```text
django_basic/
    manage.py
    django_basic/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

* `__init__.py` 是一個空白的文件，告訴python將此目錄視為python套件。
* `settings.py` 包含所有網站的設定，可以註冊所有應用的地方，與靜態文件、DataBase的相關配置。
* `urls.py` 定義所有網站的url。
* `wsgi.py` Django應用與網路服務器的通訊。
* `manage.py` 創建應用、與Database通訊、啟動開發用的網路服務器。

## 應用(Application)

### 創建一個應用(Application)

由專案來控制各個App來達到各司其職的工作。

```python
# python manage.py startapp <app_name>
python manage.py startapp blog
```

執行完這行指令，會在該目錄下新建一個文件夾，該文件夾結構為:

```text
django_basic/
    manage.py
    django_basic/
    blog/
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        __init__.py
        migrations/
```

* `migrations` 一旦你修改了數據模型，這個文件會自動升級你的資料庫。

其他的文件會在後面一一的使用。

### 註冊Application

此時專案還並不能使用這個App，所以我們必須在專案註冊它。

所有的專案設定都在`django_basic/settings.py`這個文件裡，在`INSTALLED_APPS`裡新增剛剛所創建的`blog`app。

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', 
]
```

`補充`: `settings.py`有需多設定可以更改，如資料庫、時區、DEBUG模式...等等。

這裡已更改時區為做示範：

  ```python
  TIME_ZONE = 'Asia/Taipei'
  ```

## URL

與上面的`settings.py`一樣，在創立專案的同時就有`urls.py`這個文件，雖然這個文件管理所有的url，但是考慮在往後出現多個app，而每個app都有自己的urls，這就會造成很難管理，所以更傾向讓app管理自己的urls。

首先，先更改專案文件夾裡的`urls.py`：

```python
#urls
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',include('blog.urls')),
]
```

當使用者對Django發送URL請求，Django會把該app的urls都跑一遍(urlpatterns)，如果與發送的url相同，則會呼叫該url設定views來進行下一步。

之後在`blog`app文件夾裡建立一個新的文件`urls.py`

```python
# blog.urls
from django.urls import path

urlpatterns = [
    # 裡面是放app urls的地方
]
```

## Models

現在的網頁已經不像以前只單純的顯示內容，為了能讓使用者產出的資料儲存於資料庫中，模組能定義這些資料的格式，與資料庫溝通進而保存。

### Database設定

到`django_basic/settings.py`，

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

預設是使用`sqlite3`，也可以更改自己想要的資料庫，

* 'django.db.backends.postgresql'
* 'django.db.backends.mysql'
* 'django.db.backends.sqlite3'
* 'django.db.backends.oracle'

當然也可以使用其他的資料庫。

### 在資料庫建立Tables

```bash
python manage.py migrate
```

使用上面指令能在資料庫裡建立對應我們模型的Tables，`migrate`會根據`INSTALLED_APPS`來做依據新增Tables，這也是為什麼剛剛需要註冊App，並讓專案認識它。

這個指令也會在我們往後更改模型時用到。

### Models設計

進到`blog/models.py`，

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
```

建立完成後並輸入下面指令，

```bash
python manage.py makemigrations
```

並會出現新增成功訊息

```bash
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post
```

並把新的變更搬到資料庫裡

```bash
python manage.py migrate
```

如果要看到更詳細的資料庫運作，可以使用

```bash
# python manage.py sqlmigrate <app_name> <migration_number>
python manage.py sqlmigrate blog 0001
```

## Django Admin

完成了上面步驟，那要如何新增資料進資料庫裡，最簡單的方法就是使用`Django Admin`，但在使用前必須要有一個帳號密碼吧，不然這樣連路人都可以隨意更改我們的資料，一步一步開始。

### 建立一個 admin user

```python
python manage.py createsuperuser
```

之後便照著各個欄位輸入並建立一個`admin user`。

### 使用 Django Admin

開啟伺服器便能開始使用，

```bash
python manage.py runserver
```

進入[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)，會看到一個登入畫面，這個就是讓你登入你的`admin user`。

當登入進去後，你不會看到你所建立的`models`在上面，因為此時還需要一個步驟。

到`blog/admin.py`並更新

```python
from django.contrib import admin

from .models import Post

# Register your models here.
admin.site.register(Post)
```

此時再把網頁更新，就能看到剛剛新增的`blog`在上面了。

## Views & Templates

Python函數會`獲得request`與`回傳response`，response可能會是HTML、Error、文字或是圖片等等...，視圖就是回傳這些內容的地方。

### 簡單的Views

先在views裡新增

```python
# blog.views
from django.shortcuts import render, HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse('<h1>Index</h1>')
```

views改完後，這時候就要用`URL`來呼叫它

```python
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index_view, name='index'),
]
```

* `app_name`: app有名字後，當專案有一個以上的app，如果兩個app都有相同的`URL`，這個時候`app_name`就可以分別。

進入[http://127.0.0.1:8000/](http://127.0.0.1:8000/admin/)，就會看到結果。

### Templates

使用Templates之前，需要先建立一個文件夾名為`templates`，在文件夾下面再放一個與app同名的文件夾

```text
django_basic/
    manage.py
    django_basic/
    blog/
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        __init__.py
        migrations/
        templates/
          blog/
```

這個同名文件夾是放該app的html文件，在這裡先新增一個文件名為`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Index</title>
</head>
<body>
  <h1>The Index</h1>
</body>
</html>
```

之後再更改views，讓它回傳`index.html`

```python
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'blog/index.html', {})
```

進入[http://127.0.0.1:8000/](http://127.0.0.1:8000/admin/)，就會看到結果。

## URLconf

現階段的URL都是只回傳特定的`views`，如果今天要進入部落格的各個文章裡，就要設定URLconf

```python
# blog.urls
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail')
]
```

獲取所設定的格式獲得相對應得值，此功能為`Path converters`，以下是該轉換器所支援的型別：

* str
* int
* slug
* uuid
* path

`注意`：到`Django admin`裡面建立一個以上的`post`來做測試，

### views.py

對`views.py`做更改與新增

```python
# blog.views
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index_view(request):
    post_list = Post.objects.order_by('-pub_date')
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html', {'post': post})
```

* `index_view`：把資料庫裡相應的資料提出來，並且依據發布日期來排序(order_by)，再把資料傳給`index.html`使用。

* `post_detail_view`：與`index_view`雷同，不過它可以獲得該url轉換器所轉換的值，這邊會依據輸入值的不同，會回傳不同的結果。

* `get_object_or_404`當從資料庫回傳的資料是空的，則會把頁面導到404(Debug=False)。

### Templates.py

接下來我們要新增`post.html`與更改`index.html`文件。

* 修改`index.html`

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>
  </head>
  <body>
    <h1>The Index</h1>
    {% if post_list %}
      {% for post in post_list %}
      <div class="post">
        <h2><a href="{% url 'blog:post_detail' post.id %}">{{ post.headline }}</a></h2>
        <p>time: {{ post.pub_date }}</p>
      </div>
      {% endfor %}
    {% else %}
      <h2>No Post</h2>
    {% endif %}
  </body>
  </html>
  ```

  `{% url 'blog:post_detail' post.id %}`：使用`{% url %}`函數可以簡單的連結到各個url，`blog`為這個app的名字；`post_detail`是該url的名稱；`post.id`是各個post的id。

* 新增`post.html`

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Post</title>
  </head>
  <body>
    <h1>{{ post.headline }}</h1>
    <p>{{ post.pub_date }}</p>
    <p>{{ post.body }}</p>
  </body>
  </html>
  ```

上面帶有`{% %},{{ }}`為[Jinja2](https://jinja.palletsprojects.com/)網頁模板，非常方便能獲取views傳來的資料，也能運用在邏輯與for迴圈，甚至能重複運用以寫過的程式碼，十分的方便易學。

## Form

表格能讓使用者使用輸入資料的方式，來與網站做互動。這邊展示一個簡單的文章搜尋器，使用表格輸入該文章的標題，把與之有相同文字的標題顯示出來。

首先，先在App文件夾裡製作一個新的文件名為`form.py`(與`urls.py`相同)，再來就可以新增我們想要的表格格式

```python
# blog.form
from django import forms

class HeadlineSearch(forms.Form):
    post_headline = forms.CharField(required=False)
```

與models一樣，必須要先確定該格式。

新增好以後再來新增到`views.py`

```python
from django.shortcuts import render, get_object_or_404
from .models import Post
from .form import HeadlineSearch

# Create your views here.
def index_view(request):
    form = HeadlineSearch()
    post_list = Post.objects.order_by('-pub_date')

    if request.method == 'POST':
        form = HeadlineSearch(request.POST)

        if form.is_valid():
            headline = form.cleaned_data['post_headline']
            post_list = Post.objects.filter(headline__contains=headline)
            context = {'post_list': post_list, 'form': form}
            return render(request, 'blog/index.html', context)
    else:
        context = {'post_list': post_list, 'form': form}
        return render(request, 'blog/index.html', context)
    return render(request, 'blog/index.html', context)
```

首先先引入剛剛所建立的`form.py`文件的表格，`if request.method == 'POST':`當templates所request的狀態為`POST`，即為表格被提交，由`views`來驗證該表格輸入的資料是否有效，如果有效，即使用`filter`來篩選有相同文字的文章標題並且回傳。

`注意`：filter是硬性的搜尋，即為輸入的資料必須相同才會回傳，`__contains`就是告訴filter，只要有相同的字元就能回傳。

更改`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Index</title>
  </head>
  <body>
    <h1>The Index</h1>
    <form method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Search</button>
    </form>
    {% if post_list %}
      {% for post in post_list %}
      <div class="post">
        <h2><a href="{% url 'blog:post_detail' post.id %}">{{ post.headline }}</a></h2>
        <p>time: {{ post.pub_date }}</p>
      </div>
      {% endfor %}
    {% else %}
      <h2>No Post</h2>
    {% endif %}
  </body>
</html>
```

* `{% csrf_token %}`：CSRF 全名 Cross-Site Request Forgery，為跨站請求攻擊或跨站偽造請求，通常是在 Web 應用程式站外的其他頁面中，包括惡意程式碼或鏈結，當使用者已通過驗證且會話（Session）未過期時，瀏覽該頁面或點選該惡意鏈結，就會造成攻擊成功的可能性。

* `{{ form.as_p }}`：不只有`as_p`可以使用，目前有三種方式可以解析form

  * as_table
  * as_p
  * as_ul

## Static file

在預設情況下，管理Static files的參數已經寫入於`settings.py`

```python
INSTALLED_APPS = [
    #...
    'django.contrib.staticfiles',
]

# other configs
STATIC_URL = 'static/'
```

首先，在app裡加入`static`文件夾，並根據文件的種類分別(css,js,images...)

```text
django_basic/
    manage.py
    django_basic/
    blog/
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        __init__.py
        migrations/
        static/
          css/
            style.css
          images/
          js/
        templates/
          blog/
```

讓`templates`使用這些靜態文件

`index.html`

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- other code -->
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  <title>Index</title>
</head>
```

### 部屬時使用Static file

`django.contrib.staticfiles`只有在`DEBUG=True`時才會運行，這表示當網站部屬時(`DEBUG=Fals`)，`staticfiles`會失效，為解決這個問題，必須更改相關文件檔

首先，先在`settings.py`設定`STATIC_ROOT`、`STATICFILES_DIRS`

```python
import os

DEBUG = False # 部屬時，Debug為False
#...
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

* `STATICFILES_DIRS`: 可以把它看成Global的靜態文件，讓所有app都能使用
* `STATIC_ROOT`: collectstatic指令產生的路徑參考

設定`urls.py`

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

都完成後，在終端機輸入以下指令，並會在專案文件夾下產生一個`staticfiles`文件夾(根據`STATIC_ROOT`路徑產生)，他會將所有有註冊app的靜態文件夾，進行複製到該`staticfiles`

```python
python manage.py collectstatic
```

如果這時候運行伺服器，你會發現，靜態文件還是處於失效的狀態。原因是因為你還需要一個Web伺服器(`uWSGI`、`gunicorn`、`Nginx`...)。

這裡我們使用簡單的`whiteNoise`來當伺服器示範

`pip install whitenoise`

```python
setting.py
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #...
]
```

再次運行伺服器，就會看到靜態文件確實的套用了。
