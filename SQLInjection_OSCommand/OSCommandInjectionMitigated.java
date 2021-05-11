import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
/**
 Hiren Shah
 3/16/21
 OS Command Injenction Mitigated
 */
public class OSCommandInjectionMitigated {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		String ipAddress = "";
		
		System.out.println("This is an example of OS Command Injection");
		System.out.println("This app performs pings to ip addresses specified by the USer");
		
		// -- this  part is vulnerable to OS Command Injection --
		System.out.println("Eneter ip address to ping (ex. 8.8.8.8): ");
		ipAddress = scanner.nextLine();
		
		//this part mitigates the OS command Injection through validation
		if (!isValidInput(ipAddress)) {
			while(!isValidInput(ipAddress)) {
				System.out.println("The address given was invalid. Try again.");
				// -- this  part is vulnerable to OS Command Injection --
				System.out.println("Eneter ip address to ping (ex. 8.8.8.8): ");
				ipAddress = scanner.nextLine();
			}
		} // code mitigations
		
		Runtime runtime = Runtime.getRuntime();
		try {
			Process exec = runtime.exec("cmd.exe /C ping " + ipAddress);
			System.out.println("------ Results -------");
			
			BufferedReader stdInput = new BufferedReader(new 
				     InputStreamReader(exec.getInputStream()));

			BufferedReader stdError = new BufferedReader(new 
				     InputStreamReader(exec.getErrorStream()));
			
			// read output of command
			String s = null;
			while ((s = stdInput.readLine()) != null) {
			    System.out.println(s);
			}
			
			// Read any errors from the attempted command
			System.out.println("\nHere is error from the command (if any):\n");
			while ((s = stdError.readLine()) != null) {
			    System.out.println(s);
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} // catch
    	
    	
	}// main
	
	/*
	 * if input contains anything other than numbers, letters, and periods, colons
	 * since colons and periods are used in ip addresses
	 */
	public static boolean isValidInput(String input){
		char token;
		
		for(int i = 0; i < input.length();i++) {
			token = input.charAt(i);
			if(!((token >= 48 && token <= 58) || (token >= 65 && token <= 90) ||
					(token >= 97 && token <= 122) || token == 46)) {
				return false;
			} // if token != 0-9, a-z, A-z, :, . it is invalid
		}
		
		return true;
	}
	
	
} // IntegerOverflowVulner