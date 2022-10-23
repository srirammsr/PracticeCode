public class vcount{
	public static void main(String[] args)
	{
		String s="There are more than 10 lines of code";
		int counts=vowels(s);
		System.out.println(counts);
	}
static int vowels(String str)
{
	int vowelcount=0;
        for(int i=0;i<str.length();i++)
	     switch(str.charAt(i))
	     {
		case 'a' :
                case 'A' :
                case 'e':
                case 'E' :
                case 'i' :
                case 'I' :
                case 'o' :
                case 'O' :
                case 'u' :
                case 'U' :
                    vowelcount+=1;
                    continue;
              }
	   
	 return vowelcount;
   }
}