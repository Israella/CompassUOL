--E3
SELECT COUNT(livro.editora) AS quantidade, editora.nome, endereco.estado, endereco.cidade
FROM livro
INNER JOIN editora ON livro.editora = editora.codeditora
INNER JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY livro.editora, editora.nome, endereco.estado, endereco.cidade
ORDER BY quantidade DESC
LIMIT 5


--E4
SELECT 
    AUT.nome, 
    AUT.codautor, 
    AUT.nascimento, 
    count(L.cod) AS quantidade
FROM autor as AUT
LEFT OUTER JOIN livro as L on AUT.codautor= L.autor
GROUP BY AUT.codautor
ORDER BY AUT.nome


--E5
select distinct autor.nome
from autor
	join livro
		on autor.codautor = livro.autor
	join editora 
		on livro.editora = editora.codeditora
	join endereco 
		on editora.endereco = endereco.codendereco
where endereco.estado not in ('PARANÁ', 'RIO GRANDE DO SUL')
order by autor.nome


--E6
select
	autor.codautor,
	autor.nome,
	count(*) as quantidade_publicacoes
from livro 
	join autor on livro.autor = autor.codautor
group by autor.codautor, autor.nome
order by quantidade_publicacoes desc
limit 1;


--E7
SELECT autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor
WHERE livro.publicacao IS NULL
GROUP BY autor.codautor, autor.nome;




