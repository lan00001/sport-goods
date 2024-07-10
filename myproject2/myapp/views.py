from django.shortcuts import get_object_or_404,render, redirect  # 导入 redirect
from .forms import ProductForm
from .models import Product

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'myapp/upload_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})
