from .usecase import UsecaseKelas

class HandlerKelas:

    @staticmethod
    def getAll():
        return UsecaseKelas.getAll()

    @staticmethod
    def getSingle(request):
        id_kelas = request.json.get('id_kelas')
        return UsecaseKelas.getSingle(id_kelas)

    @staticmethod
    def insert(request):
        data = request.json
        return UsecaseKelas.insert(data)

    @staticmethod
    def update(request):
        data = request.json
        id_kelas = data.get('id_kelas')
        return UsecaseKelas.update(id_kelas, data)

    @staticmethod
    def delete(request):
        id_kelas = request.json.get('id_kelas')
        return UsecaseKelas.delete(id_kelas)
