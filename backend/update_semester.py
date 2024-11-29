import psycopg2
from config import config


def update_semester():
    conn = psycopg2.connect(**config)
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET semester = semester + 1
        WHERE reason = 'studium'
    """)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    update_semester()
