from dataclasses import field
from random import choices
from django import forms
from admissionapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        ADM_MODES = (
            ("regular", "Regular"),
            ("lateral", 'Lateral'),
            ('readmission', 'Readmission'),
            ('transfer', 'Transfer')
        )

        CATEGORY = (
            ('UG', 'UG'),
            ('PG', 'PG'),
        )

        BRANCHES = (
            ('AIDS', 'AIDS'),	
            ('MBA', 'MBA'),
            ('CIVIL', 'CIVIL'),	
            ('CAD/CAM', 'CAD/CAM'),
            ('CSBS', 'CSBS'),	
            ('CSE', 'CSE'),
            ('CS', 'CS'),
            ('ECE', 'ECE'),	
            ('AE', 'AE'),
            ('EEE', 'EEE'),	
            ('SE', 'SE'),
            ('IT', 'IT'),
            ('ED', 'ED'),
            ('MCT', 'MCT'),
            ('PED', 'PED'),
            ('MECH', 'MECH'),	
            ('M.Tech.CSE', 'M.Tech.CSE')
        )

        QUOTA = (
            ('GQ', 'GQ'),
            ('MQ', 'MQ'),
            ('GQ-LAPSED', 'GQ-LAPSED'),
            ('MQ-LAPSED', 'MQ-LAPSED'),
            ('NRI', 'NRI'),
            ('GOI', 'GOI'),
            ('FOR', 'FOR')
        )

        ADM_QUOTA = (
            ('OC', 'OC'),
            ('BC', 'BC'),
            ('MBC', 'MBC'),
            ('DNC', 'DNC'),
            ('SC', 'SC'),
            ('SCA', 'SCA'),
            ('ST', 'ST'),
            ('Sports', 'Sports'),
            ('Exserviceman', 'Exserviceman'),
            ('Vocational', 'Vocational')
        )

        BOOLEAN_DATA = (
            ('YES', 'YES'),
            ('NO', 'NO')
        )

        TNBC = (
            ('NSP', 'NSP'),
            ('CATEGORY 1', 'CATEGORY 1'),
            ('CATEGORY 2', 'CATEGORY 2'),
            ('CATEGORY 3', 'CATEGORY 3'),
        )

        GENDER = (
            ('MALE', 'MALE'),
            ('FEMALE', 'FEMALE'),
            ('OTHERS', 'OTHERS')
        )

        MEDIUM = (
            ('ENGLISH', 'ENGLISH'),
            ('TAMIL', 'TAMIL'),
            ('OTHERS', 'OTHERS')
        )

        RELIGION = (
            ('Hindu', 'Hindu'),
            ('Christian', 'Christian'),
            ('Muslim', 'Muslim'),
            ('Sikhism', 'Sikhism'),
            ('Buddhism', 'Buddhism'),
            ('Jainism', 'Jainism'),
            ('Judaism', 'Judaism'),
            ('Others', 'Others')
        )

        COMMUNITY = (
            ('OC', 'OC'),
            ('BC', 'BC'),
            ('MBC', 'MBC'),
            ('DNC', 'DNC'),
            ('SC', 'SC'),
            ('SCA', 'SCA'),
            ('ST', 'ST'),
            ('SCC', 'SCC'),
        )

        SCOLMODE = (
            ('HOSTELLER', 'HOSTELLER'),
            ('DAYSCHOLAR', 'DAYSCHOLAR')
        )

        widgets = {
            'adm_mode': forms.Select(choices = ADM_MODES),
            'adm_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'category': forms.Select(choices = CATEGORY),
            'branch': forms.Select(choices = BRANCHES),
            'sdob': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'quota': forms.Select(choices = QUOTA),
            'admquota': forms.Select(choices = ADM_QUOTA),
            'firstgrad': forms.Select(choices = BOOLEAN_DATA),
            'tnscst': forms.Select(choices = BOOLEAN_DATA),
            'tnbc': forms.Select(choices = TNBC),
            'aicte': forms.Select(choices = BOOLEAN_DATA),
            'sgender': forms.Select(choices = GENDER),
            'medium': forms.Select(choices = MEDIUM),
            'religion': forms.Select(choices = RELIGION),
            'community': forms.Select(choices = COMMUNITY),
            'scolmode': forms.Select(choices = SCOLMODE),
            'phychallenged': forms.Select(choices = BOOLEAN_DATA),
        }
