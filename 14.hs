import qualified Data.Set as Set
import Data.List (transpose)

isTheSame :: [Char] -> Bool
isTheSame xs = (Set.size . Set.fromList) xs <= 1

longestCommonPrefix :: [String] -> String
longestCommonPrefix strs =
  map head $ takeWhile isTheSame (transpose strs)
