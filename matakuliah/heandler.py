from .usecase import UsecaseMatakuliah # type: ignore

class HandlerMatakuliah:

    # GET ALL
    @staticmethod
    def getAll():
        return UsecaseMatakuliah.getAll()

    # GET SINGLE
    @staticmethod
    def getSingle(request):
        id_matakuliah = request.json.get('id_matakuliah')
        return UsecaseMatakuliah.getSingle(id_matakuliah)

    # INSERT
    @staticmethod
    def post(request):
        payload = {
            "nama_matakuliah": request.json.get("nama_matakuliah"),
            "sks": request.json.get("sks"),
            "dosen_pengampu": request.json.get("dosen_pengampu")
        }
        return UsecaseMatakuliah.post(payload)

    # UPDATE
    @staticmethod
    def update(request):
        id_matakuliah = request.json.get("id_matakuliah")
        payload = {
            "nama_matakuliah": request.json.get("nama_matakuliah"),
            "sks": request.json.get("sks"),
            "dosen_pengampu": request.json.get("dosen_pengampu")
        }
        return UsecaseMatakuliah.update(id_matakuliah, payload)

    # DELETE
    @staticmethod
    def delete(request):
        id_matakuliah = request.json.get("id_matakuliah")
        return UsecaseMatakuliah.delete(id_matakuliah)
