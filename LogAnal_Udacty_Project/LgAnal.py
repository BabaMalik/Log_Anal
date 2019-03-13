#!/usr/bin/env python
import psycopg2

# first top 3 articles execution


def Top_Mst_Articles_View(qury):
    results = connect(qury)
    print(" \n  THE LIST OF POPULAR ARTICLES ARE:- ? \n")
    cont = 1
    for reslt in results:
        number = '(' + str(cont) + ') "'
        totl = reslt[0]
        views = '"' + str(reslt[1]) + " views"
        cont = cont+1
        print('  "{0}" ----->{1} views'.format(reslt[0], reslt[1]))


# top 4 authors


def Top_Mst_Athors_View(qury):
    results = connect(qury)
    print("\n THE LIST OF POPULAR AUTHORS ARE:- ?\n")
    cont = 1
    for reslt in results:
        number = '(' + str(cont) + ') "'
        totl = reslt[0]
        views = '"Authors' + str(reslt[1]) + " views"
        cont = cont+1
        print('  "{0}" ----->{1} views'.format(reslt[0], reslt[1]))


# lead errors


def Lg_Err_View(qury):
    results = connect(qury)
    print(" \n  ***ERROR MORE THAN 1.0*** ")
    for rs in results:
        print('\n On ' + str(rs[0]) + '-->' + '%.1f' % rs[1] + '% errors\n')

qury1 = ''' SELECT title, views FROM lganal_articles INNER JOIN articles ON
    articles.slug = lganal_articles.slug ORDER BY views desc LIMIT 3; '''
qury2 = '''
    SELECT lgathors_nm.name AS author,
    sum(lganal_articles.views) AS views FROM lganal_articles INNER JOIN
    lgathors_nm ON lgathors_nm.slug=lganal_articles.slug
    GROUP BY lgathors_nm.name ORDER BY views desc limit 4;
    '''
qury3 = '''
    SELECT lgerr_fails.date ,(lgerr_fails.count*100.00 / lganal_totl.count) AS
    percentage FROM lgerr_fails INNER JOIN lganal_totl
    ON lgerr_fails.date = lganal_totl.date
    AND (lgerr_fails.count*100.00 / lganal_totl.count) >1
    ORDER BY (lgerr_fails.count*100.00 /lganal_totl.count) desc;
    '''


def connect(qury):
    database = psycopg2.connect(database="news")
    cursr = database.cursor()
    cursr.execute(qury)
    results = cursr.fetchall()
    database.close()
    return results

Top_Mst_Articles_View(qury1)
Top_Mst_Athors_View(qury2)
Lg_Err_View(qury3)
