import java.util.*;

 /**
 * Hiren Shah
 * 4/12/21
 * Use of Hard Coded Credentials
 * Mitigated Code
 * 
 */
 
//public class UseOfHardCodedCredentials_Mit{
	
	// method which checks if the password does not equal "Mew!". 
	//public static int VerifyAdmin(String password) {
	//	if (!password.equals("Mew!")) {
	//		return(0);
	//	}
		
		//Diagnostic Mode
		//return(1);
	//}
	
	public static int checkingPasswordService(String password) {
		System.out.println("Send password to server");
		System.out.println("Server side is performing password verification");
		System.out.println("Server sent back the result which indicates if it is successful or not");
		
		Random rn = new Random();
		int result = rn.nextInt(2);
		
		return result;
	} 
	
	//Verifies the user password if the password is "Mew!", if it is not it will state invalid password.
	public static void main(String[] args) {
		
		System.out.println("Please Input the password: ");
		Scanner sc = new Scanner(System.in);
		String password = sc.nextLine();
		//int successful = VerifyAdmin(password);
		
		for (int i=0;i<20;i++) {
		int	successful = checkingPasswordService(password);
	
			if (successful == 1) {
				System.out.println ("This was a successful log in\n");
				
			}
			else {
				System.out.println("This was an invalid password\n");
			}
		}
		
		
	
	}
}