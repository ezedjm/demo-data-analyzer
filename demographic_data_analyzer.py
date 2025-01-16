import pandas as pd


def calculate_demographic_data(print_data=True):
    # lee datos del archivo
    df = pd.read_csv('adult.data.csv')

    # Cantidad de personas x raza
    race_count = df['race'].value_counts()

    # Edad promedio hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentaje con grado de licenciatura
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Porcentaje con educación avanzada que ganan >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] /
                                   df[higher_education].shape[0]) * 100, 1)

    # Porcentaje sin educación avanzada que ganan >50K
    lower_education = ~higher_education
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] /
                                  df[lower_education].shape[0]) * 100, 1)

    # Mínimo número de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje que trabaja las horas mínimas y ganan >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] /
                             num_min_workers.shape[0]) * 100, 1)

    # País con porcentaje más alto de personas que ganan >50K
    country_rich_percentage = (df[df['salary'] == '>50K']['native-country']
                                .value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # Ocupación más popular entre los que ganan >50K en India
    top_IN_occupation = (df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
                         ['occupation'].value_counts().idxmax())

    # NO MODIFICAR 
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # diccionario
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
