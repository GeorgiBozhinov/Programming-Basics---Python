length = float(input())
width = float(input())
heigth = float(input())
percent = float(input())

aquarium_volume = length * width * heigth;
litters = aquarium_volume * 0.001;
percent_sum = percent * 0.01;
end_sum = litters * (1 - percent_sum);

print("%.3f" % end_sum)
