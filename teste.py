def repeatedString(s, n):
  if s.count(s[0]) == len(s):
    return s.count(s[0])*n
  else:
    if (n/len(s)).is_integer():
      return (s.count(s[0]))*n
    else:
      return (s.count(s[0])+1)*n


# s = 'a'
s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
# n = 1000000000000
n = 7367789064
print(repeatedString(s, n))
