# GarbageClassification

## Giới thiệu 
* Với sự phát triển của xã hội ngày nay thì lượng rác thải đang tăng lên không ngừng.
* Vì vậy phân loại và tái chế rác thải là một việc làm hết sức cần thiết và có ý nghĩa quan trọng.
* Xây dựng bài toán phân loại rác thải dựa trên một trong những mô hình Deep Learning vô cùng tiên tiến  - mô hình mạng nơ ron tích chập (hay còn gọi là CNNs  - Convolutional Neural Network)  - 
* Hiện nay các mô hình CNNs được áp dụng nhiều trong các bài toán về phân loại hoặc truy vấn ảnh.
* Có thể áp dụng bài toán vào các hệ thống phân loại rác tự động.

1. Input: Dữ liệu đầu vào là các ảnh chứa 1 loại rác thải cụ thể 
2. Output: Nhãn của loại rác thải tương ứng

### Dữ liệu 

Dữ liệu được lấy từ google với tập gồm 15551 ảnh với 12 lớp, gồm các loại: 
* battery | 
* biological
* brown-glass 
* cardboard 
* clothes 
* green-glass 
* metal 
* paper 
* plastic 
* shoes 
* trash 
* white-glass

|Nguồn : [kaggle.com]

### Training model
Sử dụng Google Colab để train
**Framework:** Keras
**Language:** Python

Sử dụng mô hình VGG16 với phương pháp huấn luyện Transfer Learning: 
* **13 tầng đầu:** Sử dụng bộ trong số đã training sẵn với tập ImageNet
* **3 tầng cuối:** Train với tập dữ liệu trên

### Áp dụng model

#### Ứng dụng dự đoán rác thải qua ảnh
#### Ứng dụng dự đoán rác thải video realtime


