from django import forms

class SalaryPredictionForm(forms.Form):
    YEARS_OF_EXPERIENCE_CHOICES = [(i, i) for i in range(0, 51)]  # e.g., 0 to 50 years
    AGE_CHOICES = [(i, i) for i in range(18, 101)]  # e.g., 18 to 100 years

    EDUCATION_LEVEL_CHOICES = [
        ('bachelor\'s', 'Bachelor\'s'),
        ('master\'s', 'Master\'s'),
        ('phd', 'Ph.D.'),
    ]

    JOB_TITLE_CHOICES = [
        ('java developer', 'Java Developer'),
        ('backend developer', 'Backend Developer'),
        ('web developer', 'Web Developer'),
    ]

    GEOGRAPHIC_LOCATION_CHOICES = [
        ('mumbai', 'Mumbai'),
        ('delhi', 'Delhi'),
        ('bangalore', 'Bangalore'),
    ]

    COMPANY_SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    SKILLS_AND_ABILITIES_CHOICES = [
        ('java', 'Java'),
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
    ]

    years_of_experience = forms.ChoiceField(choices=YEARS_OF_EXPERIENCE_CHOICES, label='Years of Experience')
    age = forms.ChoiceField(choices=AGE_CHOICES, label='Age')
    education_level = forms.ChoiceField(choices=EDUCATION_LEVEL_CHOICES, label='Education Level')
    job_title = forms.ChoiceField(choices=JOB_TITLE_CHOICES, label='Job Title')
    geographic_location = forms.ChoiceField(choices=GEOGRAPHIC_LOCATION_CHOICES, label='Geographic Location')
    company_size = forms.ChoiceField(choices=COMPANY_SIZE_CHOICES, label='Company Size')
    skills_and_abilities = forms.ChoiceField(choices=SKILLS_AND_ABILITIES_CHOICES, label='Skills and Abilities')
