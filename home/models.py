from django.db import models

class Student(models.Model):
    BRANCH_CHOICES = (
        ('CE', 'Civil Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('CHE', 'Chemical Engineering'),
        ('MET', 'Metallurgy Engineering'),
        ('AE', 'Aerospace Engineering'),
        ('BT', 'Biotechnology'),
    )
    CATEGORY_CHOICES = (
        ('OBC', 'Other Backward Class'),
        ('GEN', 'General'),
        ('SC', 'Scheduled Caste'),
        ('ST', 'Scheduled Tribe'),
    )
    state_choices = (
        ("Andhra Pradesh", "Andhra Pradesh"),
        ("Arunachal Pradesh", "Arunachal Pradesh"),
        ("Assam", "Assam"),
        ("Bihar", "Bihar"),
        ("Chhattisgarh", "Chhattisgarh"),
        ("Goa", "Goa"),
        ("Gujarat", "Gujarat"),
        ("Haryana", "Haryana"),
        ("Himachal Pradesh", "Himachal Pradesh"),
        ("Jharkhand", "Jharkhand"),
        ("Karnataka", "Karnataka"),
        ("Kerala", "Kerala"),
        ("Madhya Pradesh", "Madhya Pradesh"),
        ("Maharashtra", "Maharashtra"),
        ("Manipur", "Manipur"),
        ("Meghalaya", "Meghalaya"),
        ("Mizoram", "Mizoram"),
        ("Nagaland", "Nagaland"),
        ("Odisha", "Odisha"),
        ("Punjab", "Punjab"),
        ("Rajasthan", "Rajasthan"),
        ("Sikkim", "Sikkim"),
        ("Tamil Nadu", "Tamil Nadu"),
        ("Telangana", "Telangana"),
        ("Tripura", "Tripura"),
        ("Uttar Pradesh", "Uttar Pradesh"),
        ("Uttarakhand", "Uttarakhand"),
        ("West Bengal", "West Bengal"),
        ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
        ("Chandigarh", "Chandigarh"),
        ("Dadra and Nagar Haveli and Daman and Diu", "Dadra and Nagar Haveli and Daman and Diu"),
        ("Lakshadweep", "Lakshadweep"),
        ("Delhi", "Delhi"),
        ("Puducherry", "Puducherry")
    )
    
    preferred_branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)
    score = models.FloatField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    state = models.CharField(max_length=50, choices=state_choices)

    def __str__(self):
        return f"{self.get_preferred_branch_display()} - {self.category} - {self.state}"
