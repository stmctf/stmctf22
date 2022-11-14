# STMCTF'22 Final

## Soru İsmi:

`where is my drone?`

### Kategori:
 - `Coding`

### Soru:
```
TR:
Tarım alanında kullanılmak üzere bir drone üretilmiştir. Amacı ise tarım yapılan tarla üzerinde bulundurduğu kameralar sayesinde alanı tarayarak yetiştirilmekte olan ürünün görüntülerini almak ve detaylı bilgi üretmektir. Ürettiği bu bilgiyi ise yer istasyonu ile paylaşmaktadır. Ayrıca drone uzaktan yönlendirilmektedir.
	Bu drone’un poziyonu ve yer bilgisi x ve y koordinatlarının kombinasyonuyla ve 4 adet kardinal pusula yönleriyle belirtilmektedir. Örnek olarak drone’un pozisyonu 0,0,K olabilir ve bu koordinat düzleminin sol alt köşesinde ve yönü kuzeye bakıyor şeklindedir.
	Drone basit harfler ile komutları algılamaktadır. Bu harfler, ‘L’ (Sol), ‘R’ (Sağ) ve ‘M’ (ilerle) şeklindedir. ‘L’ ve ‘R’ komutları drone’u mevcut konumundan hareket ettirmeden sadece 90 derece sağa ya da sola çevirir. ‘M’ komutu ise yönünün baktığı doğrultuda bir birim ileri hareket ettirmektedir.Tek bir girdi olması halinde x Koordinat y Koordinat Yön arasında boşluk olacak şekilde yazılmalıdır. Birden fazla girdi olması halinde ilk girdinin çıktısı virgül ile ayrıldıktan sonra ikinci girdinin çıktısının eklenmesi beklenmektedir.

Girdi:
	İlk girdi satırı düzlemin sağ üst koordinatlarını belirler. Bu düzlemin genişliği bilgisini verir. Sol alt köşenin koordinatları ise 0,0 olarak kabul edilir.
	İkinci girdi Drone’a ait başlangıç konum ve pozisyon bilgisini vermektedir.
	Üçüncü satır ise sırasıyla yapması gereken komutların dizesini içermektedir.
Çıktı:
	Drone’a ait bulunduğu son koordinatları ve yönünün nereye baktığı bilgisini vermelidir.

Örnek:
Girdi:
5 5
1 2 K
LMLMLMLMM
3 3 D 
MMRMMRMRRM

Çıktı:
STMCTF{1 3 K,5 1 D}

EN:
A drone has been produced for use in agriculture. Its purpose is to scan the area with the cameras it has on the agricultural field, to take the images of the product being grown and to produce detailed information. It shares this information with the ground station. In addition, the drone is remotely steered.
The position and location of this drone are indicated by the combination of x and y coordinates and the 4 cardinal compass directions. For example, the position of the drone could be 0,0,K and it is in the lower left corner of the coordinate plane and its direction is facing north.
The drone detects commands with simple lines. These letters are 'L' (Left), 'R' (Right), and 'M' (forward). The 'L' and 'R' commands only turn the drone 90 degrees right or left without moving it from its current position. The 'M' command moves one unit forward in the direction its direction is facing.

Entry:
The first input line determines the upper-right coordinates of the plane. This gives the width of the plane. The coordinates of the lower left corner are accepted as 0.0.
The second input gives the initial position and position information of the drone.
The third line contains the string of commands it should do, in order.
Output:
It should give information about the last coordinates of the drone and its direction.

Example:
Input:
5 5
1 2 N
LMLMLMLMM
3 3 E 
MMRMMRMRRM

Output:
STMCTF{1 3 N,5 1 E}
```
---

## Çözüm:
```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace CTF
{
    public class ctf
    {
        static readonly string inputDroneFile = @"...\inputDroneFile.txt";
        static void Main(string[] args)
        {
            var formattedInput = PrepareInput();
            var result = AgricultureDrone(formattedInput.XBoundary, formattedInput.YBoundary, formattedInput.DroneList);
            writeOutput(result);
            Console.ReadKey();
        }

        public static FormattedInput PrepareInput()
        {
            int x = 0;
            int y = 0;
            List<Drone> droneList = new List<Drone>();

            if (File.Exists(inputDroneFile))
            {
                using (StreamReader file = new StreamReader(inputDroneFile))
                {
                    int counter = 0;
                    string ln;

                    while ((ln = file.ReadLine()) != null)
                    {
                        Console.WriteLine(ln);
                        if (counter == 0)
                        {
                            try
                            {
                                x = int.Parse(ln.Split(' ')[0]);
                                y = int.Parse(ln.Split(' ')[1]);
                            }
                            catch (Exception e)
                            {
                                throw new Exception("Invalid Boundaries. Exception Message: " + e.Message);
                            }
                        }
                        else
                        {
                            var fLine = ln.Split(' ');
                            ln = file.ReadLine();
                            if (ln == null)
                            {
                                throw new Exception("Invalid Movements For Drone: " + counter);
                            }
                            var sLineTrimmed = ln.Trim();
                            Console.WriteLine(sLineTrimmed);
                            var sLine = sLineTrimmed.Split(' ');
                            var drone = new Drone();

                            try
                            {
                                var position = new Position()
                                {
                                    X = int.Parse(fLine[0]),
                                    Y = int.Parse(fLine[1])
                                };
                                if (fLine[2].Length > 1 || string.IsNullOrWhiteSpace(fLine[2]))
                                {
                                    throw new Exception("Invalid Face of Position For Drone: " + counter);
                                }
                                position.Face = Char.ToLower(fLine[2][0]);
                                drone.Position = position;
                            }
                            catch (Exception)
                            {
                                throw new Exception("Invalid Positions For Drone: " + counter);
                            }

                            try
                            {
                                var movementString = sLine[0].ToLower();
                                List<char> movements = new List<char>();
                                movements.AddRange(movementString);
                                drone.Movements = movements;
                            }
                            catch (Exception)
                            {
                                throw new Exception("Invalid Movements For Drone: " + counter);
                            }

                            droneList.Add(drone);
                        }
                        counter++;

                    }
                    file.Close();
                    Console.WriteLine($"File has {counter - 1} drones.");
                }
            }

            return new FormattedInput { XBoundary = x, YBoundary = y, DroneList = droneList };
        }

        public static List<Drone> AgricultureDrone(int xBoundary, int yBoundary, List<Drone> drones)
        {
            var result = new List<string>();
            int index = 0;

            foreach (var item in drones)
            {
                if (item.Position.X > xBoundary || item.Position.Y > yBoundary)
                {
                    result.Add("Drone " + index + ". has invalid positions.");
                    continue;
                }

                foreach (var move in item.Movements)
                {
                    item.Position = ChangePosition(item.Position, Char.ToLower(move), xBoundary, yBoundary);
                }
                index++;
            }
            return drones;
        }

        public static Position ChangePosition(Position oldPosition, char movement, int xLimit, int yLimit)
        {
            if (movement == 'l' || movement == 'r')
            {
                oldPosition.Face = TurnFlow(oldPosition.Face, movement);
            }
            else if (movement == 'm')
            {
                if (oldPosition.Face == 'k')
                {
                    oldPosition.Y = oldPosition.Y == yLimit ? oldPosition.Y : oldPosition.Y + 1;
                }
                else if (oldPosition.Face == 'd')
                {
                    oldPosition.X = oldPosition.X == xLimit ? oldPosition.X : oldPosition.X + 1;
                }
                else if (oldPosition.Face == 'g')
                {
                    oldPosition.Y = oldPosition.Y == 0 ? oldPosition.Y : oldPosition.Y - 1;
                }
                else if (oldPosition.Face == 'b')
                {
                    oldPosition.X = oldPosition.X == 0 ? oldPosition.X : oldPosition.X - 1;
                }
            }
            return oldPosition;
        }

        public static char TurnFlow(char curDirection, char rotation)
        {
            if (curDirection == 'k' && rotation == 'l')
            {
                return 'b';
            }
            else if (curDirection == 'k' && rotation == 'r')
            {
                return 'd';
            }
            else if (curDirection == 'd' && rotation == 'l')
            {
                return 'k';
            }
            else if (curDirection == 'd' && rotation == 'r')
            {
                return 'g';
            }
            else if (curDirection == 'g' && rotation == 'l')
            {
                return 'd';
            }
            else if (curDirection == 'g' && rotation == 'r')
            {
                return 'b';
            }
            else if (curDirection == 'b' && rotation == 'l')
            {
                return 'g';
            }
            else if (curDirection == 'b' && rotation == 'r')
            {
                return 'k';
            }
            else
            {
                return curDirection;
            }
        }

        public static void writeOutput(List<Drone> drones)
        {
            Console.WriteLine($"Final positions of the drones: ");
            foreach (var item in drones)
            {
                Console.WriteLine(item.Position.X + " " + item.Position.Y + " " + char.ToUpperInvariant(item.Position.Face));
            }
        }

        public class FormattedInput
        {
            public int XBoundary { get; set; }
            public int YBoundary { get; set; }
            public List<Drone> DroneList { get; set; }
        }
        public class Drone
        {
            public Position Position { get; set; }
            public List<char> Movements { get; set; }
        }
        public class Position
        {
            public int X { get; set; }
            public int Y { get; set; }
            public char Face { get; set; }
        }
    }
}

```