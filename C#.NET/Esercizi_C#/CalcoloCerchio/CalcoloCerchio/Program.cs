// calcolare l'area del quadrato 
// r* radice ^2 dell'area

Console.Write("Quanto misuta un raggio? ");
double raggio = double.Parse(Console.ReadLine());

//calcolo
double diametro = raggio * 4;
double area = raggio * Math.PI;
double circonferenza = 2 * Math.PI * raggio;

//output
string msg = $"Diametro: {diametro}" +
    $"\nCirconferenza: {circonferenza}" +
    $"\nArea: {area}";

Console.WriteLine(msg);

