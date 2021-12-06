SELECT
R.COUNTRY,
YEAR_YYYY=YEAR(DS.SALES_DATE_YYYYMMDD),
SALES_NET_AMOUNT=SUM(SALES_GROSS-SALES_TAX_AMMOUNT),
SALES_TAX_AMOUNT=SUM(SALES_TAX_AMOUNT)
FROM
#REGION R
JOIN #DEPARTMENT D ON R.REGION=D.REGION
JOIN #DAILYSALES DS ON D.DEPARTMENT=DS.DEPARTMENT
GROUP BY R.COUNTRY,YEAR(DS.SALES_DATE_YYYYMMDD)


----Join month with Date
SELECT
B.MONTH_YYYYMM
,R.COUNTRY
,D.DEPARTMENT
,D.DEPARTMENT_MANAGER
,SUM(B.BUDGET_COST) as BUDGET_COST
,SALES_NET_AMOUNT=SUM(DS.SALES_GROSS-DS.SALES_TAX_AMMOUNT)
,PROFIT = (SUM(DS.SALES_GROSS-DS.SALES_TAX_AMMOUNT) - SUM(B.BUDGET_COST))
FROM
MOSTLY_BUDGET_COST B
JOIN REGION R ON R.REGION=B.REGION
JOIN DEPARTMENT D ON R.REGION=D.REGION
---converting a DATE datatype to character 6 'yyyymm' output using CONVERT and FORMAT functions.
--CONVERT using style = 112
JOIN DAILYSALES DS ON B.MONTH_YYYYMM = CONVERT(CHAR(6), DS.sales_date_yyyymmdd, 112)
GROUP BY
B.MONTH_YYYYMM
,R.COUNTRY
,D.DEPARTMENT
,D.DEPARTMENT_MANAGER


--Join with Department
SELECT
B.MONTH_YYYYMM
,R.COUNTRY
,D.DEPARTMENT
,D.DEPARTMENT_MANAGER
,SUM(B.BUDGET_COST) as BUDGET_COST
,SALES_NET_AMOUNT=SUM(DS.SALES_GROSS-DS.SALES_TAX_AMMOUNT)
,PROFIT = (SUM(DS.SALES_GROSS-DS.SALES_TAX_AMMOUNT) - SUM(B.BUDGET_COST))
FROM
#MOSTLY_BUDGET_COST B
JOIN #REGION R ON R.REGION=B.REGION
JOIN #DEPARTMENT D ON R.REGION=D.REGION
JOIN #DAILYSALES DS ON D.DEPARTMENT=DS.DEPARTMENT
GROUP BY
B.MONTH_YYYYMM
,R.COUNTRY
,D.DEPARTMENT
,D.DEPARTMENT_MANAGER

