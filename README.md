# TMDB Movie Dataset Analysis

## Tổng quan Dataset

- **Tổng số phim**: 10,866 bộ phim
- **Khoảng thời gian**: 1960 - 2015
- **Số đạo diễn**: 5,067 người
- **Số diễn viên**: 19,026 người  
- **Số thể loại**: 20 thể loại khác nhau
- **Tổng doanh thu**: $432.7 tỷ USD
- **Tổng ngân sách**: $158.9 tỷ USD
- **Tổng lợi nhuận**: $273.8 tỷ USD

## Các nhiệm vụ đã thực hiện

### 1. Sắp xếp phim theo ngày phát hành
- Xử lý và sửa lỗi format ngày tháng
- Sắp xếp từ mới nhất đến cũ nhất
- **Output**: `movies_sorted_by_release_date.csv`

### 2. Lọc phim có đánh giá cao
- Lọc 350 phim có điểm > 7.5/10 (3.2% tổng số)
- Phim cao điểm nhất: "The Story of Film: An Odyssey" (9.2/10)
- **Output**: `high_rated_movies.csv`

### 3. Phân tích doanh thu cực trị
- **Cao nhất**: Avatar ($2,781,505,847)
- **Thấp nhất**: Shattered Glass ($2)
- 6016 (55.4%) phim có doanh thu = 0

### 4. Tính tổng doanh thu
- **Tổng doanh thu**: $432,720,192,875
- **Doanh thu trung bình mỗi phim**: $39,823,320

### 5. Top 10 phim lợi nhuận cao nhất
 1. Avatar - Lợi nhuận: $2,544,505,847
 2. Star Wars: The Force Awakens - Lợi nhuận: $1,868,178,225
 3. Titanic - Lợi nhuận: $1,645,034,188
 4. Jurassic World - Lợi nhuận: $1,363,528,810
 5. Furious 7 - Lợi nhuận: $1,316,249,360
 6. The Avengers - Lợi nhuận: $1,299,557,910
 7. Harry Potter and the Deathly Hallows: Part 2 - Lợi nhuận: $1,202,817,822
 8. Avengers: Age of Ultron - Lợi nhuận: $1,125,035,767
 9. Frozen - Lợi nhuận: $1,124,219,009
10. The Net - Lợi nhuận: $1,084,279,658

### 6. Thống kê nhân vật nổi bật
- **Đạo diễn nhiều phim nhất**: Woody Allen (45 phim)
- **Diễn viên xuất hiện nhiều nhất**: Robert De Niro (72 phim)

### 7. Phân tích thể loại phim
- **Top 3**: Drama (4,761), Comedy (3,793), Thriller (2,908)

## Cách sử dụng

### Cài đặt môi trường Python và thư viện cần thiết
```bash
git clone https://github.com/audreydang4103/Dang_Thao_LV1_project_03

cd https://github.com/audreydang4103/Dang_Thao_LV1_project_03
```

### Cài đặt môi trường Python và thư viện cần thiết
```bash
pip install pandas numpy 
```

### Chạy script
```python
python Dang_Thao_LV1_project_03.py
```

```

## License

Dataset từ [TMDB](https://www.themoviedb.org/)

