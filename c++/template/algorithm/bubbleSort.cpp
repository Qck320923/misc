void bubbleSort(int *first, int *last, bool (*comp)(int, int))
{
    for (int *i = first, sub = 0; i < last - 1; i++, sub++)
    {
        for (int *j = first; j < last - sub - 1; j++) 
        {
            if (comp(*(j + 1), *j)) swap(*(j + 1), *j);
        }
    }
}
