import java.util.*;

class fibo{
	public static void main(String args[])
	{  
  		int n=10;
 		int result=fiboprint(n);
		/*System.out.println(result);*/
	}
	static int fiboprint(int n)
	{
		int a=0;
		int b=1;
		int c;
		System.out.println(a);
		System.out.println(b);
		for(int i=0;i<n-2;i++)
		{
			c=a+b;
			System.out.println(c);
			a=b;
			b=c;
		}
		return b;
	}
 
}