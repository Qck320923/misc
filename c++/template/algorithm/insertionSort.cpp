void insertionSort(int *first, int *last, bool (*comp)(int, int))
{
    for (int *i = first + 1; i < last; i++)
    {
        int *j = i, tmp = *i;
        while (!(*(j - 1) < tmp))
        {
            *j = *(j - 1);
            j--;
            if (j == first) break;
        }
        *j = tmp;
    }
}
