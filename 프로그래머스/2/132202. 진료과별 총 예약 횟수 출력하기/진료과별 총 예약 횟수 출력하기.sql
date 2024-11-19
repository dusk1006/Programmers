SELECT 
    MCDP_CD AS 진료과코드,
    COUNT(PT_NO) AS 5월예약건수
FROM 
    APPOINTMENT
where year(apnt_ymd) = '2022' and MONTH(APNT_YMD) = '05'
group by mcdp_cd
order by 5월예약건수, 진료과코드