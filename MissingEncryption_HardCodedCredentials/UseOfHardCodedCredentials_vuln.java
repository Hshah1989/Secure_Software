import java.util.*;

/**
 * Hiren Shah
 * 4/12/21
 * User of Hard Coded Credentials
 * Vulnerable Code
 */


public class UseOfHardCodedCredentials_vuln {
	// method which checks if the password does not equal "Mew!". 
	public static int VerifyAdmin(String password) {
		if (!password.equals("Mew!")) {
			return(0);
		}

		//Diagnostic Mode
		return(1);
		}
	
	//Verifies the user password if the password is "Mew!", if it is not it will state invalid password.
	public static void main(String[] args) {
		System.out.println("Please Input the password: ");
		Scanner sc = new Scanner(System.in);
		String password = sc.nextLine();
		int successful = VerifyAdmin(password);
	
		if (successful == 1) {
			System.out.println ("This was a successful log in");
			
		}
		else {
			System.out.println("This was an invalid password");
		}
		
	
	}
}