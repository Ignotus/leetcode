removeDuplicates :: [Int] -> ([Int], Int)
removeDuplicates [x] = ([x], 1)
removeDuplicates (x1:x2:xs)
  | x1 == x2 = (rd, c)
  | otherwise = (x1:rd, c + 1)
  where (rd,c) = removeDuplicates (x2:xs)
