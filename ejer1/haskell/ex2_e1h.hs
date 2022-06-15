fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

fibAux 0 = return()
fibAux n =
   do
     let aux=n-1     
     print (fib aux)
     fibAux (aux)

main = do
  putStrLn "Serie Fibonacci"
  fibAux 11