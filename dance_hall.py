import math;

length = float(input())
weight = float(input())
wardrobe_side = float(input())

room_area = (length * 100) * (weight * 100);
wardrobe_size = ((wardrobe_side * 100) * (wardrobe_side * 100));
bench_size = room_area / 10;
empty_space = room_area - wardrobe_size - bench_size;

danceres_num = empty_space / (40 + 7000);
print(math.floor(danceres_num))
