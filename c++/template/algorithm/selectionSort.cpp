void selectionSort(int *first, int *last, bool (*comp)(int, int))
{
    for (int *i = first; i < last; i++)
    {
        for (int *j = first; j < i; j++) 
        {
            if (comp(*i, *j)) swap(*i, *j);
        }
    }
}
