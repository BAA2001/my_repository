# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#comparison of language
switserland_most_spoken_language = 'German'
spain_most_spoken_language = 'Castilian Spanish'

print(switserland_most_spoken_language == spain_most_spoken_language)

#comparison of religion
switserland_most_prevalent_religion = 'Roman Catholic'
spain_most_prevalent_religion = 'Roman Catholic'

print(switserland_most_prevalent_religion == spain_most_prevalent_religion)

#comparison of capital name length
switserland_capital_name = 'Bern'
spain_capital_name = 'Madrid'

print(len(switserland_capital_name) != len(spain_capital_name))

#comparison of GDP
switserland_GDP = 748,000,000,000
spain_GDP = 1281,000,000,000,000

print({switserland_GDP} > {spain_GDP})

#comparison of population growth
switserland_pop_growth = 0.65
spain_pop_growth = 0.13

print((switserland_pop_growth + spain_pop_growth) < 1)

#at least one of two countries has a population count of over 10 mil
switserland_pop = 8,508,698
spain_pop = 47,163,418

if {switserland_pop or spain_pop} > {10,000,000}:
    print('True')

#exactly one of two countries has a population count of over 10 mil
if {switserland_pop or spain_pop} > {10,000,000}:
    print('True')