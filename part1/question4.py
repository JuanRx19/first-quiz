import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
SELECT A.NAME, A.SPECIES, A.AGE
FROM ANIMALS AS A
LEFT JOIN PEOPLE_ANIMALS AS PA ON A.ANIMAL_ID = PA.PET_ID
WHERE PA.OWNER_ID IS NULL;
"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """
SELECT COUNT(*)
FROM ANIMALS AS A
INNER JOIN PEOPLE_ANIMALS AS PA ON A.ANIMAL_ID = PA.PET_ID
INNER JOIN PEOPLE AS P ON PA.OWNER_ID = P.PERSON_ID
WHERE PA.OWNER_ID IS NOT NULL AND A.AGE > P.AGE;
"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 
SELECT p.name AS person_name, a.name AS pet_name, a.species
FROM people AS p
JOIN people_animals AS pa ON p.person_id = pa.owner_id
JOIN animals AS a ON pa.pet_id = a.animal_id
WHERE p.name = 'bessie'
AND (
  SELECT COUNT(*)
  FROM people_animals AS pa2
  WHERE pa2.pet_id = pa.pet_id
) = 1;
"""