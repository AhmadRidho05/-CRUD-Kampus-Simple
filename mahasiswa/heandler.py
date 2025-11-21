from .usecase import Usecase

class HandlerMahasiswa():
    def getAll():
        return Usecase.getAll()
    
    def getSingle(request):
        kode = request.json.get('kode')
        return Usecase.getSingle(kode)
    
    def update():
        return Usecase.update()
    
    def delete():
        return Usecase.delete()
    
    def post():
        return Usecase.post()