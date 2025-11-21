import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='mahasiswa',
        user='postgres',
        password='Qwerty1357',
        port='5432'
    )
    return conn

class RepoData:

    @staticmethod
    def getAllData():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                nama, 
                "NIM", 
                "Tahun_masuk", 
                "Alamat", 
                "Tanggal_lahir"
            FROM mahasiswa
            ORDER BY nama DESC;
        """)

        rows = cur.fetchall()
        cur.close()
        conn.close()

        payload = [
            {
                "nama": row[0],
                "nim": row[1],
                "tahun_masuk": row[2],
                "alamat": row[3],
                "tanggal_lahir": row[4]
            }
            for row in rows
        ]

        return payload

    @staticmethod
    def getSingle(nim):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                nama, 
                "NIM", 
                "Tahun_masuk", 
                "Alamat", 
                "Tanggal_lahir"
            FROM mahasiswa
            WHERE "NIM" = %s;
        """, (nim,))

        row = cur.fetchone()
        cur.close()
        conn.close()

        if row is None:
            return None

        payload = {
            "nama": row[0],
            "nim": row[1],
            "tahun_masuk": row[2],
            "alamat": row[3],
            "tanggal_lahir": row[4]
        }

        return payload
