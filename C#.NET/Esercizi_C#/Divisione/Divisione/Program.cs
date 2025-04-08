Console.Write("dividendo: ");
int a = int.Parse(Console.ReadLine());

Console.Write("divisore: ");
int b = int.Parse(Console.ReadLine());

int qi = a / b;
int r = a % b;
double qr = (double)a / b;

Console.WriteLine("{0}/{1}", a, b);
Console.WriteLine("Quoziente intero: {0}", qi);
Console.WriteLine("resto: {0}",r);
Console.WriteLine("Quoziente reale: {0}",qr);
