from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {'name': 'худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'image_path': "/static/vendor/img/products/Adidas-hoodie.png",
             'status': 'Отправить в корзину'},
            {'name': 'синяя куртка The North Face', 'price': 23725,
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'image_path': "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
             'status': 'Удалить из корзины'},
            {'name': 'коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'image_path': "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
             'status': 'Отправить в корзину'},
            {'name': 'черный рюкзак Nike Heritage', 'price': 2340,
             'description': 'Плотная ткань. Легкий материал.',
             'image_path': "/static/vendor/img/products/Black-Nike-Heritage-backpack.png",
             'status': 'Отправить в корзину'},
            {'name': 'черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'image_path': "/static/vendor/img/products/Black-Dr-Martens-shoes.png",
             'status': 'Отправить в корзину'},
            {'name': 'темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'image_path': "/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
             'status': 'Отправить в корзину'},
        ],
    }
    return render(request, "products/products.html", context)
