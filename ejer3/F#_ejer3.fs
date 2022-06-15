open System

[<EntryPoint>]
let main argv =
    printfn "%A" argv
    Console.WriteLine("Serie Fibonacci")
    Console.WriteLine("Recursivo")
    let rec fRecursivo = fun x -> 
        match x with
            | 1 -> 0
            | 2 -> 1
            | 3 -> 1
            | _ -> fRecursivo (x-1)+fRecursivo (x-2)
    (
        fun x -> 
        for i in 1..x do
            Console.Write(fRecursivo i)
            Console.Write(", ")
    ) 11


    Console.WriteLine("")
    Console.WriteLine("Estructurado")

    (
        fun x ->
        let mutable a=0
        let mutable b=1
        let mutable c=0
          
        for i in 1..x do
        
            match i with
                | 1 -> c <- 0
                | 2 -> c <- 1
                | _ -> c <- a+b
            Console.Write(c)
            Console.Write(", ")  
            if i > 2
            then a<-b
            else a<-0

            if i > 2
            then b<-c
            else b<-1
    ) 11    

    let tecla = Console.ReadKey()
    0 // return an integer exit code
