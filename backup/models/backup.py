import os

from django.db import models

from backup.enums import BACKUP_BUCKET
from backup.monster_interface import MonsterInterface


class Backup(models.Model):
    dir_path = models.TextField()
    crontab = models.CharField(max_length=20, default='0 * * * *')
    dest_dir_path = models.TextField()

    def run_backup(self):
        files = list()
        for (dir_path, dir_names, filenames) in os.walk(self.dir_path):
            files += [os.path.join(dir_path, file) for file in filenames]
        for file in files:
            MonsterInterface.create_obj_from_file(
                BACKUP_BUCKET,
                '%s/%s' % (self.dest_dir_path, file[len(self.dir_path) + 1:]),
                file
            )

