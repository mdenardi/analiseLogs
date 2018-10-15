# Descrição
- Ferramenta interna de relatórios que responde perguntas utilizando um banco de dados
# Instalar
- instalar o [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
- instalar o [Vagrant](https://www.vagrantup.com/downloads.html)
- baixar a VM [FSND-Virtual-Machine.zip](https://github.com/udacity/fullstack-nanodegree-vm) e instalar via `vagrant up`
- baixar arquivo compactado: https://github.com/mdenardi/analiseLogs/archive/master.zip
- extrair na pasta vagrant (programa será executado por dentro da VM)
- baixar os dados [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- popular a base news através do comando: `psql -d news -f newsdata.sql`
## Criar Views
- Acessar o banco de dados news: vagrant@vagrant:/vagrant$ `psql news`
1. `create view report as select articles.title,articles.slug, authors.name from articles, authors where articles.author = authors.id;`
2. `create view calc as select path, count(*) as num from log where path like '%article%' and status='200 OK' group by path;`
3. `create view error as select to_char(date_trunc('day', time::timestamp with time zone), 'Mon DD, YYYY') as dd, count(*) as count_error from log where status<>'200 OK' group by to_char(date_trunc('day', time::timestamp with time zone), 'Mon DD, YYYY');`
4. `create view total_error as select to_char(date_trunc('day', time::timestamp with time zone), 'Mon DD, YYYY') as dd, count(*) as count_total from log group by to_char(date_trunc('day', time::timestamp with time zone), 'Mon DD, YYYY');`
# Executar
- rodar analiseLogs.py utilizando o python 2.7: vagrant@vagrant:/vagrant$ `python analiseLogs.py`
