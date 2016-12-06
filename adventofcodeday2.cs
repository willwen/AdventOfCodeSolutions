using System;
using System.Collections.Generic;

public class Program
{
	//int [] negateUp = {1,2,3};   //in range from 0< x <=3
	//int [] negateDown = {7,8,9};  // in range from 7 <= x < 10
	//int [] negateLeft = {1,4,7}; // y = 3*x+1 where  0 <= x <=2  ; (y-1)%3 reverse and see if x is whole number
	//int [] negateRight = {3,6,9}; // input x %3==0 check
	public static bool isRedundantOP(int currentState, char direction){
		switch(direction){
			case ('U'):
				return (0<currentState && currentState<=3);
			case ('D'):
				return (7 <= currentState && currentState <10);
			case ('L'):
				return (currentState-1)%3==0;
			case ('R'):
				return (currentState%3==0);
			default:
				throw new Exception("unexpected input");
			
		}
	}
	public static void Main()
	{
		int currentState = 5;


		String args = @"LLULLLRLDLLLRLUURDDLRDLDURULRLUULUDDUDDLLLURRLDRRLDRRRLDUDLRDLRRDLLDUDUDUDRLUDUUDLLLRDURUDUULUDLRDUUUDUUDURLDUULLRDLULDUURUDRDDLDRLURLRURRDUURLRLUURURUUULLRLLULRUURLULURDLLRRUDLUDULDRDRLRULUURRDRULLRUUUDLRLDLUURRRURDLUDDRRUDRLUDRDLLLLLRULLDUDRLRRDDULDLRUURRRRRLDLDLRDURDRUUURDLRDDDDULURRRRDUURLULLLDLRULRDULRUDLRRLRDLLRLLLUDDLRDRURDDLLLLDUDRDLRURRDLRDDDLDULDRLRULUUDRRRUUULLLURRDDUULURULDURRLLULLDRURUUULRLRDRRUDRDRRDURRUUUULDRDDDUDLDDURLLRR
LDLRRRUURDLDDRLRRDLLULRULLLUDUUDUDLRULLDRUDRULLDULURDRDDLRURDDULLLLDLRDRDRDDURLURLURLUDRDDRDULULUDDRURRDLLDUURDRDDLRLLURRDLRDDULDLULURDRDLUDRRUUDULLULURRDUDRUUUDRULDLDURLRRUDURLDLRRUURRRURDLUDRLDUDRRUDUURURUDDUUDRDULRDLUDRRRLDRURLLRDDDLUDRDUDURDDDRRDDRRRLLRRDDLDDLRUURRURDLLDRLRRDLLUDRRRURURLRDRLLRLRLRULLRURLDLRRULLRRRDULUUULDRDLLURDDLDLRDRLUUDLLUDDLDRRLDLRUDRUDLLUURLLULURUDUDRLULLUDRURDDLDLDDUDLRDDRRURLRLLUDDUDRUURRURRULDRLDDRLLRRLDDURRDLDULLLURULLLRUURLRRRRUUULRLLLURRLRLRUDRDUUUDUUUDDLULLDLLLLDLDRULDRUUULDDDLURLDLRLULRUDDDDURDDLU
RURLURRDLDULLULDDDLRUULLUURLRUDRUDRRUDDLDDDDRRDLRURLRURLDDDUDDUURRDRULDRRRULRDRDDLRUDULRLURDUUDRRLDLRDRURDLDRRRRDRURUUDDDLLRDRDUDUDUDLLULURULRRLRURUULUULDDDDURULRULLRUDUURLURDUDLUDLUDRLLDUUDUULRLRLUUDRDULDULRURDRRRULRUDLRURDDULUDULLRLRURURUULLULDRURLLRRUUDDUUURRDLURUURULRDRRDDUDULRDDLUDLURURUURDRULLRDDLLRDDLDRDUDRRDLUURRLRLUURRULUDURLDDRLLURRDDDLDDRURULLDDRLUDDLRLURDUDULLRDULLLDLLUDDRUDRUDDUUDRDRULRL
RLRDRDULULUDLUDRDRLUDLDLLUDURULDDDUDLRURLLRLRLDLDRLDURDLRRURLULLULURLLDRRDRLUDRLRDLLULRULURRURURUULRDUDLLRDLRRRRRLUURDRRRDLRUDLLDLLDLRUUUDLLLDDDLRDULLRUUDDRLDDURRRDLRLRLDDDDLRDRULLUURUUDRRLLRLLRDDLLRURRRRDRULRRLLRLLLRLDRRLDDDURRURLDURUURRLRLRLDRURULLRLRUDLDUURDLLRLDLURUUUDLLRDRDDDDDDRLDRRRLRRRRURUDLDDRDLLURUDLRRLDDDLUDUDUULRDULULUDDULUUDLLLLRLDDUUULRLRDULURDURRRURRULURRRDRDLDDURDLURUDURRRDDRLRLUDLUDDLUULLDURLURDDUDDLRUUUDRLLDRURL
ULUDLLUDDULRUURDRURDUDUDLUURDDDRRLUDURURDRURRLDRDURLRLLRRDDRRDRRRUULURUDURUDULRRRRDDLDURRLRRDUDDDRLLLULDRLRLURRDUURDURRRURRDLUDUDDRLDLURRRDDRLLRDRDDRDURRRRLURRLUDDURRULRUDUDULDRUDDRULLUUULDURRRLDRULLURULLRUDLDUDDLDULDLUUDRULULDLLDRULLRUULDUDUUDRLRRLDLUULUDLLDDRLRRDDLLURURDULRRDDRURDRLRLULDLDURULLUUUDURURDLDUDDDDUUULUDLUURRULLDLRLURDLURLRLDDURRLDDRRRDUUULLUULDLLDLLDDRLRRUDLULDRLULDULULRRLRULUUURURUUURDUUDDURLLUDDRLRDDLUURRUULRDLDDRLULUULRDRURLUURDRDUURUDLRR";
		//String args = " L2, L3, R3";
		String [] directions = args.Split('\n');
		List<char> bathroomCode = new List <char> ();
		foreach (String input in directions){
			//Console.WriteLine("L:"+ input);
			foreach (char c in input){
				//Console.WriteLine("c:"+c);
				//remove redudant moves:
				if(!Program.isRedundantOP(currentState, c)){
					//define state machine
					switch (currentState){
						case (1):
							if(c == 'U'){
								throw new Exception ("isRedundantOP should have caught this");
							}
							else if(c == 'D'){
								currentState = 4;
							}
							else if(c == 'L'){
								throw new Exception ("isRedundantOP should have caught this");
							}
							else if(c == 'R'){
								currentState = 2;
							}
						break;
						case (2):
						if(c == 'U'){
							throw new Exception ("isRedundantOP should have caught this");
						}
						else if(c == 'D'){
							currentState = 5;
						}
						else if(c == 'L'){
							currentState = 1;
						}
						else if(c == 'R'){
							currentState = 3;
						}
						break;
						case (3):
						if(c == 'U'){
							throw new Exception ("isRedundantOP should have caught this");
						}
						else if(c == 'D'){
							currentState = 6;
						}
						else if(c == 'L'){
							currentState = 2;
						}
						else if(c == 'R'){
							throw new Exception ("isRedundantOP should have caught this");
						}
					break;
						case (4):
						if(c == 'U'){
							currentState = 1;
						}
						else if(c == 'D'){
							currentState = 7;
						}
						else if(c == 'L'){
							throw new Exception ("isRedundantOP should have caught this");
						}
						else if(c == 'R'){
							currentState = 5;
						}
					break;
						case (5):
						if(c == 'U'){
							currentState = 2;
						}
						else if(c == 'D'){
							currentState = 8;
						}
						else if(c == 'L'){
							currentState = 4;
						}
						else if(c == 'R'){
							currentState = 6;
						}
					break;
						case (6):
						if(c == 'U'){
							currentState = 3;
						}
						else if(c == 'D'){
							currentState = 9;
						}
						else if(c == 'L'){
							currentState = 5;
						}
						else if(c == 'R'){
							throw new Exception ("isRedundantOP should have caught this");
						}
					break;
						case (7):
						if(c == 'U'){
							currentState = 4;
						}
						else if(c == 'D'){
							throw new Exception ("isRedundantOP should have caught this");
						}
						else if(c == 'L'){
							throw new Exception ("isRedundantOP should have caught this");
						}
						else if(c == 'R'){
							currentState = 8;
						}
					break;
						case (8):
						if(c == 'U'){
							currentState = 5;
						}
						else if(c == 'D'){
							throw new Exception ("isRedundantOP should have caught this");
						}
						else if(c == 'L'){
							currentState = 7;
						}
						else if(c == 'R'){
							currentState = 9;
						}
					break;
						case (9):
						if(c == 'U'){
							currentState = 6;
						}
						else if(c == 'D'){
							throw new Exception ("isRedundantOP should have caught this");
						}
						else if(c == 'L'){
							currentState = 8;
						}
						else if(c == 'R'){
							throw new Exception ("isRedundantOP should have caught this");
						}
					break;
						
					}//end case
				}//end char for
				
			}//end if
			Console.WriteLine(currentState);
		}//end line for
		
		
	}//end main
}//end class def