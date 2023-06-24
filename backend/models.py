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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_bio = models.TextField(default="the bio not filled yet.")
    skills = models.CharField(max_length=255)
    resume_image = models.ImageField(upload_to='Resumes/')

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
    company_bio = models.TextField(default="the bio not filled yet.")
    start_year = models.PositiveIntegerField()
    no_of_emp = models.PositiveIntegerField()
    social_links = models.OneToOneField(SocialLinks, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.company_name

class Rec_Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_bio = models.TextField(default="the bio not filled yet.")
    company_data = models.ForeignKey(
        CompanyDetails,
        on_delete=models.CASCADE,
        default=1  # Set the default value to the primary key of the desired CompanyDetails instance
    )
    description = models.TextField()

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