def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far > last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
        return furthest_reach_so_far >= last_index