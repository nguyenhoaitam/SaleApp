def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone 15 Pro Max',
        'price': "46.990.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-blue-1.jpg'
    }, {
        'id': 2,
        'name': 'iPhone 14 Pro',
        'price': "24.390.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/247508/iphone-14-pro-trang-1.jpg'
    }, {
        'id': 3,
        'name': 'iPhone 14 Pro Max',
        'price': "27.090.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg'
    }, {
        'id': 4,
        'name': 'iPhone 13',
        'price': "16.690.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/223602/iphone-13-1-3.jpg'
    }, {
        'id': 5,
        'name': 'iPhone 12',
        'price': "13.490.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/213031/iphone-12-1-2.jpg'
    }, {
        'id': 6,
        'name': 'iPhone 11',
        'price': "10.690.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/153856/iphone-11-den-1-1-1-org.jpg'
    }, {
        'id': 7,
        'name': 'Samsung Galaxy Z Fold5 5G',
        'price': "36.990.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/301608/samsung-galaxy-zfold5-xanh-256gb-1-1.jpg'
    }, {
        'id': 8,
        'name': 'Samsung Galaxy Z Flip5 5G',
        'price': "21.990.000",
        'image': 'https://cdn.tgdd.vn/Products/Images/42/299250/samsung-galaxy-zflip5-xanh-256gb-1-1.jpg'
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
