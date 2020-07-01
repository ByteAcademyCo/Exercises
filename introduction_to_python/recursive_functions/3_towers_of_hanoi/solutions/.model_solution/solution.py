def tower_of_hanoi(n , from_rod, to_rod, aux_rod):
    return 1 if n == 1 else 1 + tower_of_hanoi(n-1, from_rod, aux_rod, to_rod) + tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)
