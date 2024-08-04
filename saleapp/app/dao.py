from app.models import Category, Product, User, Receipt, ReceiptDetails, Comment
from app import app, db
import hashlib
from flask_login import current_user
from sqlalchemy import func
import cloudinary.uploader


def get_categories():
    return Category.query.all()


def get_products(kw, cate_id, page=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size

        return products.slice(start, start + page_size)

    return products.all()


def count_product():
    return Product.query.count()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()


def add_receipt(cart):
    if cart:
        r = Receipt(user=current_user)
        db.session.add(r)

        for c in cart.values():
            d = ReceiptDetails(quantity=c['quantity'], price=c['price'], receipt=r, product_id=c['id'])
            db.session.add(d)

        try:
            db.session.commit()
        except:
            return False
        else:
            return True

    return False


def count_products_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
                     .join(Product, Product.category_id.__eq__(Category.id), isouter=True)\
                     .group_by(Category.id).all()


def stats_revenue(kw=None):
    query = db.session.query(Product.id, Product.name, func.sum(ReceiptDetails.price*ReceiptDetails.quantity))\
                      .join(ReceiptDetails, ReceiptDetails.product_id.__eq__(Product.id))
    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.group_by(Product.id).all()


def stats_revenue_by_month(year=2024):
    return db.session.query(func.extract('month', Receipt.created_date),
                            func.sum(ReceiptDetails.price*ReceiptDetails.quantity))\
                     .join(ReceiptDetails, ReceiptDetails.receipt_id.__eq__(Receipt.id))\
                     .filter(func.extract('year', Receipt.created_date).__eq__(year))\
                     .group_by(func.extract('month', Receipt.created_date)).all()


def add_user(name, username, password, avatar):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password)

    if avatar:
        res = cloudinary.uploader.upload(avatar)
        u.avatar = res['secure_url']

    db.session.add(u)
    db.session.commit()


def get_product_by_id(id):
    return Product.query.get(id)


def get_comments(product_id):
    return Comment.query.filter(Comment.product_id.__eq__(product_id)).all()


def add_comment(product_id, content):
    c = Comment(product_id=product_id, content=content, user=current_user)
    db.session.add(c)
    db.session.commit()

    return c


if __name__ == '__main__':
    with app.app_context():
        print(stats_revenue_by_month())


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
