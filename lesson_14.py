def get_shift_rewport(ok_pieces, rejected_pieces):
    #1. Variable
    total = ok_pieces + rejected_pieces
    # 2. Variable
    efficiency = (ok_pieces / total) * 100
    return total, efficiency
total_final, porcentaje = get_shift_rewport(250, 40)
print(f"The total pieces produced are: {total_final}")
print(f"The efficiency of the shift is: {porcentaje:.2f}%")