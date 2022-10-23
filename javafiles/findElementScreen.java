import java.util.*;

class FindElementScreen {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];

        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        int x = sc.nextInt();

        int result = findElement(n, arr, x);

        System.out.println(result);

    }

    // TODO: Implement this method
    static int findElement(int n, int[] arr, int x) {
	int i=0;
	for(i=0;i<n;i++)
	  { if(arr[i]==x) break;}
	return arr[i];
    }
}
