
# Funções parte 1

# Funções parte 2

# Funções parte 3

## Map

* Utilizando for

  ```python
  pows = []
  for num in range(6):
    pows.append((lambda x: x ** 2)(num))
  print(pows) # -> [0, 1, 4, 9, 16, 25]
  ```

* Utilizando map

  ```python
  print(list(map(lambda x: x ** 2, range(6))))
  # -> [0, 1, 4, 9, 16, 25]
  ```
