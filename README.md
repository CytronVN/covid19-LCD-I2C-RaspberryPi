# covid19-LCD-I2C-RaspberryPi
Hiển thị số ca nhiễm Covid ở Việt Nam lên màn hình LCD I2C sử dụng Raspberry Pi

Chương trình này gồm 2 tập tin:

+ I2C_LCD_driver.py - Driver cho màn hình LCD I2C 1602
+ Vietnam.py - Chương trình chính

Để chạy được chương trình, bạn cần có **Python** và bộ thư viện **smbus**. Hãy tải 2 tập tin được đề cập về máy và chạy **python3 Vietnam.py**
Chương trình sẽ lấy dữ liệu về số ca nhiễm Covid từ file https://jhucoronavirus.azureedge.net/api/v1/regions/vn.json và hiển thị kết quả trên màn hình LCD I2C.
Dữ liệu về số ca nhiễm Covid được Trung tâm thông tin về Coronavirus của **Đại học Johns Hopkins**, Hoa Kỳ cung cấp. Dữ liệu có thể được cập nhật trễ khoảng 1 ngày.

Để tham khảo video hướng dẫn, hãy truy cập https://www.facebook.com/CytronTech.vn/posts/214277054037180
Những sản phẩm liên quan có thể tìm được thấy tại website https://cytrontech.vn

