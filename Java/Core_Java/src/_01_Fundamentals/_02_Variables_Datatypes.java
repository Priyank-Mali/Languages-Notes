package _01_Fundamentals;

public class _02_Variables_Datatypes {
	public static void main(String[] args) {
		
		// Variables: Variables are containers for storing data values.
		/*
		 * int
		 * String
		 * float
		 * char
		 * boolean
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
		System.out.println(myChar);
		
		// Identifiers:
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
		
	}
}
