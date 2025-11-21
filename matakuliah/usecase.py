from .repo import RepoMatakuliah # type: ignore

class UsecaseMatakuliah:

    # =========================
    # GET ALL DATA
    # =========================
    @staticmethod
    def getAll():
        data = RepoMatakuliah.getAllData()
        return data

    # =========================
    # GET SINGLE DATA
    # =========================
    @staticmethod
    def getSingle(id_matakuliah):
        data = RepoMatakuliah.getSingle(id_matakuliah)
        return data

    # =========================
    # INSERT DATA
    # =========================
    @staticmethod
    def post(payload):
        new_id = RepoMatakuliah.insert(payload)

        return {
            "code": 200,
            "message": "Berhasil Menambahkan Data",
            "data": new_id
        }

    # =========================
    # UPDATE DATA
    # =========================
    @staticmethod
    def update(id_matakuliah, payload):
        RepoMatakuliah.update(id_matakuliah, payload)

        return {
            "code": 200,
            "message": "Berhasil Update Data",
            "id": id_matakuliah
        }

    # =========================
    # DELETE DATA
    # =========================
    @staticmethod
    def delete(id_matakuliah):
        RepoMatakuliah.delete(id_matakuliah)

        return {
            "code": 200,
            "message": "Berhasil Menghapus Data",
            "id": id_matakuliah
        }
