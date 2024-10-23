package _01_Fundamentals;

public class _02_Variables_Datatypes {
	public static void main(String[] args) {
		
		// Variables: Variables are containers for storing data values. ==================================
		/*
		 * int
		 * String
		 * float    float num = 12.3f
		 * double   double num = 23.56d
		 * char 
		 * boolean  boolean isValue = false 
		 * 
		 * */
		int number = 10;
		String name = "priyank";
		
		int myNum;
		myNum = 12;
		
//		overwrite existing values, use the final keyword 
		
		final int myNumber = 13;
//		myNumber = 20;
		
		System.out.println(number);
		System.out.println(name);
		System.out.println(myNum);
		
		char myChar = '1';
		char jhas = 65;
		System.out.println(jhas);
		System.out.println(myChar);
		
		// Identifiers: =================================================================================
		// all java variables must be identified by unique names these name called as identifiers
		
		
		String studentName = "priyank";
		int studentId = 201;
		int studentAge = 99;
		float studentFees = 20.45f;
		char studentGrade = 'c';
		
		System.out.println("Name : "+ studentName);
		System.out.println("ID : "+ studentId);
		System.out.println("Age : "+ studentAge);
		System.out.println("Fees : "+ studentFees);
		System.out.println("Grade : "+ studentGrade);
		
		// non-premitive datatype ==============================================================
		
		// String
		// Arrays
		// Classes
		
		
		// Type Casting ======================================================================== 
		
		/*
		 * In java there are two types of casting
		 * 
		 * 1.) Widening Casting (implicit - automatically)  converting a smaller type to a larger type size
		 * 		
		 * 		byte -> short -> char -> int -> long -> float -> double
		 * 
		 * 2.) Narrowing Casting (explicit - manually)   converting a larger type to a smaller size type
		 * 
		 * 		double -> float -> long -> int -> char -> short -> byte
		 * 

		 */
		int a = 12;
		double b = a;
		
		System.out.println(b);
		
		double c = 12.3d;
		int d = (int) c;
		System.out.println(d);
		
	}
}
