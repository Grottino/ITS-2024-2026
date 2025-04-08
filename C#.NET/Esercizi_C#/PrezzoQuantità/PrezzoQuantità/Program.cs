Console.Write("inserisci il prezzo: ");
double prezzo = double.Parse(Console.ReadLine());

Console.Write("inserisci la quantità: ");
int quantita = int.Parse(Console.ReadLine());

Console.Write("inserisci lo sconto: ");
int sconto = int.Parse(Console.ReadLine());


double totale = prezzo * quantita;
double totaleScontato = totale * sconto / 100;
double prezzoScontato = totale - totaleScontato;


Console.WriteLine("\nIl totale è: {0}",totale);
Console.WriteLine("Il totale scontato è: {0}",totaleScontato);
Console.WriteLine("Il prezzo scontato è: {0}",prezzoScontato);
