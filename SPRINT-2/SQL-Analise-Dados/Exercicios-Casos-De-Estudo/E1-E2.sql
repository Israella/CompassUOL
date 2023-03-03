---EXERCICIO 1
SELECT *
from livro
where publicacao > '2015-01-01'
order by cod

---EXERCICIO 2
SELECT titulo, valor 
from livro
order by valor DESC 
limit 10