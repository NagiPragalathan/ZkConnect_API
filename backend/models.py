from django.db import models

class users(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50) #    Recunitr = 1, individual = 2

    def __str__(self):
        return self.username

class Ind_Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_bio = models.TextField(default="the bio not filled yet.")
    contact_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    resume_image = models.CharField(max_length=255)
    usr_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Individual Profiles"


class SocialLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return f"Social Links for User ID: {self.userid}"
    
    class Meta: 
        verbose_name_plural = "Social Links"

class CompanyDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_number = models.CharField(max_length=255)
    company_linkedin = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_bio = models.TextField(default="the bio not filled yet.")
    start_year = models.PositiveIntegerField()
    no_of_emp = models.PositiveIntegerField()
    logo = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Rec_Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    profile_bio = models.TextField(default="the bio not filled yet.")
    contact_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    linked_in = models.CharField(max_length=255)
    company_data = models.ForeignKey(
        CompanyDetails,
        on_delete=models.CASCADE,
        default=1  # Set the default value to the primary key of the desired CompanyDetails instance
    )
    no_of_emp = models.CharField(max_length=255)
    start_date =  models.CharField(max_length=255)
    logo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name}"

    class Meta:
        verbose_name_plural = "Recruiter Profiles"
        

class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    TYPE_CHOICES = (
        ('tech', 'Technical'),
        ('non-tech', 'Non-Technical'),
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='tech')

    def __str__(self):
        return self.Name

class JobCreate(models.Model):
    id = models.IntegerField(primary_key=True)
    company_details = models.ForeignKey(
        CompanyDetails,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    description = models.TextField(default="the description not filled yet.")
    experience = models.CharField(max_length=255)
    looking_for = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    environment = models.TextField()

    def __str__(self):
        return f"Job ID: {self.id}"

    class Meta:
        verbose_name_plural = "Job Creates"
        
class StackReq(models.Model):
    stackid = models.IntegerField(primary_key=True)
    job_create = models.ForeignKey(
        JobCreate,
        on_delete=models.CASCADE,
        related_name='stack_requirements'
    )
    skills = models.TextField()

    def __str__(self):
        return f"Stack ID: {self.stackid}"

    class Meta:
        verbose_name_plural = "Stack Requirements"

class Applyed_jobs(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    job_create = models.ForeignKey(
        JobCreate,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Application ID: {self.id}"

    class Meta:
        verbose_name_plural = "Applied Jobs"
        
class PDF(models.Model):
    name = models.CharField(max_length=255)
    data = models.BinaryField()
    
class Clims(models.Model):
    callback_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    repo = models.CharField(max_length=255)
    template_id = models.IntegerField()

    def __str__(self):
        return self.callback_id