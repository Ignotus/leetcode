removeElement :: [Int] -> Int -> ([Int], Int)
removeElement [a] b
  | a == b = ([], 0)
  | otherwise = ([a], 1)
removeElement (x:xs) b = (xs1 ++ xs2, c1 + c2)
  where
    (xs1, c1) = removeElement [x] b
    (xs2, c2) = removeElement xs b
