/*
Hiren Shah
SDEV 325 7380
4/23/2021
Professor Matthew L. Brown, Ph.D
Demonstrating Porous Defenses Final
CWE759-Vulnerable
Use of One_Way Hash without SALT
 */
import java.util.*;


public class OneWaySaltVuln {
	public static void main(String[] args) {
    	System.out.println("Enter a word to print out: ");
    	Scanner sc = new Scanner(System.in);
    	String str = sc.nextLine();
    	System.out.println(Hashed(str));
    	
		}
	
private static String Hashed(String str) {
	String result = "";
	for(int i=0; i<str.length(); i++) {
		result += Character.getNumericValue(str.charAt(i)) % 7;
		
	}
	return result;
		
	}
}