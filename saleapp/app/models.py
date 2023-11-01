from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app import app, db


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='iPhone 15 Pro Max', price=46990000,
                     image='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-blue-1.jpg',
                     category_id=1)
        p2 = Product(name='iPhone 14 Pro', price=24390000,
                     image='https://cdn.tgdd.vn/Products/Images/42/247508/iphone-14-pro-trang-1.jpg',
                     category_id=1)
        p3 = Product(name='iPhone 14 Pro Max', price=27090000,
                     image='https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg',
                     category_id=1)
        p4 = Product(name='iPhone 13', price=16690000,
                     image='https://cdn.tgdd.vn/Products/Images/42/223602/iphone-13-1-3.jpg',
                     category_id=1)
        p5 = Product(name='iPhone 12', price=13490000,
                     image='https://cdn.tgdd.vn/Products/Images/42/213031/iphone-12-1-2.jpg',
                     category_id=1)
        p6 = Product(name='iPhone 11', price=10690000,
                     image='https://cdn.tgdd.vn/Products/Images/42/153856/iphone-11-den-1-1-1-org.jpg',
                     category_id=1)
        p7 = Product(name='Samsung Galaxy Z Fold5 5G', price=36990000,
                     image='https://cdn.tgdd.vn/Products/Images/42/301608/samsung-galaxy-zfold5-xanh-256gb-1-1.jpg',
                     category_id=1)
        p8 = Product(name='Samsung Galaxy Z Flip5 5G', price=21990000,
                     image='https://cdn.tgdd.vn/Products/Images/42/299250/samsung-galaxy-zflip5-xanh-256gb-1-1.jpg',
                     category_id=1)
        p9 = Product(name='Samsung Galaxy Tab A8', price=5890000,
                     image='https://cdn.tgdd.vn/Products/Images/522/251704/samsung-galaxy-tab-a8-1-2.jpg',
                     category_id=2)
        p10 = Product(name='iPad Air 5 M1 WiFi 64GB', price=14390000,
                      image='https://cdn.tgdd.vn/Products/Images/522/248096/ipad-air-5-m1-xam-1.jpg',
                      category_id=2)

        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        db.session.commit()

        # db.create_all()
