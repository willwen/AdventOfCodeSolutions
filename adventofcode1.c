using System;
//using System.Text.RegularExpressions.Regex;
	
public class Program
{
	public static void Main()
	{
		int x = 0;
		int y = 0;
		String direction = "north";
		String args = " R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3";
		//String args = " L2, L3, R3";
		String [] directions = args.Split(',');
		foreach (String input in directions){
			char dir = input[1];
			int steps;
			
			string stepsString = input.Substring(2,input.Length-2);
			Console.WriteLine(stepsString);

			steps = Int32.Parse(stepsString);
	
			switch (direction){
				case ("north"):
					if(dir == 'L'){
						x -= steps;
						direction = "west";
					}
					else if(dir == 'R'){
						x += steps;
						direction = "east";
					}
				break;
				case ("south"):
				if(dir == 'L'){
						x += steps;
						direction = "east";
					}
					else if(dir == 'R'){
						x -= steps;
						direction = "west";
					}
				break;
				case ("east"):
				if(dir == 'L'){
						y += steps;
						direction = "north";
					}
					else if(dir == 'R'){
						y -= steps;
						direction = "south";
					}
				break;
				case ("west"):
				if(dir == 'L'){
						y -= steps;
						direction = "south";
					}
					else if(dir == 'R'){
						y += steps;
						direction = "north";
					}
				break;	
			}
		}
		
		Console.WriteLine(x + " " + y);
		
	}
}