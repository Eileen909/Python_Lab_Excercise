from module_ListFunction import list_max, list_min, list_sum, list_avg, list_median

def main():
    lst1 = [x for x in range(1, 21)]
    print("1st list created using List Comprehensions is", lst1)
    print("Maximum value in the list:", list_max(lst1))
    print("Minimum value in the list:", list_min(lst1))
    print("Sum of all the elements in the list:", list_sum(lst1))
    print("Average of the list:", list_avg(lst1))
    print("Median of the list:", list_median(lst1))

    lst2 = [x**3 for x in range(1, 21)]
    print("\n2nd list created using List Comprehensions is", lst2)
    print("Maximum value in the list:", list_max(lst2))
    print("Minimum value in the list:", list_min(lst2))
    print("Sum of all the elements in the list:", list_sum(lst2))
    print("Average of the list:", list_avg(lst2))
    print("Median of the list:", list_median(lst2))

    lst3 = [x for x in range(1, 21) if x % 2 != 0]
    print("\n3rd list created using List Comprehensions is", lst3)
    print("Maximum value in the list:", list_max(lst3))
    print("Minimum value in the list:", list_min(lst3))
    print("Sum of all the elements in the list:", list_sum(lst3))
    print("Average of the list:", list_avg(lst3))
    print("Median of the list:", list_median(lst3))

if __name__ == "__main__":
    main()
