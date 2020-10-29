from django.db import models

class OpenTokSessions(models.Model):
    session_id = models.CharField(max_length=100)

class OpenTokTokens(models.Model):
    session_id = models.ForeignKey(
        'OpenTokSessions',
        on_delete=models.CASCADE,
    )
    token = models.TextField()