from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from core.models import Project, Site


class UserRole(models.Model):
    user = models.ForeignKey(User, related_name="user_roles", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_roles")
    project = models.ForeignKey(Project, null=True, blank=True, related_name="project_roles", on_delete=models.SET_NULL)
    site = models.ForeignKey(Site, null=True, blank=True, related_name="site_roles", on_delete=models.SET_NULL)

    # def clean(self):
    #     if self.group.name in ['Field Engineer', 'Community Member'] and not self.site_id:
    #         raise ValidationError({
    #             'site': ValidationError(_('Missing site.'), code='required'),
    #         })
    #
    #     if self.group.name == 'Project Manager' and not self.project_id:
    #         raise ValidationError({
    #             'project': ValidationError(_('Missing Project.'), code='required'),
    #         })
    #
    #     if self.user and UserRole.objects.filter(user=self.user, group=self.group, project=self.project,
    #                                              site=self.site).exists():
    #         raise ValidationError({
    #             'user': ValidationError(_('User Role Already Exists.')),
    #         })
    #
    def save(self, *args, **kwargs):
        if self.group.name == 'Super Admin':
            self.project = None
            self.site = None
        elif self.group.name == 'Field Engineer':
            self.project = None
        elif self.group.name == 'Project Manager':
            self.site = None
        elif self.group.name in ['Community Member']:
            self.site = None

        super(UserRole, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        if self.group.name == 'Super Admin':
            self.project = None
            self.site = None
        elif self.group.name == 'Field Engineer':
            self.project = None
        elif self.group.name == 'Project Manager':
            self.site = None
        elif self.group.name in ['Community Member']:
            self.site = None

        super(UserRole, self).save(*args, **kwargs)