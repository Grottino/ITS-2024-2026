-- 1. Selezionare tutti i paesi e i loro dati
select *
from `country-data`;

-- 2. Selezionare solo il nome dei paesi
select country
from `country-data`;
-- 3. Selezionare i paesi con un'aspettativa di vita superiore a 70 anni
select country, life_expec
from `country-data`
where life_expec > 70;
-- 4. Selezionare i paesi con un PIL pro capite maggiore di 10.000
select country, gdpp
from `country-data`
where gdpp > 10000;
-- 5. Trovare i paesi con un tasso di mortalità infantile inferiore a 20
select country, child_mort
from `country-data`
where child_mort > 20;
-- 6. Ordinare i paesi per reddito pro capite in ordine decrescente
select country, income 
from `country-data`
order by income desc;
-- 7. Ordinare i paesi per aspettativa di vita in ordine crescente
select country, life_expec
from `country-data`
order by life_expec asc;
-- 8. Selezionare i paesi con un tasso di fertilità superiore a 5
select country, total_fer
from `country-data`
where total_fer > 5;
-- 9. Trovare i paesi con una spesa sanitaria superiore al 10% del PIL
select country, health
from `country-data`
where health > 10;
-- 10. Selezionare i paesi con un'inflazione negativa (deflazione)
select country, inflation
from `country-data`
where inflation < 0;
-- 11. Trovare i paesi con esportazioni che superano il 50% del PIL
select country, exports
from `country-data`
where exports > 50;
-- 12. Trovare i paesi con importazioni maggiori delle esportazioni
select country, imports, exports
from `country-data`
where imports > exports;
-- 13. Selezionare i paesi con un PIL pro capite compreso tra 5.000 e 10.000
select country, gdpp
from `country-data`
where gdpp > 5000 and gdpp <10000;
-- 14. Trovare i paesi con un tasso di fertilità inferiore a 2 e un'aspettativa di vita superiore a 75 anni
select country, total_fer, life_expec
from `country-data`
where 
	total_fer < 2
    and 
    life_expec > 75;
-- 15. Selezionare i paesi con un tasso di mortalità infantile maggiore di 100
select country, child_mort
from `country-data`
where child_mort > 100;
-- 16. Trovare i paesi con reddito pro capite maggiore di 15.000 e inflazione inferiore a 5%
select country, gdpp, inflation
from `country-data`
where gdpp > 15000 and inflation < 5;
-- 17. Ordinare i paesi per spesa sanitaria in ordine decrescente
select country, health 
from `country-data`
order by health desc;
-- 18. Selezionare i paesi con un PIL pro capite inferiore a 2.000
select country, gdpp
from `country-data`
where gdpp < 2000;
-- 19. Trovare i paesi con esportazioni e importazioni combinate superiori al 90% del PIL
select country, (exports + imports)
from `country-data`
where (exports + imports) > 90;
-- 20. Trovare i 3 paesi con il più alto rapporto tra spesa sanitaria e reddito pro capite
select country, (health/gdpp) as rapporto
from `country-data`
order by rapporto desc
limit 3;
-- 21. Trovare il rapporto tra fertilità totale e aspettativa di vita per ogni paese e ordinarlo in ordine crescente
select country, (life_expec/total_fer) as rapporto
from `country-data`
order by rapporto asc;
-- 22. Calcolare la media del tasso di fertilità per i paesi con un’aspettativa di vita superiore a 70 anni
select country, total_fer, life_expec
from `country-data` 
where life_expec >(
			select avg(total_fer)
			from `country-data`
            where life_expec >70 );
-- 23. Trovare i paesi con il massimo e il minimo reddito pro capite
select country, (income) as RPP
from `country-data` 
where 
	income = (select min(income) from `country-data`)
    or 
    income = (select max(income) from `country-data`);
    
-- 24. Contare il numero di paesi con inflazione negativa
select count(*) as country
from `country-data`
where inflation < 0;
-- 25. Trovare i 5 paesi con il PIL pro capite (gdpp) più alto
select country, gdpp
from `country-data`
order by gdpp desc
limit 5;
-- 26. Calcolare la somma delle esportazioni e delle importazioni per ciascun paese
 select country, (imports + exports) as somma
from `country-data`
order by somma desc;
-- 27. Trovare i paesi dove il totale delle esportazioni è almeno il doppio delle importazioni
select country, exports, imports
from `country-data`
where exports >= 2* imports;
-- 28. Calcolare il PIL pro capite medio (gdpp) per ogni gruppo di aspettativa di vita (fasce di 10 anni)
select floor(life_expec/10)*10 as range_age, avg(gdpp) as media
from `country-data`
group by range_age
order by range_age;
-- 29. Trovare i paesi con un tasso di mortalità infantile superiore alla media globale
select country, child_mort 
from `country-data`
where child_mort > (
select avg(child_mort) as GlobalChildMort from `country-data`);

-- select avg(child_mort) as GlobalChildMort from `country-data`;

-- 30. Trovare i paesi con il massimo tasso di mortalità infantile in ogni fascia di reddito
select country, child_mort, income
from `country-data` as m1
where m1.child_mort =(
	select max(child_mort)
    from `country-data` as m2
    where m1.income=m2.income);
