class Solution {
public:
    int sort_and_count(vector<int>::iterator begin, vector<int>::iterator end) {
        if (end - begin <= 1)
            return 0;
        auto mid = begin + (end - begin) / 2;
        int count = sort_and_count(begin, mid) + sort_and_count(mid, end);
        for (auto i = begin, j = mid; i != mid; ++i) {
            while (j != end and *i > 2L * *j)
                ++j;
            count += j - mid;
        }
        inplace_merge(begin, mid, end);
        return count;
    }

    int reversePairs(vector<int>& nums) {
        return sort_and_count(nums.begin(), nums.end());
    }
};

// 繁琐版，官方题解
// class Solution {
// public:
//     void merge(vector<int>& arr, int start, int mid, int end) {
//         int lenl = mid - start + 1;
//         int lenr = end - mid;
//         int l[lenl], r[lenr];

//         for (int i = 0; i < lenl; i++)
//             l[i] = arr[start + i];
//         for (int j = 0; j < lenr; j++)
//             r[j] = arr[mid + 1 + j];

//         int i = 0, j = 0;
//         for (int k = start; k <= end; k++) {
//             if (j >= lenr || (i < lenl && l[i] <= r[j]))
//                 arr[k] = l[i++];
//             else
//                 arr[k] = r[j++];
//         }
//     }


//     int mergeSort(vector<int>& arr, int start, int end) {
//         if (start < end) {
//             int mid = (start + end) / 2;
//             int count = mergeSort(arr, start, mid) + mergeSort(arr, mid + 1, end);

//             int j = mid + 1;
//             for (int i = start; i<= mid; i++) {
//                 while (j <= end && arr[i] > arr[j] * 2LL)    j++;
//                 count += j - (mid + 1);
//             }
//             merge(arr, start, mid, end);
//             return count;
//         }
//         else
//             return 0;
//     }


//     int reversePairs(vector<int>& nums) {
//         return mergeSort(nums, 0, nums.size() - 1);
//     }
// };

