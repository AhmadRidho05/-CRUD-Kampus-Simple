from .repo import RepoKelas

class UsecaseKelas:

    @staticmethod
    def getAll():
        return RepoKelas.getAllData()

    @staticmethod
    def getSingle(id_kelas):
        return RepoKelas.getSingle(id_kelas)

    @staticmethod
    def insert(data):
        return RepoKelas.insert(data)

    @staticmethod
    def update(id_kelas, data):
        return RepoKelas.update(id_kelas, data)

    @staticmethod
    def delete(id_kelas):
        return RepoKelas.delete(id_kelas)
