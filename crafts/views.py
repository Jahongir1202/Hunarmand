from .forms import  ContactForm
from .utils import send_to_telegram
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm
ADMIN_USERNAME = "admin"

def home(request):
    products = Product.objects.all().order_by('-created_at')
    user = request.GET.get("user", "")
    form = ProductForm()
    contact_form = ContactForm()

    # Mahsulot qo‘shish (faqat admin uchun)
    if user == ADMIN_USERNAME and request.method == "POST" and 'add_product' in request.POST:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/?user={ADMIN_USERNAME}")

    # Murojaat formasini yuborish
    elif request.method == "POST" and 'contact_submit' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            msg = (
                f"📩 Yangi murojaat:\n\n"
                f"👤 {data['first_name']} {data['last_name']}\n"
                f"📞 {data['phone']}\n"
                f"💬 {data['message']}"
            )
            send_to_telegram(msg)
            return redirect('home')

    # Mahsulot sotib olish
    elif request.method == "POST" and 'buy_product' in request.POST:
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        phone = request.POST.get("phone")
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)

        message = (
            f"🛒 Yangi buyurtma!\n\n"
            f"👤 {first} {last}\n"
            f"📞 {phone}\n"
            f"🪙 Mahsulot: {product.name}\n"
            f"💰 Narxi: {product.price} so'm"
        )

        send_to_telegram(message, product.image.path)
        return redirect('home')

    context = {
        'products': products,
        'form': form,
        'is_admin': user == ADMIN_USERNAME,
        'contact_form': contact_form
    }
    return render(request, 'home.html', context)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345"

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri!")
            return redirect('admin_login')

    return render(request, 'admin/login.html')

def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    products = Product.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot muvaffaqiyatli qo‘shildi!")
            return redirect('admin_dashboard')
    else:
        form = ProductForm()

    return render(request, 'admin/dashboard.html', {'form': form, 'products': products})

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')

def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    products = Product.objects.all().order_by('-created_at')

    # 🟢 Tahrirlash (edit)
    if 'edit_id' in request.POST:
        product = get_object_or_404(Product, id=request.POST['edit_id'])
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot tahrirlandi ✅")
            return redirect('admin_dashboard')

    # 🔴 O‘chirish (delete)
    elif 'delete_id' in request.POST:
        product = get_object_or_404(Product, id=request.POST['delete_id'])
        product.delete()
        messages.success(request, "Mahsulot o‘chirildi ❌")
        return redirect('admin_dashboard')

    # 🟢 Yangi qo‘shish
    elif request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot qo‘shildi ✅")
            return redirect('admin_dashboard')
    else:
        form = ProductForm()

    return render(request, 'admin/dashboard.html', {'form': form, 'products': products})