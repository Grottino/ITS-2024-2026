//dato in input un carattere rappresentabile 
//visualizzare la sua posizione in ascii standard

Console.WriteLine("Inserisci un carattere da tastiera: ");
char c = char.Parse(Console.ReadLine());

int posizione = (int)c;
Console.WriteLine("Il carattere {0} è in posizione ASCII: {1}", c,posizione);