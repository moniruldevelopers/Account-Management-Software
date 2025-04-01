from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.timezone import now

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    writer = models.CharField(max_length=255, blank=True, null=True)
    publication = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, blank=True, null=True)  # Total available copies

    def __str__(self):
        return f"{self.name} by {self.writer or 'Unknown'} ({self.publication or 'Unknown'})"
    


class LibraryRecord(models.Model):
    STATUS_CHOICES = [
        ('Not Returned', 'Not Returned'),
        ('Returned', 'Returned'),        
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrower", blank=True, null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, blank=True, null=True)
    shelf_no = models.CharField(max_length=10, blank=True, null=True)
    row_no = models.CharField(max_length=10, blank=True, null=True)
    issue_date = models.DateField(default=date.today, blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)  # Fixed return_date spelling
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Not Returned', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    borrow_id = models.CharField(max_length=12, unique=True, editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate Borrow ID in format: MMDDYYYYXX
        if not self.borrow_id:
            today = date.today()
            date_str = today.strftime("%m%d%Y")  # MMDDYYYY
            last_borrow = LibraryRecord.objects.filter(borrow_id__startswith=date_str).order_by('-borrow_id').first()
            if last_borrow:
                last_serial = int(last_borrow.borrow_id[-2:]) + 1
            else:
                last_serial = 1
            self.borrow_id = f"{date_str}{last_serial:02d}"  # Ensure 2-digit serial number
        
        # Removed the auto-update status logic for expired return date

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.name if self.book else 'Unknown Book'} ({self.borrow_id or 'No ID'}) - {self.status}"