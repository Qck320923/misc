#include <malloc.h>

void mergeSort(int *first, int *last, bool (*comp)(int, int))
{
	int n = last - first;
	int *tmp = (int*)malloc(sizeof(int) * n + 1);
	if (tmp == NULL) return;
	int gap = 1;
	while (gap < n)
	{
		for (int i = 0; i < n; i += 2 * gap)
		{
			int begin1 = i;
			int end1 = i + gap - 1;
			int begin2 = i + gap;
			int end2 = i + 2 * gap - 1;
			if (end1 >= n)
			{
				end1 = n - 1;
				begin2 = n;
				end2 = n - 1;
			}
			else if (begin2 >= n)
			{
				begin2 = n;
				end2 = n - 1;
			}
			else if (end2 >= n) end2 = n - 1;
			int j = begin1;
			while ((begin1 <= end1) && (begin2 <= end2))
			{
				if (comp(*(first + begin1), *(first + begin2)))
				{
					tmp[j++] = *(first + begin1);
					begin1++;
				}
				else
				{
					tmp[j++] = *(first + begin2);
					begin2++;
				}
			}
			while (begin1 <= end1)
			{
				tmp[j++] = *(first + begin1);
				begin1++;
			}
			while (begin2 <= end2)
			{
				tmp[j++] = *(first + begin2);
				begin2++;
			}
		}
		for (int i = 0; i < n; i++) *(first + i) = tmp[i];
		gap *= 2;
	}
	free(tmp);
}
