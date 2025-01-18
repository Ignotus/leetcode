isValidImpl :: String -> String -> Bool
isValidImpl openBrackets [] = null openBrackets
isValidImpl openBrackets (x:xs)
  | x `elem` "({[" = isValidImpl (x:openBrackets) xs
  | null openBrackets = False
  | [l, x] `elem` ["()", "{}", "[]"] = isValidImpl ls xs
  | otherwise = False
  where l:ls = openBrackets

isValid :: String -> Bool
isValid s = isValidImpl [] s
