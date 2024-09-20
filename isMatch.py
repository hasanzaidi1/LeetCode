def is_match(s: str, p: str) -> bool:
    # Create a table where dp[i][j] means whether s[:i] matches p[:j]
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Empty string matches empty pattern
    dp[0][0] = True
    
    # Handle patterns like "a*" or ".*" which can match an empty string
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                # If characters match or we have a '.', we just move diagonally
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' matches zero occurrences
                dp[i][j] = dp[i][j - 2]
                # '*' matches one or more occurrences
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    # The final answer is in dp[len(s)][len(p)]
    return dp[len(s)][len(p)]

# Test cases
print(is_match("aa", "a"))   # False
print(is_match("aa", "a*"))  # True
print(is_match("ab", ".*"))  # True
