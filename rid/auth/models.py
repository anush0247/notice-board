from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, rid, date_of_birth, gender, first_name,last_name, dept,batch, year, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not first_name:
            raise ValueError('Users must have a first name')

        if not year:
            raise ValueError('Users must have a valid year')
        
            
        user = self.model(
            rid = rid,
            date_of_birth = date_of_birth,
            gender = gender,
            first_name = first_name,
            last_name = last_name,
            dept = dept,
            batch = batch,
            year = year,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rid, date_of_birth, gender, first_name, last_name, dept, batch, year, password):
        """
        Creates and saves a supeRidUser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            rid,
            password=password,
            date_of_birth=date_of_birth,
            gender = gender,
            first_name = first_name,
            last_name = last_name,
            dept = dept,
            batch = batch,
            year = year,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class RidUser(AbstractBaseUser):
	
    rid = models.CharField(
        verbose_name = "University ID",
        unique = True,
        max_length = 40
    )
    
    first_name = models.CharField(
        max_length=100,
        verbose_name = "First Name",
    )
    
    last_name = models.CharField(
        max_length=100,
        verbose_name = "Last Name",
        null=True,
        default="",
    )

    date_of_birth = models.DateField(
        verbose_name = "Date of Birth",
    )
    

    gender_labels = (
        ("M", "Male"),
        ("F", "Female"),
    )
    
    gender = models.CharField(
        max_length=1,
        choices=gender_labels,
        verbose_name = "Gender",
    )
    
    
    department_labels = (
        ("CSE", "Computer Science"),
        ("MME", "Metrial & Matlurgical"),
        ("CE",  "Civil"),
        ("CHE", "Chemical"),
        ("ECE", "Electronics & Communication"),
        ("ME",  "Mechanical"),
        ("MNG", "Management"),
        ("MAT", "Maths"),
        ("PHY", "Physics"),
        ("CH",  "Chemistry"),
        ("BIO", "Biology"),
        ("LBA", "Libaral Arts"),
        ("IT",  "Information Technolgoy"),
        ("ADM", "Administration"),
    )
    
    dept = models.CharField(
        max_length=3,
        choices=department_labels,
        verbose_name="Dept. Name",
    )

    batch_labels = (
        ("E4", "Final Year, Engg"),
        ("E3", "Third Year, Engg"),
        ("E2", "Second Year, Engg"),
        ("E1", "First Year, Engg"),
        ("P1", "First Year, PUC"),
        ("P2", "Second Year, PUC"),
        ("MT", "Mentor"),
        ("FA", "Faculty"),
        ("ST", "Office Staff"),
        ("LA", "Lab Assistant"),
        ("AL", "Alumini")
    )

    batch = models.CharField(
        max_length=2,
        choices=batch_labels,
        verbose_name="Batch",
    )

    year = models.IntegerField(
        max_length = 4,
        verbose_name = "Year"
    )

    
    
    is_active = models.BooleanField(
        default=True,
        verbose_name = "Is Active User",
    )
    
    is_admin = models.BooleanField(
        default=False,
        verbose_name = "Is Admin",
    )
    
    
    objects = UserManager()

    USERNAME_FIELD = 'rid'
    REQUIRED_FIELDS = ['first_name','last_name','date_of_birth','gender','dept','year','batch']

    def __unicode__(self):
        return unicode(self.rid)

    def get_full_name(self):
        return "%s %s" %(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.rid

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user an admin"
        # Simplest possible answer: All admins are staff
        return self.is_admin

