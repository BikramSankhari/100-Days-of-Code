from sqlalchemy import create_engine, MetaData, Table, Integer, \
    String, Column, ForeignKey, insert, select, update, bindparam

engine = create_engine("sqlite:///core_data.db")

metadata_obj = MetaData()

user_table = Table(
    "user_details",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(20))
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("address", String),
    Column("user_id", Integer, ForeignKey("user_details.id"), nullable=False)
)

# metadata_obj.create_all(bind=engine)

stmt = insert(address_table)

with engine.connect() as con:
    # con.execute(stmt, [{"name": "u1"},
    #                    {"name": "u2"},
    #                    {"name": "u3"}])

    # con.commit()

    # con.execute(stmt, [{"address": "address1", "user_id": 3},
    #                    {"address": "address1", "user_id": 1},
    #                    {"address": "address1", "user_id": 1}])
    #
    # con.commit()
    con.execute(update(user_table).where(user_table.c.name == bindparam("nam")).values(id=bindparam("id")),
                [{"nam": "u1", "id": 0},
                 {"nam": "u2", "id": 1},
                 {"nam": "u3", "id": 2}])
    con.commit()

    results = con.execute(select(user_table))
    for row in results:
        print(row)
