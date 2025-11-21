from .repo import RepoData
class Usecase():
    def getAll():
        data = RepoData.getAllData()
        return data
    
    def getSingle(kode):
        data = RepoData.getSingle(kode)
        return data
    
    def update():
        data = {
            "code" : 200,
            "message" : "Berhasil Update Data"
        }

        return data
    
    def delete():
        data = {
            "code" : 200,
            "message" : "Berhasil Menghapus Data"
        }

        return data
    
    def post():
        data = {
            "code" : 200,
            "message" : "Berhasil Manambahkan Data"
        }

        return data
