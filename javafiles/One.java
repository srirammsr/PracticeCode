class One
{
	String studentClass;
	String studentName;
	char section;

	public One(String stuClass,String stuName,char sect)
	{
		studentClass=stuClass;
		studentName=stuName;
		section=sect;
	}


public static void main(String args[])
{
	One var1=new One("VI","Jyothika",'B');
	int i=5;

	switch(i){
		case 5:
			System.out.println("Value entered is less than 5");	
			break;
		case 11:
			System.out.println("Value entered is greater than 5");	
			break;
		case 20:
			System.out.println("Value entered is equal to 5");	
			break;
		default:
			System.out.println("Something else");
			break;
	}

}
}