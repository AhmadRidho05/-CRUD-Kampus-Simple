from flask import Flask, request

# Import handler mahasiswa
from mahasiswa.heandler import HandlerMahasiswa

# Import handler matakuliah
from matakuliah.heandler import HandlerMatakuliah

# Import handler kelas (❗ wajib supaya gak error)
from kelas.heandler import HandlerKelas


app = Flask(__name__)

# ====================================
# ROUTE MAHASISWA
# ====================================

@app.route('/mahasiswa/get-all', methods=['POST'])
def getAllMahasiswa():
    return HandlerMahasiswa.getAll()

@app.route('/mahasiswa/get-single', methods=['POST'])
def getSingleMahasiswa():
    return HandlerMahasiswa.getSingle(request)

@app.route('/mahasiswa/post', methods=['POST'])
def postMahasiswa():
    return HandlerMahasiswa.post(request)

@app.route('/mahasiswa/update', methods=['POST'])
def updateMahasiswa():
    return HandlerMahasiswa.update(request)

@app.route('/mahasiswa/delete', methods=['POST'])
def deleteMahasiswa():
    return HandlerMahasiswa.delete(request)


# ====================================
# ROUTE MATAKULIAH
# ====================================

@app.route('/matakuliah/get-all', methods=['POST'])
def getAllMatakuliah():
    return HandlerMatakuliah.getAll()

@app.route('/matakuliah/get-single', methods=['POST'])
def getSingleMatakuliah():
    return HandlerMatakuliah.getSingle(request)

@app.route('/matakuliah/post', methods=['POST'])
def postMatakuliah():
    return HandlerMatakuliah.post(request)

@app.route('/matakuliah/update', methods=['POST'])
def updateMatakuliah():
    return HandlerMatakuliah.update(request)

@app.route('/matakuliah/delete', methods=['POST'])
def deleteMatakuliah():
    return HandlerMatakuliah.delete(request)


# ====================================
# ROUTE KELAS
# ====================================

@app.route('/kelas/get-all', methods=['POST'])
def kelasGetAll():
    return HandlerKelas.getAll()

@app.route('/kelas/get-single', methods=['POST'])
def kelasGetSingle():
    return HandlerKelas.getSingle(request)

@app.route('/kelas/post', methods=['POST'])
def kelasInsert():
    return HandlerKelas.post(request)

@app.route('/kelas/update', methods=['POST'])
def kelasUpdate():
    return HandlerKelas.update(request)

@app.route('/kelas/delete', methods=['POST'])
def kelasDelete():
    return HandlerKelas.delete(request)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8005)
