public class taxcalc
{
	double TotalIncome;
	final double firstTaxSlab =0.12;
	public taxcalc(double AnnualIncome)
	{
		TotalIncome=AnnualIncome;
	}
	public void calculateTAX()
	{
		System.out.println(TotalIncome);
		double tmpvar;
		if(TotalIncome<=450000)
			System.out.println("Not under tax slab");
		else
		{
			tmpvar=TotalIncome-450000;
			System.out.println("Tax you should pay is  "+firstTaxSlab*tmpvar);		
		}
	}
	
	public static void main(String[] args)
	{
		taxcalc emp1=new taxcalc(500000);
		emp1.calculateTAX();
	}

}
