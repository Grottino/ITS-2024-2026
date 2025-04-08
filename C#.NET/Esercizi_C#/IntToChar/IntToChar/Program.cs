//dato in input un numero intero [32,127] rappresentabile 
//visualizzare il carattere corrispondente in ascii standard

Console.WriteLine("Inserisci un numero intero da tastiera [32,127]: ");
int posizione = int.Parse(Console.ReadLine());

 char c = (char)posizione;
Console.WriteLine("La posizione ASCII: {0} corrisponde al carattere {1}", posizione, c);