select ID, EMAIL, FIRST_NAME, LAST_NAME from DEVELOPER_INFOS
WHERE 
    SKILL_1 = 'Python' or
    SKILL_2 = 'Python' or
    SKILL_3 = 'Python'
order by id;