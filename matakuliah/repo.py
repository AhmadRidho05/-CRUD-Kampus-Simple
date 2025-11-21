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


class RepoMatakuliah:

    # =========================
    # GET ALL DATA
    # =========================
    @staticmethod
    def getAllData():
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                id_matakuliah,
                nama_matakuliah,
                sks,
                dosen_pengampu
            FROM mata_kuliah
            ORDER BY id_matakuliah ASC;
        """)

        rows = cur.fetchall()
        cur.close()
        conn.close()

        payload = [
            {
                "id_matakuliah": row[0],
                "nama_matakuliah": row[1],
                "sks": row[2],
                "dosen_pengampu": row[3]
            }
            for row in rows
        ]

        return payload

    # =========================
    # GET SINGLE DATA
    # =========================
    @staticmethod
    def getSingle(id_matakuliah):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                id_matakuliah,
                nama_matakuliah,
                sks,
                dosen_pengampu
            FROM mata_kuliah
            WHERE id_matakuliah = %s;
        """, (id_matakuliah,))

        row = cur.fetchone()
        cur.close()
        conn.close()

        if row is None:
            return None

        payload = {
            "id_matakuliah": row[0],
            "nama_matakuliah": row[1],
            "sks": row[2],
            "dosen_pengampu": row[3]
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
            INSERT INTO mata_kuliah (nama_matakuliah, sks, dosen_pengampu)
            VALUES (%s, %s, %s)
            RETURNING id_matakuliah;
        """, (data["nama_matakuliah"], data["sks"], data["dosen_pengampu"]))

        new_id = cur.fetchone()[0]
        conn.commit()

        cur.close()
        conn.close()

        return {"inserted_id": new_id}

    # =========================
    # UPDATE DATA
    # =========================
    @staticmethod
    def update(id_matakuliah, data):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE mata_kuliah
            SET 
                nama_matakuliah = %s,
                sks = %s,
                dosen_pengampu = %s
            WHERE id_matakuliah = %s;
        """, (
            data["nama_matakuliah"],
            data["sks"],
            data["dosen_pengampu"],
            id_matakuliah
        ))

        conn.commit()
        cur.close()
        conn.close()

        return {"updated_id": id_matakuliah}

    # =========================
    # DELETE DATA
    # =========================
    @staticmethod
    def delete(id_matakuliah):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM mata_kuliah
            WHERE id_matakuliah = %s;
        """, (id_matakuliah,))

        conn.commit()
        cur.close()
        conn.close()

        return {"deleted_id": id_matakuliah}
