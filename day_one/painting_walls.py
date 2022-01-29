def painting_walls(wall_size):
    litres_needed = wall_size / 3
    buckets_needed = litres_needed / 18
    total_price = buckets_needed * 80
    return (buckets_needed, total_price)


print(painting_walls(54))
