characterToInt :: Char -> Int
characterToInt 'M' = 1000
characterToInt 'D' = 500
characterToInt 'C' = 100
characterToInt 'L' = 50
characterToInt 'X' = 10
characterToInt 'V' = 5
characterToInt 'I' = 1
characterToInt _ = error "Not a valid roman"

sign :: String -> Int
sign s
  | s `elem` ["IV", "IX", "XL", "XC", "CD", "CM"] = -1
  | otherwise = 1

romanToInt :: String -> Int
romanToInt [] = 0
romanToInt [s] = characterToInt s
romanToInt (s1:s2:xs) = sign [s1, s2] * characterToInt s1 + romanToInt (s2:xs)
