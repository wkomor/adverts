# created by Vitold Komorovski
# 06.09.2016
from django.core.cache import cache


class HitCountMixin(object):
    """
    Mixin to count hits
    """
    def increment_hit(self, view_object):
        """
        Method to increment hits and save it to DB
        :param view_object: object of the ad to increment hits
        """
        try:
            view_object.hits += 1
            view_object.save()
        except:
            pass

    def count_hit(self):
        """
        Method to count hits
        :return: True if hit has been counted or False if not
        """
        view_object = self.get_object()
        key = self.request.META['REMOTE_ADDR']+str(view_object.id)
        hit = cache.get(key)
        if not hit:
            self.increment_hit(view_object)
            cache.set(key, view_object.id, 3600*24)
            return True
        if hit != view_object.id:
            self.increment_hit(view_object)
            cache.set(key, view_object.id, 3600*24)
            return True
        return False
