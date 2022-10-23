import javax.lang.model.util.ElementScanner6;

public class compare {
    public static void main(String[] args) 
    {
     int a=10;int b=11;int c= 11;
     if(a>b)
        if(a>c)
            System.out.println(a);
        else
            System.out.println(c);
     else if (b>c)
        System.out.println(b);
     else 
        System.out.println(c);

    
        
    }
}
