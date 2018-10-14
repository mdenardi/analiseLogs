# Instalar
- baixar arquivo compactado: https://github.com/mdenardi/analiseLogs/archive/master.zip
- extrair na pasta vagrant (programa será executado por dentro da VM)
## Criar Views
1. report
`create view report as
select articles.title,articles.slug, authors.name 
	from articles, authors
	where articles.author = authors.id;`
2. calc
`create view calc as
select path, count(*) as num 
	from log
	where path like '%article%' and status='200 OK'
	group by path;`
3. error
`create view error as
select to_char(date_trunc('day', time::timestamp with time zone), 'YYYY-MM-DD') as dd, count(*) as count_error
	from log
	where status<>'200 OK'
	group by to_char(date_trunc('day', time::timestamp with time zone), 'YYYY-MM-DD');`
4. total_error
`create view total_error as
select to_char(date_trunc('day', time::timestamp with time zone), 'YYYY-MM-DD') as dd, count(*) as count_total
	from log
	group by to_char(date_trunc('day', time::timestamp with time zone), 'YYYY-MM-DD');`

# Executar
- rodar analiseLogs.py utilizando o python 2.7: vagrant@vagrant:/vagrant$ `python analiseLogs.py`
