planted = [2.43, 0.82, 1.68, 1.50, 1.41, 
           2.34, 2.05, 2.26, 3.13, 4.55]

cut = [5.47, 3.69, 4.47, 4.29, 3.37,
       4.35, 2.86, 4.32, 5.52, 3.88]

planted.append(3.03)
cut.append(2.89)

for item in planted:
    position = planted.index(item)
    total = planted[position] -  cut[position]
    total = round(total, 2)
    print(f"The net forest gain/loss for year {position+1} was {total}")