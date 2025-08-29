import pandas as pd
import numpy as np


# Tải và đọc dữ liệu
url = "https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv"
df = pd.read_csv(url)


# Task 1: Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới

def parse_date(row):
    try:
        date_str = row['release_date']
        year = row['release_year']
        month, day, yy = date_str.split('/')
        full_date_str = f"{month}/{day}/{year}"
        return pd.to_datetime(full_date_str)
    except:
        return pd.NaT
df['release_date_corrected'] = df.apply(parse_date, axis=1)

df_sorted_by_date = df.sort_values('release_date_corrected', ascending=False) 

df_sorted_by_date.to_csv('movies_sorted_by_release_date.csv', index=False)

print("Đã hoàn thành task 1: file mới movies_sorted_by_release_date.csv đã được lưu")
print("\n" + "="*60 + "\n")

# Task 2: Lọc ra các bộ phim có đánh giá trung bình trên 7.5 rồi lưu ra một file mới

high_rated_movies = df[df['vote_average'] > 7.5].copy()
high_rated_movies.to_csv('high_rated_movies.csv', index=False)

print(f"Có {len(high_rated_movies)} bộ phim có điểm đánh giá trên 7.5")
print(f"Tỷ lệ: {len(high_rated_movies)/len(df)*100:.1f}% tổng số phim")
print("Đã hoàn thành task 2")
print("\n" + "="*60 + "\n")

# Task 3: Tìm phim có doanh thu cao nhất và doanh thu thấp nhất

highest_revenue_movie = df.loc[df['revenue'].idxmax()]
print("PHIM CÓ DOANH THU CAO NHẤT:")
print(f"Tên phim: {highest_revenue_movie['original_title']}")
print(f"Đạo diễn: {highest_revenue_movie['director']}")
print(f"Doanh thu: ${highest_revenue_movie['revenue']:,.0f}")
print(f"Năm phát hành: {highest_revenue_movie['release_year']}")
print()

# Film có doanh thu thấp nhất (loại trừ 0)
non_zero_revenue = df[df['revenue'] > 0]
if len(non_zero_revenue) > 0:
    lowest_revenue_movie = non_zero_revenue.loc[non_zero_revenue['revenue'].idxmin()]
    print("\nPHIM CÓ DOANH THU THẤP NHẤT (loại trừ phim doanh thu = 0):")
    print(f"Tên phim: {lowest_revenue_movie['original_title']}")
    print(f"Đạo diễn: {lowest_revenue_movie['director']}")
    print(f"Doanh thu: ${lowest_revenue_movie['revenue']:,.0f}")
    print(f"Năm phát hành: {lowest_revenue_movie['release_year']}")


# Tổng số phim với có doanh thu bằng 0
zero_revenue_count = len(df[df['revenue'] == 0])
print(f"\nSố phim có doanh thu = 0: {zero_revenue_count} phim")
print("Đã hoàn thành task 3")
print("\n" + "="*60 + "\n")

# Task 4: Tính tổng doanh thu tất cả các bộ phim

total_revenue = df['revenue'].sum()
print(f"Tổng doanh thu tất cả các bộ phim: ${total_revenue:,.0f}")
print(f"Doanh thu trung bình mỗi phim: ${df['revenue'].mean():,.0f}")
print("Đã hoàn thành task 4")
print("\n" + "="*60 + "\n")

# Task 5: Top 10 bộ phim đem về lợi nhuận cao nhất

df['profit'] = df['revenue'] - df['budget']
top_profitable = df.nlargest(10, 'profit')

print("Top 10 bộ phim có lợi nhuận cao nhất:")
for i, (idx, movie) in enumerate(top_profitable.iterrows(), 1):
    print(f"{i:2d}. {movie['original_title']}")
    print(f"    Lợi nhuận: ${movie['profit']:,.0f}")
print("Đã hoàn thành task 5")
print("\n" + "="*60 + "\n")
    
# Task 6: Tìm đạo diễn nào có nhiều bộ phim nhất và diễn viên nào đóng nhiều phim nhất

director_counts = df[df['director'].notna()]['director'].value_counts()

top_director = director_counts.idxmax()
top_director_count = director_counts.max()
print(f"Đạo diễn có nhiều phim nhất: {top_director}: {top_director_count} phim")


actor_counts = {}
for cast_list in df[df['cast'].notna()]['cast']:
    if pd.notna(cast_list):
        actors = [actor.strip() for actor in cast_list.split('|')]
        for actor in actors:
            if actor: 
                actor_counts[actor] = actor_counts.get(actor, 0) + 1

sorted_actors = sorted(actor_counts.items(), key=lambda x: x[1], reverse=True)
top_actor, top_actor_count = sorted_actors[0]
print(f"Diễn viên xuất hiện nhiều nhất: {top_actor}: {top_actor_count} phim")

print("Đã hoàn thành task 6")
print("\n" + "="*60 + "\n")

# Task 7: Thống kê số lượng phim theo các thể loại

genre_counts = {}
for genres_list in df[df['genres'].notna()]['genres']:
    if pd.notna(genres_list):
        genres = [genre.strip() for genre in genres_list.split('|')]
        for genre in genres:
            if genre: 
                genre_counts[genre] = genre_counts.get(genre, 0) + 1

sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

print("Thống kê số lượng phim theo thể loại:")
total_genre_appearances = sum(genre_counts.values())

for i, (genre, count) in enumerate(sorted_genres, 1):
    percentage = (count / len(df)) * 100
    print(f"{i:2d}. {genre:<20}: {count:>4} phim ({percentage:5.1f}%)")
print("Đã hoàn thành task 7")
print("\n" + "="*60 + "\n")

#Tổng quan:

print("TỔNG QUAN DỮ LIỆU:")
print(f"- Tổng số phim: {len(df):,}")
print(f"Tổng số cột: {len(df.columns)}")
print("Các cột dữ liệu gồm:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")
print(f"- Khoảng thời gian: {df['release_year'].min()} - {df['release_year'].max()}")
print(f"- Số đạo diễn khác nhau: {df['director'].nunique()}")
print(f"- Số diễn viên khác nhau: {len(actor_counts)}")
print(f"- Số thể loại khác nhau: {len(genre_counts)}")


print(f"- Tổng doanh thu toàn bộ: ${total_revenue:,.0f}")
print(f"- Doanh thu trung bình: ${df['revenue'].mean():,.0f}")
print(f"- Tổng ngân sách: ${df['budget'].sum():,.0f}")
print(f"- Tổng lợi nhuận: ${df['profit'].sum():,.0f}")

print("\nCÁC FILE ĐÃ TẠO:")
print("1. movies_sorted_by_release_date.csv - Phim sắp xếp theo ngày phát hành")
print("2. high_rated_movies.csv - Phim có đánh giá > 7.5")
