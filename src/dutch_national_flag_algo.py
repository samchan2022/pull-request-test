"""
Algorithm Type: Array sorting with 0s,1s and 2s in a single pass
Explain: To separate three different groups
Time Complexity: O(n)

    0 0 1 1 1 ? ? ? ? 2 2
        |     |     |
        v     v     v
       Low   Mid   High

   To goal of the algo is to shrink this '?' region
   wrapped by Mid and High

   > Low starts at 1
"""

arr = [2, 0, 1, 1,  2, 1, 1, 0]

# Dutch national flag sort
def DNFS( arr ):
  arr_size = len(arr)
  low = 0
  high = arr_size - 1
  mid = 0
  count = 0
  while mid <= high:
    if arr[mid] == 0:
      arr[low], arr[mid] = arr[mid], arr[low]
      low = low + 1
      mid = mid + 1
    elif arr[mid] == 1:
      mid = mid + 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high = high - 1
  return arr

if __name__ == "__main__":
    print("Sorted Array:", DNFS(arr))
