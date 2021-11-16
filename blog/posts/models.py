from django.db import models
import re

class Post(models.Model):
    """Post class is used for database operations
       Added the deserializer() to get post-data from Markdown files
    """    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, default='None')
    slug = models.CharField(max_length=255, unique=True, blank=False)
    tags = models.CharField(max_length=255, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def deserializer(self, md_file_str):
        """Deserialize from text to Post object.

        Args:
            md_file_str (string): Target text-file string
        """
        regex = r"===\n[Tt]itle:\s*(.*)$[\r\n]*[Aa]uthor:\s*(.*)$[\r\n]*[Ss]lug:\s*(.*)$[\r\n]*===\n*([\s\S]*)"
        # Use regular expressions to do a one-time match on the text, and you can directly match all results.
        # Enhanced the compatibility of regular matching, even if there are a lot of spaces in the text, it can be matched correctly.
        
        matches = re.finditer(regex, md_file_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            self.title = match.group(1).strip()
            self.author = match.group(2).strip()
            self.slug = match.group(3).strip()
            self.content = match.group(4).strip()