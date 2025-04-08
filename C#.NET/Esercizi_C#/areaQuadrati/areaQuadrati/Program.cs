// calcolare l'area del quadrato 
// r* radice ^2 dell'area

Console.Write("Quanto misuta un lato? ");
double lato = double.Parse(Console.ReadLine());

//calcolo
double perimetro = lato * 4;
double area = lato * lato;
double diagonale = lato * Math.Sqrt(2);

Console.WriteLine("Il perimetro misura: {0} \nl'area misura: {1} \nla diagonale misura: {2}S", perimetro, area, diagonale);

