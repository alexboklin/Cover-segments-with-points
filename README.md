Given n segments, provide a minimal set of points such that each segment contains at least one of these points. 
The first input line contains 1 &le; <i>n</i> &le; 100 segments.
Each successive input line (n lines total) contains two numbers  0 &le; <i>l</i> &le; <i>r</i> &le; 10<sup>9</sup> -- segment's endpoints.
The task is to output the optimal amount of m points and these m points themselves. 
If there are several such points sets, output any of those.

<b>Sample Input 1:</b>
3
1 3
2 5
3 6
<b>Sample Output 1:</b>
1
3 

<b>Sample Input 2:</b>
4
4 7
1 3
2 5
5 6
<b>Sample Output 2:</b>
2
3 6 
