# Django Counter App Setup Guide - HTMX Version

A simple counter application using Django, DaisyUI (Cyberpunk theme), and HTMX.

## Prerequisites

- Python 3.8+ installed
- pip (Python package manager)
- Basic command line knowledge

## Step 1: Create Project Directory

```bash
mkdir django-counter-app
cd django-counter-app
git init .
```

## Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

## Step 3: Install Django

```bash
pip install django
```

## Step 4: Create Django Project

```bash
django-admin startproject counter_project .
git add .
git commit -m "Create Django project"
```

## Step 5: Create Django App

```bash
python manage.py startapp counter
git add .
git commit -m "Create Django app"
```

## Step 6: Configure Settings

Open `counter_project/settings.py` and add 'counter' to INSTALLED_APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'counter',  # Add this line
]
```

```bash
git add .
git commit -m "Add counter to django apps in settings"
```

## Step 7: Create Views

Create/edit `counter/views.py`:

```python
from django.shortcuts import render
from django.http import HttpResponse

counter_value = 0

def index(request):
    """Render the main counter page"""
    global counter_value
    return render(request, 'counter/index.html', {'counter': counter_value})

def increment(request):
    """Increment counter and return new value"""
    global counter_value
    counter_value += 1
    return HttpResponse(str(counter_value))

def decrement(request):
    """Decrement counter and return new value"""
    global counter_value
    counter_value -= 1
    return HttpResponse(str(counter_value))

def reset(request):
    """Reset counter to zero"""
    global counter_value
    counter_value = 0
    return HttpResponse(str(counter_value))
```

```bash
git add .
git commit -m "Create Django views"
```

## Step 8: Configure URLs

### Project URLs
Edit `counter_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('counter.urls')),
]
```


```bash
git add .
git commit -m "Configure URLs"
```

### App URLs
Create `counter/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increment/', views.increment, name='increment'),
    path('decrement/', views.decrement, name='decrement'),
    path('reset/', views.reset, name='reset'),
]
```

```bash
git add .
git commit -m "Create Django app urls"
```
## Step 9: Create Templates Directory

```bash
mkdir -p counter/templates/counter
git add .
git commit -m "Create templates folder
```


## Step 10: Create HTML Template

Create `counter/templates/counter/index.html`:

```html
<!DOCTYPE html>
<html lang="en" data-theme="cyberpunk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counter App</title>
    
    <!-- DaisyUI + Tailwind CSS -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- HTMX -->
    <script src="https://unpkg.com/htmx.org@2.0.3"></script>
</head>
<body>
    <div class="min-h-screen flex items-center justify-center bg-base-200">
        <div class="card w-96 bg-base-100 shadow-2xl">
            <div class="card-body items-center text-center">
                <h2 class="card-title text-4xl mb-8 text-primary">Counter App</h2>
                
                <!-- Counter Display -->
                <div class="bg-base-300 rounded-lg p-8 mb-8 w-full">
                    <div id="counter-display" class="text-6xl font-bold text-secondary">
                        {{ counter }}
                    </div>
                </div>
                
                <!-- Buttons -->
                <div class="card-actions flex gap-4">
                    <!-- Decrement Button -->
                    <button 
                        class="btn btn-circle btn-primary btn-lg"
                        hx-get="/decrement/"
                        hx-target="#counter-display"
                        hx-swap="innerHTML"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M20 12H4" />
                        </svg>
                    </button>
                    
                    <!-- Reset Button -->
                    <button 
                        class="btn btn-circle btn-accent btn-lg"
                        hx-get="/reset/"
                        hx-target="#counter-display"
                        hx-swap="innerHTML"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                        </svg>
                    </button>
                    
                    <!-- Increment Button -->
                    <button 
                        class="btn btn-circle btn-primary btn-lg"
                        hx-get="/increment/"
                        hx-target="#counter-display"
                        hx-swap="innerHTML"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M12 4v16m8-8H4" />
                        </svg>
                    </button>
                </div>
                
                <!-- Info -->
                <div class="mt-8 text-sm opacity-70">
                    <p>Built with Django, DaisyUI & HTMX</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

```bash

git add .
git commit -m "Create Django template"
```

## Step 11: Run Migrations

```bash
python manage.py migrate
```

## Step 12: Run the Development Server

```bash
python manage.py runserver
```

## Step 13: Open in Browser

Navigate to: **http://127.0.0.1:8000/**

You should see a cyberpunk-themed counter with three round buttons that work!

## How HTMX Works

HTMX makes AJAX simple with HTML attributes:

- **`hx-get="/increment/"`** - Makes a GET request to the URL
- **`hx-target="#counter-display"`** - Specifies which element to update
- **`hx-swap="innerHTML"`** - Replaces the content of the target element

When you click a button:
1. HTMX sends a request to Django
2. Django returns the new counter value as plain text
3. HTMX updates the `#counter-display` element with the new value

No JavaScript needed!

## Troubleshooting

### Buttons Not Working?

1. **Check browser console** (F12) for errors
2. **Verify HTMX loaded** - Look in Network tab for `htmx.org` request
3. **Check URLs** - Make sure they match your `urls.py` file
4. **Hard refresh** - Press Ctrl+Shift+R (or Cmd+Shift+R on Mac)

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Template Not Found
Make sure your directory structure is:
```
counter/
  templates/
    counter/
      index.html
```

### Virtual Environment
Make sure it's activated - you should see `(venv)` in your terminal.

## What Makes This Better

✅ **HTMX is simpler** - Just HTML attributes, no JavaScript
✅ **Reliable** - Battle-tested library used in production
✅ **Fast** - Lightweight and performant
✅ **Easy to debug** - Check Network tab to see requests

## Next Steps

- Add counter animations with HTMX extensions
- Persist counter in a database (SQLite, PostgreSQL)
- Add multiple counters with user sessions
- Add sound effects on button clicks
- Deploy to production (PythonAnywhere, Railway, Render)

---

**Your counter should now work perfectly! 🎉**
