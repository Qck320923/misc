int *partition(int *first, int *last, bool (*comp)(int, int)) {
    int *i = first, *j = last;
    while (i < j) {
        while (i < j && comp(*i, *j)) j--;
        if (i < j)
		{
            swap(*i, *j);
            i++;
        }
        while (i < j && comp(*i, *j)) i++;
        if (i < j)
		{
            swap(*i, *j);
            j--;
        }
    }
    return i;
}
void quickSort(int *first, int *last, bool (*comp)(int, int)) {
    if (first >= last) return;
    else
	{
        int *pivot = partition(first, last, comp);
        quickSort(first, pivot - 1, comp);
        quickSort(pivot + 1, last, comp);
    }
}
