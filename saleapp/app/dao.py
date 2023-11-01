from app.models import Category, Product

def load_categories():
    return Category.query.all()
    # return [{
    #     'id': 1,
    #     'name': 'Mobile'
    # }, {
    #     'id': 2,
    #     'name': 'Tablet'
    # }]


def load_products(kw=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return  products.all()
    # products = [{
    #     'id': 1,
    #     'name': 'iPhone 15 Pro Max',
    #     'price': 46990000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-blue-1.jpg'
    # }, {
    #     'id': 2,
    #     'name': 'iPhone 14 Pro',
    #     'price': 24390000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/247508/iphone-14-pro-trang-1.jpg'
    # }, {
    #     'id': 3,
    #     'name': 'iPhone 14 Pro Max',
    #     'price': 27090000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg'
    # }, {
    #     'id': 4,
    #     'name': 'iPhone 13',
    #     'price': 16690000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/223602/iphone-13-1-3.jpg'
    # }, {
    #     'id': 5,
    #     'name': 'iPhone 12',
    #     'price': 13490000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/213031/iphone-12-1-2.jpg'
    # }, {
    #     'id': 6,
    #     'name': 'iPhone 11',
    #     'price': 10690000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/153856/iphone-11-den-1-1-1-org.jpg'
    # }, {
    #     'id': 7,
    #     'name': 'Samsung Galaxy Z Fold5 5G',
    #     'price': 36990000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/301608/samsung-galaxy-zfold5-xanh-256gb-1-1.jpg'
    # }, {
    #     'id': 8,
    #     'name': 'Samsung Galaxy Z Flip5 5G',
    #     'price': 21990000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/299250/samsung-galaxy-zflip5-xanh-256gb-1-1.jpg'
    # }, {
    #     'id': 9,
    #     'name': 'Samsung Galaxy Tab A8',
    #     'price': 5890000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/522/251704/samsung-galaxy-tab-a8-1-2.jpg'
    #     }, {
    #     'id': 10,
    #     'name': 'iPad Air 5 M1 WiFi 64GB',
    #     'price': 14390000,
    #     'image': 'https://cdn.tgdd.vn/Products/Images/522/248096/ipad-air-5-m1-xam-1.jpg'
    # }]
    #
    # if kw:
    #     products = [p for p in products if p['name'].find(kw) >= 0]
    #
    # return products
