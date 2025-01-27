import json
import numpy as np
import tensorflow as tf
from flask import Flask, request

app = Flask(__name__) 
#============Membuat API Endpoint dalam Web App sebagai Model Serving===============
MODEL_PATH = r"C:\Users\user\Music\submission-mlops\serving_model_dir\happy-detection-model\1737921786"  # Ganti dengan path model Anda
model = tf.saved_model.load(MODEL_PATH)

def data_preprocessing(data):
    # Mengubah data menjadi array numpy dan melakukan normalisasi
    image = np.array(data) / 255.0
    image = np.expand_dims(image, axis=0)  # Menambahkan dimensi batch
    return image

@app.route("/predict", methods=["POST"])
def predict():
    try:
        request_json = request.json
        
        # Memastikan data yang diterima tidak kosong
        if not request_json or "data" not in request_json:
            return json.dumps({"error": "Invalid input data"}), 400
        
        # Mengambil data dari request dan mengonversi ke format yang diharapkan
        input_data = {
            'events_xf': np.array(request_json["data"]["events_xf"]).reshape(-1, 1).astype(np.float32),
            'housecost_xf': np.array(request_json["data"]["housecost_xf"]).reshape(-1, 1).astype(np.float32),
            'infoavail_xf': np.array(request_json["data"]["infoavail_xf"]).reshape(-1, 1).astype(np.float32),
            'policetrust_xf': np.array(request_json["data"]["policetrust_xf"]).reshape(-1, 1).astype(np.float32),
            'schoolquality_xf': np.array(request_json["data"]["schoolquality_xf"]).reshape(-1, 1).astype(np.float32),
            'streetquality_xf': np.array(request_json["data"]["streetquality_xf"]).reshape(-1, 1).astype(np.float32)
        }

        # Melakukan prediksi
        prediction = model(input_data)
        prediction = tf.argmax(prediction[0]).numpy()

        # Daftar nama kelas (sesuaikan dengan model Anda)
        class_names = ['Class 0', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 
                       'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9']  # Ganti dengan nama kelas yang sesuai
        
        response_json = {
            "prediction": class_names[prediction]
        }

        return json.dumps(response_json)
    
    except Exception as e:
        print(f"Error: {e}")  # Mencetak kesalahan ke konsol
        return json.dumps({"error": str(e)}), 500  # Mengembalikan kesalahan sebagai respons
#===================================================================================

#=============================Menjalankan Web App===================================
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
#===================================================================================