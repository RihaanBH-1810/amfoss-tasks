import Control.Monad

isPrime :: Int -> Bool
isPrime 2 = True
isPrime n
  | n <= 1 = False
  | otherwise = not $ any (\x -> n `mod` x == 0) [2..intSqrt n]
  where
    intSqrt = floor . sqrt . fromIntegral

main :: IO ()
main = do12
  n <- readLn
  forM_ [2..n] $ \num -> when (isPrime num) $ putStrLn $ show num
