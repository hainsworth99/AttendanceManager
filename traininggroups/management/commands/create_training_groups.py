from django.core.management.base import BaseCommand
from django.utils import timezone
from random import shuffle, seed


from users.models import CustomUser
from traininggroups.models import TrainingGroup


class Command(BaseCommand):

    help = 'Generates new training groups'

    def shuffle_users(self, user_info):
        seed()
        shuffle(user_info)
        return user_info


    def handle(self, *args, **kwargs):
        # get list of names/training group numbers
        self.stdout.write(self.style.SUCCESS('Generating new training groups...'))
        self.stdout.write(self.style.HTTP_SUCCESS('fetching user data...'))
        user_info = []
        for user in CustomUser.objects.all():
            user_info.append((
                user.first_name + ' ' + user.last_name,  # name
                user.training_group
            ))

        # randomize list order
        self.stdout.write(self.style.HTTP_SUCCESS('randomizing...'))
        user_info = self.shuffle_users(user_info)

        # split people into 4 approximately equal sized groups
        groups = [[],[],[],[]]
        for i in range(0, len(user_info)):
            groups[i % 4].append(user_info[i])

        # delete old groups
        self.stdout.write(self.style.HTTP_SUCCESS('deleting old groups...'))
        TrainingGroup.objects.all().delete()

        # create the new training group objects
        self.stdout.write(self.style.HTTP_SUCCESS('creating new groups...'))
        group_label = 1
        for group in groups:
            names = []
            for user in group:
                names.append(user[0])
            group = TrainingGroup(group_members=names, name=('Group ' + str(group_label)))
            group.save()
            group_label += 1

        self.stdout.write(self.style.SUCCESS('Training groups successfully created!'))
        for group in TrainingGroup.objects.all():
            self.stdout.write(self.style.MIGRATE_HEADING(group.name))
            for person in group.group_members:
                self.stdout.write(self.style.HTTP_SUCCESS('- ' + person))
