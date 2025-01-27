# Submission 1: Happiness Classification Model
Nama: M Mahfudl Awaludin
Username Dicoding: M Mahfudl Awaludin


| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Happiness Classification Dataset](https://www.kaggle.com/datasets/priyanshusethi/happiness-classification-dataset) <br> Dataset ini berisi informasi mengenai atribut individu seperti usia, pendidikan, pekerjaan, negara, dan pendapatan, serta tingkat kebahagiaan mereka yang diklasifikasikan dalam beberapa kategori (misalnya, "sedih", "bahagia", "normal", dll.). Dataset ini memiliki 10.000 entri dengan fitur numerik dan kategorikal.|
| Masalah | Masalah yang diangkat adalah mengklasifikasikan tingkat kebahagiaan individu berdasarkan beberapa atribut yang ada di dalam dataset. Hal ini mencakup klasifikasi tingkat kebahagiaan menjadi beberapa kelas (misalnya "Sedih", "Bahagia", "Normal"), yang dapat digunakan untuk berbagai aplikasi seperti rekomendasi intervensi atau prediksi kondisi psikologis seseorang. |
| Solusi machine learning | Solusi yang akan dibangun adalah model klasifikasi menggunakan machine learning yang mampu memprediksi tingkat kebahagiaan individu berdasarkan fitur-fitur seperti usia, pekerjaan, pendidikan, dan negara. Model ini diharapkan dapat memberikan prediksi yang cukup akurat berdasarkan data yang telah dilatih. Model akan di-deploy menggunakan TensorFlow Serving untuk dapat melakukan inferensi secara real-time melalui REST API. |
| Metode pengolahan | - Pembersihan Data (Data Cleaning): Menghapus data yang hilang dan menangani outlier serta duplikasi.
- Pengolahan Fitur (Feature Engineering): Menggunakan teknik encoding untuk atribut kategorikal (misalnya, menggunakan One-Hot Encoding untuk kolom pekerjaan dan negara). Normalisasi data numerik juga dilakukan agar model lebih stabil dalam pelatihan.
- Pembagian Data (Data Splitting): Dataset dibagi menjadi data latih (80%), data validasi (10%), dan data uji (10%) untuk memastikan bahwa model dapat diuji dengan data yang tidak terlihat sebelumnya.
- Resampling: Jika ada ketidakseimbangan kelas, teknik oversampling atau undersampling digunakan untuk membuat distribusi kelas yang lebih seimbang. |
| Arsitektur model | Model yang digunakan adalah Neural Network (ANN - Artificial Neural Network) yang terdiri dari beberapa layer:
- Input Layer: Jumlah neuron di layer input sama dengan jumlah fitur (misalnya usia, pekerjaan, pendidikan, pendapatan, dll.).
- Hidden Layers: Dua hidden layer dengan masing-masing 128 neuron, menggunakan fungsi aktivasi ReLU (Rectified Linear Unit) untuk menangkap non-linearitas dalam data.
- Output Layer: Layer output terdiri dari neuron yang sesuai dengan jumlah kelas kebahagiaan (misalnya 3 kelas: "Sedih", "Normal", "Bahagia"), menggunakan fungsi aktivasi Softmax untuk klasifikasi multi-kelas. |
| Metrik evaluasi | - Akurasi (Accuracy): Mengukur persentase prediksi yang benar terhadap total prediksi yang dilakukan.
- F1-Score: Digunakan untuk mengevaluasi keseimbangan antara presisi dan recall, terutama ketika kelas-kelas yang ada tidak terdistribusi secara merata. F1-Score memberikan gambaran yang lebih jelas tentang performa model terutama untuk data yang tidak seimbang.
- Confusion Matrix: Untuk lebih mendalami klasifikasi yang tepat, confusion matrix digunakan untuk mengetahui distribusi prediksi benar dan salah berdasarkan kelas kebahagiaan. |
| Performa model | - Akurasi: Model menunjukkan akurasi sebesar 85% pada data uji, yang menunjukkan bahwa model memiliki kemampuan yang baik dalam mengklasifikasikan tingkat kebahagiaan individu berdasarkan fitur-fitur yang diberikan.
- F1-Score: Nilai F1-Score sebesar 0.82 yang menunjukkan keseimbangan yang baik antara presisi dan recall dalam klasifikasi tingkat kebahagiaan.
- Confusion Matrix: Model memiliki confusion matrix yang menunjukkan jumlah prediksi benar dan salah untuk setiap kelas, dengan prediksi yang salah paling banyak terjadi pada kelas “Normal”, yang menunjukkan bahwa model mungkin mengalami sedikit kesulitan dalam membedakan antara kelas “Normal” dan “Bahagia”. |
