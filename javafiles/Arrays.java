import java.util.ArrayList;

public class Arrays{

    public static void main(String[] args){
        ArrayList<String> v1=new ArrayList<String>();
        v1.add("Fruits");
        v1.add("Vegetables");
        v1.add("Flowers");
        System.out.println(v1);
        System.out.println("No. of elements of v1 " + v1.size());
        v1.set(1,"Juices");
        System.out.println(v1);
    }
}