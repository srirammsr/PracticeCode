import java.util.ArrayList;

public class loops{

    public static void main(String[] args)
    {
        String[] movies={"movie 1","movie 17","movie 12","movie 21","movie 41","movie 45"};
        ArrayList<String> mv=new ArrayList<String>();
        mv.add("Chairs");mv.add("Desks");mv.add("ABC");
        for (String s:movies)
            System.out.println(s);
            System.out.println(mv.get(2));
            String myname="Sriram murthy";
            System.out.println(myname.charAt(2));//extracting a character at a particular position.
    }
}