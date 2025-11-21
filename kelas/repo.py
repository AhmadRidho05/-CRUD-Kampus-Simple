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


class RepoKelas:

    # =========================
    # GET ALL DATA
    # =========================
    @staticmethod
    def getAllData():
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                id_kelas,
                nama_kelas,
                angkatan,
                deskripsi
            FROM kelas
            ORDER BY id_kelas ASC;
        """)

        rows = cur.fetchall()
        cur.close()
        conn.close()

        payload = [
            {
                "id_kelas": row[0],
                "nama_kelas": row[1],
                "angkatan": row[2],
                "deskripsi": row[3]
            }
            for row in rows
        ]
        return payload

    # =========================
    # GET SINGLE DATA
    # =========================
    @staticmethod
    def getSingle(id_kelas):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                id_kelas,
                nama_kelas,
                angkatan,
                deskripsi
            FROM kelas
            WHERE id_kelas = %s;
        """, (id_kelas,))

        row = cur.fetchone()
        cur.close()
        conn.close()

        if row is None:
            return None

        payload = {
            "id_kelas": row[0],
            "nama_kelas": row[1],
            "angkatan": row[2],
            "deskripsi": row[3]
        }
        return payload

    # =========================
    # INSERT DATA
    # =========================
    @staticmethod
    def insert(data):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO kelas (nama_kelas, angkatan, deskripsi)
            VALUES (%s, %s, %s)
            RETURNING id_kelas;
        """, (data["nama_kelas"], data["angkatan"], data["deskripsi"]))

        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return {"inserted_id": new_id}

    # =========================
    # UPDATE DATA
    # =========================
    @staticmethod
    def update(id_kelas, data):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE kelas
            SET 
                nama_kelas = %s,
                angkatan = %s,
                deskripsi = %s
            WHERE id_kelas = %s;
        """, (
            data["nama_kelas"],
            data["angkatan"],
            data["deskripsi"],
            id_kelas
        ))

        conn.commit()
        cur.close()
        conn.close()

        return {"updated_id": id_kelas}

    # =========================
    # DELETE DATA
    # =========================
    @staticmethod
    def delete(id_kelas):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM kelas
            WHERE id_kelas = %s;
        """, (id_kelas,))

        conn.commit()
        cur.close()
        conn.close()

        return {"deleted_id": id_kelas}
