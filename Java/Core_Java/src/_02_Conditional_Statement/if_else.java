package _02_Conditional_Statement;

public class if_else {
	public static void main(String[] args) {
		int time = 10;
		
		if(time > 12) {
			System.out.println("It's night");
		}else if(time > 5) {
			System.out.println("It's morning");
		}
		
//		ternary operator  : shorthand if-else
		
//		variabble = (condition) ? (expressionTrue) : expressionFalse
		
		int num1 = 100;
		int num2 = 200;

		
		String res = num1 > num2 ? ("Num1 is greate than Num2") : ("Num1 is lesser than Num2");
		System.out.println(res);
	}
} 
