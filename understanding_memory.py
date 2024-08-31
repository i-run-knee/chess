import copy

def print_memory_locations(title, original, copy1, copy2):
    print(f"\n{title}")
    print("Original list memory location:", id(original))
    print("Shallow copy memory location:", id(copy1))
    print("Deep copy memory location:", id(copy2))
    
    print("\nChecking individual elements within the lists:")
    for i in range(len(original)):
        print(f"Element {i} in original list: {id(original[i])}")
        print(f"Element {i} in shallow copy: {id(copy1[i])}")
        print(f"Element {i} in deep copy: {id(copy2[i])}")
        print("")

def main():
    # Create an original list containing mutable objects (lists within a list)
    original_list = [[1, 2], [3, 4], [5, 6]]

    # No Copy (Reference Assignment)
    no_copy_list = original_list

    # Shallow Copy
    shallow_copy_list = copy.copy(original_list)

    # Deep Copy
    deep_copy_list = copy.deepcopy(original_list)

    # Print memory locations
    print_memory_locations("After Shallow and Deep Copy:", original_list, shallow_copy_list, deep_copy_list)

    # Modify the original list to see the effect on copies
    original_list[0][0] = 99

    print("\nAfter modifying the original list:")
    print_memory_locations("After Modification:", original_list, shallow_copy_list, deep_copy_list)

if __name__ == "__main__":
    main()
