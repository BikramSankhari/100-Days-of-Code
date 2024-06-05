from sqlalchemy import create_engine, ForeignKey, select, or_, and_, func, desc
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

engine = create_engine("sqlite:///orm_data.db")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_tabel"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"user_id : {self.id}, user_name : {self.name}"


class Address(Base):
    __tablename__ = "address_tabel"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_tabel.id"))
    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"address_id: {self.id}, address: {self.address}, user_id : {self.user_id}"


# Base.metadata.create_all(engine)

u1 = User(name="u1")
u2 = User(name="u2")
u3 = User(name="u3")

a1 = Address(address="address1")
a2 = Address(address="address2")
a3 = Address(address="address3")

u1.addresses.append(a2)
u1.addresses.append(a3)
u3.addresses.append(a1)

with Session(engine) as session:
    # session.add(u1)
    # session.add(u2)
    # session.add(u3)
    # session.flush()
    # session.commit()

    # session.add_all([a1, a2, a3])
    # session.flush()
    # session.commit()

    # results = session.execute(select(User.name, func.count(Address.address).label("count")).
    #                           join_from(User, Address, isouter=True).group_by(User.id).order_by(desc("count")))
    # for row in results:
    #     print(row)

    # results = session.scalars(select(func.upper(User.name)))
    #
    # for row in results:
    #     print(row)

    # u = session.execute(select(User).where(User.name == "u2")).scalar_one()
    #
    # u.name = "new u2"
    #
    # results = session.execute(select(User))
    # for r in results:
    #     print(r)
    #
    # session.rollback()
    # print()
    # a4 = Address(address="address4")
    # user = session.execute(select(User).where(User.id == 1)).scalar_one()
    # user.addresses.append(a4)
    # session.add(a4)
    # session.commit()

    # addr = session.execute(select(Address).where(Address.id == 2)).scalar_one()
    # addr.user_id = 2
    # session.commit()

    results = session.execute(select(User.name, Address).join(User))
    for r in results:
        print(r)


