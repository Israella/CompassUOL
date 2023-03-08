--E8
SELECT tbvendedor.cdvdd, tbvendedor.nmvdd
FROM tbvendedor
JOIN tbvendas ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY COUNT(tbvendas.cdven) DESC
LIMIT 1;


--E9
SELECT tbvendas.cdpro, tbvendas.nmpro
FROM tbvendas
WHERE tbvendas.status = 'Concluído' 
AND tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY tbvendas.cdpro, tbvendas.nmpro
ORDER BY SUM(tbvendas.qtd) DESC
LIMIT 1;


--E10
SELECT tbvendedor.nmvdd AS vendedor, 
  SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas, 
  ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao / 100, 2) AS comissao
FROM tbvendedor
JOIN tbvendas ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY comissao DESC;


--E11
SELECT tbvendas.cdcli, tbvendas.nmcli, SUM(tbvendas.qtd * tbvendas.vrunt) AS gasto
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendas.cdcli, tbvendas.nmcli
ORDER BY gasto DESC
LIMIT 1;


--E14
SELECT estado, ROUND(AVG(total_vendas), 2) AS gastomedio
FROM (
    SELECT tbvendas.estado, SUM(tbvendas.qtd * tbvendas.vrunt) AS total_vendas
    FROM tbvendas
    WHERE tbvendas.status = 'Concluído'
    GROUP BY tbvendas.cdven, tbvendas.estado
) AS vendas_por_estado
GROUP BY estado
ORDER BY gastomedio DESC
