import os
import json

cwd_path = os.getcwd()
file_path = "files"



def read_data(file_name, key="ordered_numbers"):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, str), sequential data
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), mode="r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def binary_search(seq, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param seq: (list): list of numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return None
def recursive_binary_search(arr, target, left, right):
    if right >= left:
        mid = (right + left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr, target, left, mid - 1)
        elif arr[mid] > target:
            return recursive_binary_search(arr, target, mid + 1, right)

# print(recursive_binary_search([1,2,3,4,5,6,7,8,9,10],4,0,10))



def main(file_name, number):
    sequence = read_data(file_name, key="ordered_numbers")
    left = 0
    right = len(sequence)
    rekur = recursive_binary_search(sequence,number,left,right)
    # # iterative binary search
    # binary_search(sequence, number)
    return rekur

if __name__ == "__main__":
    my_file = "sequential.json"
    my_number = 90
    main(my_file, my_number)
