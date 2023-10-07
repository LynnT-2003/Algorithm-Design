#include <iostream>
using namespace std;

typedef long long Long;
typedef long long Size;

Long inversionCount = 0;

void mergeAndCountInversions(Long leftArr[], Long rightArr[], Long mergedArr[], Size leftSize, Size rightSize)
{
  Size leftIndex = 0, rightIndex = 0, mergedIndex = 0, rightInversions = 0;

  while (leftIndex < leftSize && rightIndex < rightSize)
  {
    if (leftArr[leftIndex] <= rightArr[rightIndex])
    {
      mergedArr[mergedIndex++] = leftArr[leftIndex++];
    }
    else
    {
      mergedArr[mergedIndex++] = rightArr[rightIndex++];
      rightInversions += (leftSize - leftIndex);
    }
  }

  while (leftIndex < leftSize)
  {
    mergedArr[mergedIndex++] = leftArr[leftIndex++];
  }

  while (rightIndex < rightSize)
  {
    mergedArr[mergedIndex++] = rightArr[rightIndex++];
  }

  inversionCount += rightInversions;
}

void mergeSortAndCountInversions(Long arr[], Size size)
{
  if (size <= 1)
  {
    return;
  }

  Size mid = size / 2;
  Long leftArr[mid], rightArr[size - mid];

  for (Size i = 0; i < mid; ++i)
  {
    leftArr[i] = arr[i];
  }

  for (Size i = mid; i < size; ++i)
  {
    rightArr[i - mid] = arr[i];
  }

  mergeSortAndCountInversions(leftArr, mid);
  mergeSortAndCountInversions(rightArr, size - mid);

  mergeAndCountInversions(leftArr, rightArr, arr, mid, size - mid);
}

int main()
{
  Size n, t;
  cin >> t;

  while (t--)
  {
    cin >> n;
    inversionCount = 0;
    Long arr[n];

    for (Size i = 0; i < n; ++i)
    {
      cin >> arr[i];
    }

    mergeSortAndCountInversions(arr, n);
    cout << inversionCount << endl;
  }

  return 0;
}
