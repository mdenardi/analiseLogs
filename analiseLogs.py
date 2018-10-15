#!/usr/bin/env python

import psycopg2


def printquery(y, j):
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute(y)
    x = cur.fetchall()
    cur.close()
    for i in range(len(x)):
        print ">", x[i][0], "-", x[i][1], j
    print "\n"

	
print "1. Quais sao os tres artigos mais populares de todos os tempos?"

printquery("select title, num\
    from report,calc\
    where calc.path like concat('/article/',report.slug)\
    order by num desc\
    limit 3;", "views")

print "2. Quem sao os autores de artigos mais populares de todos os tempos?"

printquery("select name, sum(num)\
    from report,calc\
    where calc.path like concat('/article/',report.slug)\
    group by name\
    order by sum desc;", "views")

print "3. Em quais dias mais de 1% das requisicoes resultaram em erros?"

printquery("select total_error.dd,\
    round(error.count_error::numeric*100/total_error.count_total,2) as perc\
    from error,total_error\
    where error.dd = total_error.dd and\
    error.count_error*10000/total_error.count_total > 100;", "% errors")
