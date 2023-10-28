from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    stok = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    cart = Column(Integer, nullable=False)
    extend_existing=True
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'stok': self.stok,
            'price': self.price,
            'cart': self.cart,
        }