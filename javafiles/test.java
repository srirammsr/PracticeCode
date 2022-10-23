import java.util.Arrays;

public class test
{
    public test()
    {

    }
    public String[] elements()
    {
        String[] countries={"India","USA","Canada"};
        return countries;
    }

public static void main(String[] args)
    {
        test t1=new test();
        String s[]=t1.elements();
        System.out.println(Arrays.toString(s));
    }
}