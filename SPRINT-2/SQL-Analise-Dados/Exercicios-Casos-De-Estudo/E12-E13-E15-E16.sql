--E12
select DEPENDENTE.cddep, DEPENDENTE.nmdep, DEPENDENTE.dtnasc, SUM(VENDAS.vrunt * VENDAS.qtd) as valor_total_vendas
from tbdependente as DEPENDENTE
 	inner join tbvendedor as VENDEDOR on DEPENDENTE.cdvdd = VENDEDOR.cdvdd 
 	inner join tbvendas as VENDAS on VENDAS.cdvdd = DEPENDENTE.cdvdd  
 where VENDAS.status = 'Concluído' and VENDAS.deletado = '0'
 group by DEPENDENTE.cddep
 HAVING valor_total_vendas > 0
 ORDER BY valor_total_vendas ASC
 LIMIT 1;
 

--E13
SELECT v.cdpro as cdpro, v.nmcanalvendas, v.nmpro, SUM(v.qtd) as quantidade_vendas
FROM tbvendas as v
WHERE v.cdcanalvendas IN(1,2) and v.status = 'Concluído'
GROUP BY v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY quantidade_vendas ASC


--E15
SELECT cdven
FROM tbvendas
WHERE deletado = '1'
ORDER BY cdven ASC;


--E16
select VENDAS.estado, VENDAS.nmpro, ROUND(AVG(VENDAS.qtd), 4) as quantidade_media
from tbvendas as VENDAS
join tbestoqueproduto as EST on VENDAS.cdpro = EST.cdpro
where VENDAS.status = 'Concluído'
group by VENDAS.estado, VENDAS.nmpro
order by VENDAS.estado, VENDAS.nmpro 
