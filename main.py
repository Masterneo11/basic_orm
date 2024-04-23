from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory.db", echo=True)


create_students_table = """
create table students(
student_id integer primary key not null, 
first_name text not null,
last_name text not null, 
email text not null, 
enrollment_year integer not null
);
"""
insert_students = """
insert into students 
(first_name, last_name, email, enrollment_year)

values (
    'Jimmy',
    'Earnhart',
    'Jimmies@gmail.com',
    20
);
"""

with engine.connect() as conn:
    conn.execute(text(create_students_table))
    conn.execute(text(insert_students))
    conn.commit()
    result = conn.execute(text("select * from students"))
    conn.commit()
    print(result.all())