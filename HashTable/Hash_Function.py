def get_hash(key):
  h = 0
  for char in key:
    h += ord(char)
    return h% 100

ord('m')
get_hash('march 6')