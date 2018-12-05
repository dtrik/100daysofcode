import math

def triplets_with_sum(sum_of_triplet):
    triplet_list = set()
    num_added = set()
    for a in range(1, int(sum_of_triplet/2)+1):
        for b in range(a+1, int(sum_of_triplet/2)+1):
            if a in num_added and b in num_added:
                continue
            else:
                c = sum_of_triplet - (a+b)
                if is_triplet((a,b,c)):
                    num_added.update([a,b,c])
                    triplet_list.add((a,b,c))
        #print(a,b,c)
    return(triplet_list)

def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    t = list(triplet)
    t.sort()
    a,b,c = t
    if c**2 == a**2 + b**2 and (a*b*c > 0):
        return True
    else:
        return False

#print(is_triplet([3,4,5]))
print(triplets_with_sum(1001))