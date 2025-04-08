//Dati in input due numeri interi,
//calcolare la somma e visualizzare il risultato

//input 

Console.Write("Inserisci un numero intero: ");
string tmp = Console.ReadLine();
int a = int.Parse(tmp);

Console.Write("Inserisci un numero intero: ");
int b = int.Parse(Console.ReadLine());

//calcolo
int somma = a + b;
//output
Console.WriteLine(somma);