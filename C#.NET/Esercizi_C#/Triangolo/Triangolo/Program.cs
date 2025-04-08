// calcolare l'area del quadrato 
// r* radice ^2 dell'area

Console.Write("Inserisci l'imponibile: ");
double Imponibile = double.Parse(Console.ReadLine());

int iva = 22;

//calcolo
double calcoloIVA = Imponibile * iva / 100;
double totale = calcoloIVA + Imponibile;

//output
string msg = $"Iva({iva}%): {calcoloIVA} euro"+
    $"\nTotale: {totale} euro";

Console.WriteLine(msg);
