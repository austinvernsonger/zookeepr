from zookeepr.lib.base import *
from zookeepr.lib.auth import SecureController
from zookeepr.model import Person

class HomeController(BaseController):

    def index(self):
        """The home page of the website.

        If the user has not signed in, then they are presented with the
        default page.

        Otherwise, they're shown the customised page.

        We rely on `c.signed_in_person` containing the Person object for
        the currently signed in user, but we don't want to redirect to
        the signin action if we're not signed in so we duplicate the
        __before__ code from SecureController here.
        """

        if 'signed_in_person_id' in session:
            # FIXME: get is boned on the live site, use get_by
            c.signed_in_person = Query(Person).get_by(id=session['signed_in_person_id'])

        resp = render_response('home.myt')

        return resp
